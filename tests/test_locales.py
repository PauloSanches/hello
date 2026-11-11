"""Every published page and AI reader must support the same four languages."""
import json
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from agent_content import BASE, Document, LANGUAGES, LANGUAGE_LABELS, normalise, plain


class LocaleTests(unittest.TestCase):
    def test_language_discovery_and_switchers_preserve_each_page(self):
        sources = [ROOT / "index.html", *(p for section in ("field-notes", "portfolio", "setup")
                                        for p in (ROOT / section).glob("*/index.html"))]
        self.assertEqual(set(LANGUAGES), {"", "pt", "it", "es"})
        for source in sources:
            relative = source.relative_to(ROOT)
            suffix = "" if str(relative) == "index.html" else str(relative).removesuffix("index.html")
            variants = {info["lang"]: BASE + (prefix + "/" if prefix else "") + suffix
                        for prefix, info in LANGUAGES.items()}
            for prefix, info in LANGUAGES.items():
                path = ROOT / prefix / relative
                doc = Document(path.read_text()).root
                url = variants[info["lang"]]
                with self.subTest(page=path.relative_to(ROOT)):
                    self.assertEqual(next(doc.descendants("html")).attrs["lang"], info["lang"])
                    links = list(doc.descendants("link"))
                    self.assertEqual(next(n.attrs["href"] for n in links if n.attrs.get("rel") == "canonical"), url)
                    self.assertEqual({n.attrs["hreflang"]: n.attrs["href"] for n in links if "hreflang" in n.attrs},
                                     {**variants, "x-default": variants["en"]})
                    switcher = next(n for n in doc.descendants() if "language-switcher" in n.classes)
                    self.assertEqual(switcher.tag, "details")
                    self.assertNotIn("open", switcher.attrs)
                    summary = next(switcher.descendants("summary"))
                    self.assertEqual(normalise(plain(next(summary.descendants("span")))), LANGUAGE_LABELS[info["lang"]][0])
                    controls = list(switcher.descendants("a"))
                    self.assertEqual({n.attrs["hreflang"]: urljoin(url, n.attrs["href"]) for n in controls}, variants)
                    self.assertEqual([n.attrs["hreflang"] for n in controls if n.attrs.get("aria-current") == "page"], [info["lang"]])
                    self.assertEqual([normalise(plain(n)) for n in controls], [name for _, name in LANGUAGE_LABELS.values()])
                    reader = Document((path.parent / "agent/index.html").read_text()).root
                    menu = next(n for n in reader.descendants("details") if "language-switcher" in n.classes)
                    self.assertEqual(normalise(plain(next(next(menu.descendants("summary")).descendants("span")))), LANGUAGE_LABELS[info["lang"]][0])
                    self.assertEqual({n.attrs["hreflang"]: n.attrs["href"] for n in menu.descendants("a")},
                                     {lang: url + "agent/" for lang, url in variants.items()})

    def test_spanish_content_assets_and_local_links_exist(self):
        translations = json.loads((ROOT / "locales/translations.json").read_text())
        self.assertTrue(all(isinstance(value.get("es"), str) and value["es"].strip()
                            for value in translations.values()))
        for path in (ROOT / "es").rglob("index.html"):
            doc = Document(path.read_text()).root
            url = BASE + str(path.parent.relative_to(ROOT)) + "/"
            for node in doc.descendants():
                attr = "src" if node.tag == "img" else "href" if node.tag == "a" else None
                if not attr or not node.attrs.get(attr):
                    continue
                resolved = urljoin(url, node.attrs[attr])
                if resolved.startswith(BASE):
                    local = ROOT / urlsplit(resolved).path.removeprefix("/hello/")
                    self.assertTrue(local.exists(), resolved)

    def test_spanish_keeps_original_mindset_quotes_and_unreleased_cards(self):
        source = Document((ROOT / "index.html").read_text()).root
        spanish = Document((ROOT / "es/index.html").read_text()).root
        original_quotes = [normalise(plain(n)) for n in source.descendants("h3") if n.attrs.get("lang") == "pt-BR"]
        translated_quotes = [normalise(plain(n)) for n in spanish.descendants("h3") if n.attrs.get("lang") == "pt-BR"]
        self.assertEqual(translated_quotes, original_quotes)
        for name in ("story-tools", "story-routine", "story-ai"):
            card = next(n for n in spanish.descendants("article") if name in n.classes)
            self.assertFalse(list(card.descendants("a")))
        for slug in ("ai", "tools-and-apps", "work-routine"):
            self.assertFalse((ROOT / "es/setup" / slug / "index.html").exists())


if __name__ == "__main__":
    unittest.main()
