#!/usr/bin/env python3
"""Build static Portuguese and Italian pages from the English HTML and translations.

Run from any directory with Python 3; only the standard library is required.
The generated pages are committed so GitHub Pages needs no runtime translation.
"""
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from zoneinfo import ZoneInfo
from agent_content import build as build_agent_content

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://paulosanches.github.io/hello/"
LOCALES = {"pt": ("pt-BR", "pt_BR"), "it": ("it", "it_IT")}
SOURCES = ["index.html", *(str(path.relative_to(ROOT))
           for section in ("field-notes", "portfolio", "setup")
           for path in sorted((ROOT / section).glob("*/index.html")))]
DATA = json.loads((ROOT / "locales/translations.json").read_text())
MONTHS = {
    "pt": ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"],
    "it": ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"],
}
EN_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
PRESERVE = {
    "Paulo Sanches", "English", "Italiano", "Português do Brasil", "EN", "ITA", "PT", "AI/Agent",
    "AWS", "GCP / Terraform", "Microsoft Entra ID", "Portugal", "Braga, Portugal",
    "Accenture · Coimbra, Portugal", "JNation", "FlashCamp", "Cubo", "for Devs.",
    "Cubo Itaú · Masterclass #2", "MASTERCLASS / 02", "Mindset", "LinkedIn",
    "Ruan Morais", "Giovana Andrade", "Wilton Junior", "Mercia Oliveira", "Lucas Medeiros",
    "“Você conhece o Zeno Rocha?”",
}
english_home = (ROOT / SOURCES[0]).read_text()
certificates = english_home[english_home.index('id="certifications"'):english_home.index('id="contact"')]
PRESERVE.update(html.unescape(s) for s in re.findall(r'<h3>(.*?)</h3>', certificates))
PRESERVE.update(html.unescape(s) for s in re.findall(r'<p class="certification-issuer">(.*?)</p>', certificates))


def translate(value, locale, strict=True):
    if value in DATA:
        return DATA[value][locale]
    if value in PRESERVE or not re.search(r"[A-Za-zÀ-ÿ]", value):
        return value
    date = re.fullmatch(r"(" + "|".join(EN_MONTHS) + r") (\d{4})", value)
    if date:
        return MONTHS[locale][EN_MONTHS.index(date[1])] + " " + date[2]
    if strict:
        raise ValueError(f"Missing {locale} translation: {value}")
    return value


class Localize(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self, source, locale, path):
        super().__init__(convert_charrefs=True)
        self.source, self.locale, self.path = source, locale, path
        self.language, self.og_locale = LOCALES[locale]
        self.url = BASE + locale + "/" + (path.removesuffix("index.html") if path != "index.html" else "")
        self.stack, self.edits = [], []
        self.lines = [0]
        self.lines.extend(m.end() for m in re.finditer("\n", source))
        self.feed(source)

    def source_offset(self):
        line, column = self.getpos()
        return self.lines[line - 1] + column

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        start = self.source_offset()
        raw = self.get_starttag_text()
        inside_svg = any(t == "svg" for t, _ in self.stack) or tag == "svg"
        if not inside_svg:
            def attribute(match):
                name, quote, original = match[1], match[2], html.unescape(match[3])
                value = original
                if tag == "html" and name == "lang":
                    value = self.language
                elif name in {"aria-label", "aria-roledescription", "alt", "title", "placeholder"} and value:
                    value = translate(value, self.locale)
                elif tag == "meta" and name == "content":
                    key = attrs.get("name", attrs.get("property"))
                    if key == "og:url":
                        value = self.url
                    elif key == "og:locale":
                        value = self.og_locale
                    elif key in {"description", "og:title", "og:description", "og:image:alt", "twitter:title", "twitter:description", "twitter:image:alt", "article:section"}:
                        value = translate(value, self.locale)
                elif tag == "link" and attrs.get("rel") == "canonical" and name == "href":
                    value = self.url
                elif name == "href" and original.startswith(BASE) and (attrs.get("type") == "text/markdown" or "agent-mode-link" in attrs.get("class", "").split()):
                    value = BASE + self.locale + "/" + original.removeprefix(BASE)
                if name in {"src", "href"} and re.match(r"^(?:\.\./)*assets/", value):
                    value = "../" + value
                return name + "=" + quote + html.escape(value, quote=True) + quote
            changed = re.sub(r'([\w:-]+)\s*=\s*([\'"])(.*?)\2', attribute, raw, flags=re.S)
            if tag == "a" and attrs.get("hreflang"):
                changed = changed.replace(' aria-current="page"', "")
                if attrs["hreflang"] == self.language:
                    changed = changed[:-1] + ' aria-current="page">'
            if (tag == "p" and "mindset-saying" in attrs.get("class", "")) or (tag == "h3" and any("certification-content" in a.get("class", "") for _, a in self.stack)):
                changed = changed[:-1] + ' lang="en">'
            if changed != raw:
                self.edits.append((start, start + len(raw), changed))
        if tag not in self.VOID:
            self.stack.append((tag, attrs))

    def handle_startendtag(self, tag, attributes):
        self.handle_starttag(tag, attributes)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        if not data.strip() or any(t in {"script", "style", "svg"} for t, _ in self.stack):
            return
        if any(t == "head" for t, _ in self.stack) and not any(t == "title" for t, _ in self.stack):
            return
        if any((t == "h3" and "lang" in a) or (t == "p" and "mindset-saying" in a.get("class", "")) for t, a in self.stack):
            return  # Preserve Paulo's original personal quotations and their language labels.
        start = self.source_offset()
        end = self.source.find("<", start)
        if end < 0:
            end = len(self.source)
        raw = self.source[start:end]
        value = html.unescape(raw).strip()
        replacement = translate(value, self.locale)
        if replacement != value:
            leading = raw[:len(raw) - len(raw.lstrip())]
            trailing = raw[len(raw.rstrip()):]
            self.edits.append((start, end, leading + html.escape(replacement, quote=False) + trailing))

    def result(self):
        result = self.source
        for start, end, replacement in sorted(self.edits, reverse=True):
            result = result[:start] + replacement + result[end:]
        match = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', result, re.S)
        graph = json.loads(match[2])
        page_base = BASE + ("" if self.path == "index.html" else self.path.removesuffix("index.html"))
        page_types = {"ProfilePage", "WebPage", "BlogPosting", "BreadcrumbList"}

        def localize_graph(value, page=False):
            if isinstance(value, list):
                return [localize_graph(v, page) for v in value]
            if isinstance(value, dict):
                identifier = value.get("@id", "")
                own_page = value.get("@type") in page_types or page or (identifier.startswith(page_base + "#") and identifier[len(page_base):] not in {"#person", "#website", "#portrait"})
                output = {k: localize_graph(v, own_page) for k, v in value.items()}
                if value.get("@type") in {"ProfilePage", "WebPage", "BlogPosting"}:
                    output["inLanguage"] = self.language
                return output
            if isinstance(value, str):
                if page and (value == page_base or value.startswith(page_base + "#")):
                    fragment = value[len(page_base):]
                    if fragment not in {"#person", "#website", "#portrait"}:
                        return self.url + fragment
                if page and (value == BASE or (value.startswith(BASE + "#") and value[len(BASE):] not in {"#person", "#website", "#portrait"})):
                    return BASE + self.locale + "/" + value[len(BASE):]
                return translate(value, self.locale, strict=False)
            return value

        graph = localize_graph(graph)
        result = result[:match.start(2)] + "\n  " + json.dumps(graph, ensure_ascii=False, indent=2).replace("\n", "\n  ") + "\n  " + result[match.end(2):]
        return result


