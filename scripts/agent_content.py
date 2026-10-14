"""Export public portfolio content to Markdown using only the standard library.

HTML remains the content source. Navigation and decorative controls are omitted;
disclosures, carousel items and the full text of every story are always included.
"""
import argparse
import html
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit

BASE = "https://paulosanches.github.io/hello/"
ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = {
    "": {"lang": "en", "name": "English", "source": "Source", "intro": "Complete public portfolio, including the full text of every Field Note. Generated from the published pages and kept in sync with site updates.", "stories": "Field Notes — full stories"},
    "pt": {"lang": "pt-BR", "name": "Português do Brasil", "source": "Fonte", "intro": "Portfólio público completo, incluindo o texto integral de cada história. Gerado a partir das páginas publicadas e sincronizado com as atualizações do site.", "stories": "Histórias — textos completos"},
    "it": {"lang": "it", "name": "Italiano", "source": "Fonte", "intro": "Portfolio pubblico completo, con il testo integrale di ogni storia. Generato dalle pagine pubblicate e sincronizzato con gli aggiornamenti del sito.", "stories": "Storie — testi completi"},
}
VIEW_LABELS = {
    "": ("Back to portfolio", "Open Markdown file", "Complete portfolio in Markdown"),
    "pt": ("Voltar ao portfólio", "Abrir arquivo Markdown", "Portfólio completo em Markdown"),
    "it": ("Torna al portfolio", "Apri il file Markdown", "Portfolio completo in Markdown"),
}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
SKIP_TAGS = {"script", "style", "svg", "nav", "button", "input", "select", "textarea", "summary"}
SKIP_CLASSES = {"hero-tools", "carousel-hint", "carousel-controls", "sr-only", "story-open", "certification-number", "contribution-number", "agent-mode-link"}
BLOCKS = {"article", "aside", "blockquote", "div", "figure", "figcaption", "footer", "header", "h1", "h2", "h3", "h4", "h5", "h6", "li", "main", "ol", "p", "pre", "section", "table", "ul"}


@dataclass
class Node:
    tag: str
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)

    @property
    def classes(self):
        return set(self.attrs.get("class", "").split())

    def descendants(self, tag=None):
        for child in self.children:
            if isinstance(child, Node):
                if tag is None or child.tag == tag:
                    yield child
                yield from child.descendants(tag)


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.root = Node("document")
        self.stack = [self.root]
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs))
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def omitted(node):
    return node.tag in SKIP_TAGS or node.attrs.get("aria-hidden") == "true" or bool(node.classes & SKIP_CLASSES)


def plain(node):
    if isinstance(node, str):
        return node
    if omitted(node):
        return ""
    if node.tag == "br":
        return " "
    return " ".join(plain(child) for child in node.children)


def normalise(value):
    return re.sub(r"\s+", " ", value).strip()


def escape(value):
    return re.sub(r"([\\`*\[\]<>_])", r"\\\1", value)