def main():
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    existing_dates = {}
    if (ROOT / "sitemap.xml").exists():
        for entry in ET.parse(ROOT / "sitemap.xml").getroot():
            existing_dates[entry.findtext(f"{{{namespace}}}loc")] = entry.findtext(f"{{{namespace}}}lastmod")
    today = datetime.now(ZoneInfo("Europe/Lisbon")).date().isoformat()
    # Update shared asset versions before deriving every page.
    versions = {kind: hashlib.sha256((ROOT / f"assets/{name}").read_bytes()).hexdigest()[:12]
                for kind, name in [("css", "style.css"), ("js", "app.js")]}
    sources = {}
    for path in SOURCES:
        source = (ROOT / path).read_text()
        for kind, name in [("css", "style.css"), ("js", "app.js")]:
            source = re.sub(r"(assets/" + re.escape(name) + r"\?v=)[a-f0-9]+", lambda m: m[1] + versions[kind], source)
        sources[path] = source
    generated = {f"{locale}/{path}": Localize(source, locale, path).result()
                 for locale in LOCALES for path, source in sources.items()}
    changed_paths = set()
    for path, source in {**sources, **generated}.items():
        target = ROOT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.read_text() != source:
            changed_paths.add(path)
            target.write_text(source)

    alternate = "http://www.w3.org/1999/xhtml"
    ET.register_namespace("", namespace)
    ET.register_namespace("xhtml", alternate)
    sitemap = ET.Element(f"{{{namespace}}}urlset")
    for path in SOURCES:
        suffix = "" if path == "index.html" else path.removesuffix("index.html")
        variants = {"en": BASE + suffix, "it": BASE + "it/" + suffix, "pt-BR": BASE + "pt/" + suffix}
        for url in variants.values():
            entry = ET.SubElement(sitemap, f"{{{namespace}}}url")
            ET.SubElement(entry, f"{{{namespace}}}loc").text = url
            file_path = url.removeprefix(BASE) + "index.html"
            ET.SubElement(entry, f"{{{namespace}}}lastmod").text = today if file_path in changed_paths else (existing_dates.get(url) or today)
            for language, variant in {**variants, "x-default": variants["en"]}.items():
                ET.SubElement(entry, f"{{{alternate}}}link", rel="alternate", hreflang=language, href=variant)
    ET.indent(sitemap, space="  ")
    (ROOT / "sitemap.xml").write_bytes(ET.tostring(sitemap, encoding="UTF-8", xml_declaration=True) + b"\n")
    build_agent_content(ROOT)
    print(f"Built {len(generated)} localized pages; shared CSS {versions['css']}, JS {versions['js']}.")


if __name__ == "__main__":
    main()