class Markdown:
    def __init__(self, url, source_label="Source", heading_offset=0):
        self.url, self.source_label, self.heading_offset = url, source_label, heading_offset

    def link(self, value):
        url = urljoin(self.url, value)
        if urlsplit(url).scheme not in {"https", "http"}:
            return None
        return url.replace(" ", "%20").replace("(", "%28").replace(")", "%29")

    def inline(self, node):
        if isinstance(node, str):
            return escape(re.sub(r"\s+", " ", node))
        if omitted(node):
            return ""
        if node.tag == "br":
            return " "
        if node.tag == "img":
            alt = node.attrs.get("alt", "")
            url = self.link(node.attrs.get("src", ""))
            return f"![{escape(alt)}]({url})" if alt and url else ""
        # A boundary between adjacent spans/time tags must not join words.
        parts = []
        for child in node.children:
            value = self.inline(child)
            parts.append(f" {value} " if isinstance(child, Node) and child.tag in {"span", "time", "small"} else value)
        inner = "".join(parts)
        inner = normalise(inner)
        if node.tag == "a":
            url = self.link(node.attrs.get("href", ""))
            return f"[{inner}]({url})" if inner and url else inner
        if node.tag in {"strong", "b"}:
            return f"**{inner}**"
        if node.tag in {"em", "i"}:
            return f"*{inner}*"
        if node.tag == "code":
            return f"`{normalise(plain(node))}`"
        return inner

    def render(self, node):
        if isinstance(node, str):
            return escape(normalise(node))
        if omitted(node):
            return ""
        tag = node.tag
        if re.fullmatch(r"h[1-6]", tag):
            level = min(6, max(2, int(tag[1]) + self.heading_offset))
            return "#" * level + " " + self.inline(node) + "\n\n"
        if tag in {"p", "figcaption"}:
            return self.inline(node) + "\n\n"
        if tag == "img":
            value = self.inline(node)
            return value + "\n\n" if value else ""
        if tag == "blockquote":
            value = self.children(node).strip()
            return "\n".join("> " + line for line in value.splitlines()) + "\n\n"
        if tag in {"ul", "ol"}:
            if "project-timeline" in node.classes or "carousel-track" in node.classes:
                return self.children(node)
            items = [c for c in node.children if isinstance(c, Node) and c.tag == "li"]
            rows = []
            for i, item in enumerate(items, 1):
                prefix = f"{i}. " if tag == "ol" else "- "
                lines = self.children(item).strip().splitlines()
                if lines:
                    rows.append((prefix + lines[0] + "\n" + "\n".join(" " * len(prefix) + line if line else "" for line in lines[1:])).rstrip())
            return "\n".join(rows).strip() + "\n\n"
        if tag == "a" and any(c.tag in BLOCKS for c in node.descendants()):
            value = self.children(node)
            url = self.link(node.attrs.get("href", ""))
            return value + f"{self.source_label}: {url}\n\n" if url else value
        if tag == "pre":
            return "```\n" + plain(node).strip() + "\n```\n\n"
        if tag == "hr":
            return "---\n\n"
        if tag not in BLOCKS and tag != "details":
            return self.inline(node)
        return self.children(node)

    def children(self, node):
        result, inline = [], []
        for child in node.children:
            if isinstance(child, Node) and (child.tag in BLOCKS or child.tag in {"details", "img", "hr"} or (child.tag == "a" and any(c.tag in BLOCKS for c in child.descendants()))):
                if inline:
                    value = normalise(" ".join(inline))
                    if value:
                        result.append(value + "\n\n")
                    inline = []
                result.append(self.render(child))
            else:
                inline.append(self.inline(child))
        value = normalise(" ".join(inline))
        if value:
            result.append(value + "\n\n")
        return "".join(result)


def page_main(path):
    doc = Document(path.read_text(encoding="utf-8"))
    return next(doc.root.descendants("main"))


def build_document(root, prefix):
    info = LANGUAGES[prefix]
    folder = root / prefix if prefix else root
    home_url = BASE + (prefix + "/" if prefix else "")
    home = page_main(folder / "index.html")
    intro = f"# Paulo Sanches\n\n{info['intro']}\n\nLanguage: {info['lang']}\n\n{info['source']}: {home_url}\n\n"
    alternates = " · ".join(f"[{v['name']}]({BASE}{k + '/' if k else ''}portfolio.md)" for k, v in LANGUAGES.items())
    output = intro + alternates + "\n\n---\n\n" + Markdown(home_url, info["source"]).render(home)
    # Discover stories from the page in presentation order, then include any
    # newly published story not yet linked on the homepage. Never rely on a
    # fixed count or hide the remainder of a carousel/disclosure.
    available = {p.parent.name: p for p in (folder / "field-notes").glob("*/index.html")}
    order = []
    for node in home.descendants("a"):
        path = urlsplit(urljoin(home_url, node.attrs.get("href", ""))).path
        match = re.search(r"/field-notes/([^/]+)/?(?:index\.html)?$", path)
        if match and match[1] in available and match[1] not in order:
            order.append(match[1])
    order.extend(sorted(set(available) - set(order)))
    output += f"---\n\n## {info['stories']}\n\n"
    for name in order:
        url = home_url + "field-notes/" + name + "/"
        main = page_main(available[name])
        output += f"{info['source']}: {url}\n\n" + Markdown(url, info["source"], heading_offset=1).render(main) + "---\n\n"
    return re.sub(r"\n{3,}", "\n\n", output).strip() + "\n"


def build_view(document, prefix):
    language = LANGUAGES[prefix]["lang"]
    back, download, description = VIEW_LABELS[prefix]
    home = BASE + (prefix + "/" if prefix else "")
    switches = " ".join(
        f'<a href="{BASE}{k + "/" if k else ""}agent/" lang="{v["lang"]}" hreflang="{v["lang"]}"' + (' aria-current="page"' if k == prefix else '') + f'>{"PT" if k == "pt" else "ITA" if k == "it" else "EN"}</a>'
        for k, v in LANGUAGES.items()
    )
    # Fully static: agents and no-JavaScript browsers can read the same file
    # content directly. Separate styling keeps the regular portfolio intact.
    return f'''<!doctype html>
<html lang="{language}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, follow">
  <meta name="description" content="{description}">
  <title>Paulo Sanches — AI/Agent</title>
  <link rel="canonical" href="{home}">
  <link rel="alternate" type="text/markdown" href="{home}portfolio.md" title="AI/Agent">
  <style>
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: #fafafa; color: #171717; font-family: system-ui, sans-serif; }}
    .wrap {{ width: min(1440px, calc(100% - 40px)); margin-inline: auto; }}
    header {{ padding-block: 20px; border-bottom: 1px solid #ccc; }}
    nav {{ display: flex; align-items: center; justify-content: space-between; gap: 12px 24px; flex-wrap: wrap; }}
    .languages {{ display: flex; gap: 4px; }}
    a {{ color: inherit; display: inline-flex; align-items: center; min-height: 44px; padding: 8px; text-underline-offset: 4px; }}
    a:focus-visible {{ outline: 2px solid #171717; outline-offset: 2px; }}
    [aria-current="page"] {{ background: #171717; color: white; }}
    h1 {{ margin: 0; padding-block: 28px 8px; font-size: clamp(24px, 4vw, 36px); }}
    .file-link {{ font-size: 14px; margin-bottom: 20px; }}
    pre {{ margin: 0 0 40px; padding: clamp(16px, 3vw, 32px); background: white; border: 1px solid #ddd; font: 14px/1.7 ui-monospace, SFMono-Regular, Consolas, monospace; white-space: pre-wrap; overflow-wrap: anywhere; tab-size: 2; }}
  </style>
</head>
<body>
  <header><nav class="wrap" aria-label="AI/Agent"><a href="{home}">← {back}</a><div class="languages">{switches}</div></nav></header>
  <main class="wrap"><h1>AI/Agent</h1><a class="file-link" href="{home}portfolio.md" type="text/markdown">{download} ↗</a><pre>{html.escape(document)}</pre></main>
</body>
</html>
'''


def build(root=ROOT, check=False):
    stale = []
    for prefix in LANGUAGES:
        value = build_document(root, prefix)
        folder = root / prefix if prefix else root
        for path, content in [(folder / "portfolio.md", value), (folder / "agent/index.html", build_view(value, prefix))]:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(str(path.relative_to(root)))
                if not check:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(content, encoding="utf-8")
    if check and stale:
        raise SystemExit("Outdated AI/Agent content: " + ", ".join(stale) + ". Run python3 scripts/build-locales.py.")
    return stale


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if committed Markdown differs from the public HTML.")
    args = parser.parse_args()
    changed = build(check=args.check)
    print("AI/Agent Markdown is up to date." if args.check else f"Generated 3 AI/Agent files and views; {len(changed)} updated.")
