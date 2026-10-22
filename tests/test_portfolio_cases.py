"""Portfolio cases are product pages, not Field Notes or Backstage redirects."""
import hashlib
import json
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from agent_content import BASE, Document, normalise, plain

CASE = "portfolio/jogo-da-vida-magnolia/"
TITLE = "Jogo da Vida - Magnólia"
LEAD = "An interactive board game built around storytelling and reflection."
SUMMARY = "An interactive board game with illustrated stories and reflection prompts, explored at the player's own pace."
# Literal approved public copy: the build and tests never need private review files.
PARAGRAPHS = [
    "Jogo da Vida - Magnólia brings together 12 illustrated spaces, character stories and 10 reflection prompts in a browser-based game for desktop and mobile. Players control the pace. There is no scoring or answer form; the questions are intended for discussion outside the application.",
    "Each space connects a position on the board to a story. The text appears progressively, followed by a question that keeps the story visible for reference.",
    "Players can move forward, return to an earlier space, pause the text reveal or restart the game. Moving to the next space is always a manual choice.",
    "HTML, CSS and SVG define the interface and illustrated board. JavaScript manages the active space, story/question state and transitions in the browser. GitHub Pages serves the static application; the game requires no application backend or database.",
    "A dedicated playback controller manages the current job, timer and typing, waiting and paused states. It uses a 24 ms timer step and a 3,000 ms reading delay before presenting a question. Automatic presentation waits while text is selected, the reading panel has keyboard focus or unread content remains below the scroll position.",
    "Navigation cancels pending playback work, while busy-state guards prevent overlapping transitions. Pausing or hiding the tab suspends scheduling. Moving between board spaces remains manual.",
    "The full text reserves its layout space before the typing effect begins, rather than resizing the bubble with each character. A separate visual layer handles the reveal while the complete text remains available to assistive technology.",
    "The interface supports keyboard navigation and prefers-reduced-motion. Story and question remain visible together.",
    "Google Sheets supported collaborative editing during preparation. After editorial approval, that dependency was removed and the final content was published alongside the code. This keeps the narrative tied to a release, at the cost of requiring a new deployment for content changes.",
    "Automated checks cover content, navigation, images and layout, complemented by browser verification at different viewport sizes.",
    "A release script writes the same UTC timestamp into the page and version.json, and adds SHA-256-derived version parameters to JavaScript and CSS URLs. Its check mode verifies timestamp consistency; it does not recalculate asset hashes. Published files and browser behavior are checked separately to confirm the delivered revision.",
    "Hermes Agent and Codex supported implementation and testing on a MacBook Air M1, with requests and reviews through Telegram. ChatGPT generated character illustrations from supplied photographs; Hermes prepared and integrated the assets. Reusable skills guided design, testing, debugging and review. These tools belong to the development workflow, not the game's runtime."
]
ALT = "Screenshot of Jogo da Vida - Magnólia, showing the illustrated board at its final space."
CAPTION = "The illustrated board at the end of the game."
DESTINATIONS = {
    "Open the game": "https://paulosanches.github.io/magnolia-jogo-da-vida/",
    "Code on GitHub": "https://github.com/PauloSanches/magnolia-jogo-da-vida",
    "Behind the scenes": "https://paulosanches.github.io/magnolia-jogo-da-vida/backstage/",
}


class PortfolioCaseTests(unittest.TestCase):
    def test_case_presents_approved_product_copy_in_story_page_layout(self):
        path = ROOT / CASE / "index.html"
        self.assertTrue(path.exists(), "The card needs a dedicated internal portfolio case")
        self.assertEqual(hashlib.sha256((ROOT / "assets/side-quest-magnolia.png").read_bytes()).hexdigest(),
                         "7fd422ebf5d609af4058a6e1615a1ec28fe9b874c086e09b76f79029670f4000")
        doc = Document(path.read_text()).root
        body = next(doc.descendants("body"))
        self.assertIn("story-page", body.classes)
        main = next(doc.descendants("main"))
        self.assertEqual(normalise(plain(next(main.descendants("h1")))), TITLE)
        self.assertEqual([normalise(plain(n)) for n in main.descendants("h2")],
                         ["The product", "The experience", "Technical design", "Explore the project"])
        prose = next(n for n in main.descendants("div") if "story-prose" in n.classes)
        self.assertEqual([normalise(plain(n)) for n in prose.descendants("p")], PARAGRAPHS)
        text = normalise(plain(main))
        for value in [LEAD, "Portfolio / Side Quests", CAPTION, "View full-size screenshot", "Game and backstage in Portuguese."]:
            self.assertIn(value, text)
        self.assertNotRegex(text, r"Field Notes|Continue the conversation|weekend|commits")
        image = next(main.descendants("img"))
        self.assertEqual(image.attrs["alt"], ALT)
        self.assertEqual((image.attrs["width"], image.attrs["height"]), ("1440", "1000"))
        self.assertEqual(urljoin(BASE + CASE, image.attrs["src"]), BASE + "assets/side-quest-magnolia.png")
        visual = next(n for n in main.descendants("figure") if "story-page-visual" in n.classes)
        for link in visual.descendants("a"):
            self.assertEqual(urljoin(BASE + CASE, link.attrs["href"]), BASE + "assets/side-quest-magnolia.png")
            self.assertEqual(link.attrs.get("target"), "_blank")
        actions = [n for n in main.descendants("a") if n.attrs.get("href") in DESTINATIONS.values()]
        self.assertEqual([normalise(plain(n)) for n in actions], list(DESTINATIONS))
        for action in actions:
            self.assertEqual(action.attrs["href"], DESTINATIONS[normalise(plain(action))])
            self.assertEqual(action.attrs.get("target"), "_blank")
            self.assertEqual(set(action.attrs.get("rel", "").split()), {"noopener", "noreferrer"})
            self.assertIn("opens in a new tab", "".join(str(n.children) for n in action.descendants("span")))
        returns = [n for n in doc.descendants("a") if normalise(plain(n)) == "Back to portfolio"]
        self.assertEqual(len(returns), 2)
        self.assertTrue(all(n.attrs.get("href") == "../../#side-quests" for n in returns))
        self.assertNotIn("Return to Field Notes", path.read_text())

    def test_localized_case_metadata_navigation_and_sitemap(self):
        import xml.etree.ElementTree as ET
        translations = json.loads((ROOT / "locales/translations.json").read_text())
        variants = {"en": BASE + CASE, "it": BASE + "it/" + CASE, "pt-BR": BASE + "pt/" + CASE, "x-default": BASE + CASE}
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9", "x": "http://www.w3.org/1999/xhtml"}
        sitemap = ET.parse(ROOT / "sitemap.xml").getroot()
        for prefix, language in [("", "en"), ("pt/", "pt-BR"), ("it/", "it")]:
            with self.subTest(locale=language):
                path = ROOT / prefix / CASE / "index.html"
                self.assertTrue(path.exists(), "Build the case in every supported locale")
                source = path.read_text()
                doc = Document(source).root
                url = BASE + prefix + CASE
                translate = lambda value: translations[value][prefix.rstrip("/")] if prefix else value
                self.assertEqual(next(doc.descendants("html")).attrs["lang"], language)
                self.assertEqual(normalise(plain(next(doc.descendants("title")))), translate(TITLE + " | Paulo Sanches"))
                links = list(doc.descendants("link"))
                self.assertEqual(next(n.attrs["href"] for n in links if n.attrs.get("rel") == "canonical"), url)
                self.assertEqual({n.attrs["hreflang"]: n.attrs["href"] for n in links if "hreflang" in n.attrs}, variants)
                self.assertEqual(next(n.attrs["href"] for n in links if n.attrs.get("type") == "text/markdown"), url + "case.md")
                meta = {n.attrs.get("name", n.attrs.get("property")): n.attrs.get("content") for n in doc.descendants("meta")}
                self.assertEqual(meta["description"], translate(LEAD))
                self.assertEqual(meta["og:url"], url)
                self.assertEqual(meta["og:image"], BASE + "assets/side-quest-magnolia.png")
                self.assertEqual(meta["twitter:image"], meta["og:image"])
                self.assertEqual(meta["og:image:alt"], translate(ALT))
                self.assertEqual(meta["twitter:description"], translate(LEAD))
                self.assertEqual(meta["og:title"], translate(TITLE + " — Paulo Sanches"))
                graph = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', source, re.S)[1])["@graph"]
                page = next(n for n in graph if n["@type"] == "WebPage")
                self.assertEqual(page["url"], url)
                self.assertEqual(page["@id"], url + "#webpage")
                self.assertEqual(page["inLanguage"], language)
                self.assertEqual(page["description"], translate(LEAD))
                self.assertFalse(any(n["@type"] == "BlogPosting" for n in graph))
                crumbs = next(n for n in graph if n["@type"] == "BreadcrumbList")["itemListElement"]
                self.assertEqual([n["item"] for n in crumbs], [BASE + prefix, BASE + prefix + "#side-quests", url])
                self.assertEqual(crumbs[1]["name"], translate("Portfolio / Side Quests"))
                anchors = list(doc.descendants("a"))
                self.assertEqual({n.attrs["hreflang"]: urljoin(url, n.attrs["href"]) for n in anchors if "hreflang" in n.attrs}, {k:v for k,v in variants.items() if k != "x-default"})
                self.assertEqual([n.attrs["hreflang"] for n in anchors if n.attrs.get("aria-current") == "page"], [language])
                self.assertEqual(next(n.attrs["href"] for n in anchors if "agent-mode-link" in n.classes), url + "agent/")
                for n in anchors:
                    if n.attrs.get("href", "").endswith("#side-quests"):
                        self.assertEqual(urljoin(url, n.attrs["href"]), BASE + prefix + "#side-quests")
                prose = next(n for n in doc.descendants("div") if "story-prose" in n.classes)
                self.assertEqual([normalise(plain(n)) for n in prose.descendants("p")], [translate(p) for p in PARAGRAPHS])
                self.assertEqual({n.attrs["href"] for n in anchors if n.attrs.get("href") in DESTINATIONS.values()}, set(DESTINATIONS.values()))
                image = next(doc.descendants("img"))
                self.assertEqual(urljoin(url, image.attrs["src"]), BASE + "assets/side-quest-magnolia.png")
                entries = [n for n in sitemap if n.findtext("s:loc", namespaces=ns) == url]
                self.assertEqual(len(entries), 1)
                self.assertEqual({n.attrib["hreflang"]: n.attrib["href"] for n in entries[0].findall("x:link", ns)}, variants)

    def test_case_exports_are_complete_localized_and_keep_agent_navigation(self):
        from agent_content import agent_url
        from test_agent_content import text_nodes
        case_headings = {"": "Portfolio / Side Quests — full case studies", "pt/": "Portfolio / Side Quests — estudos de caso completos", "it/": "Portfolio / Side Quests — casi di studio completi"}
        for prefix in case_headings:
            with self.subTest(locale=prefix or "en"):
                folder = ROOT / prefix / CASE
                self.assertTrue((folder / "case.md").exists(), "Cases need their own Markdown export")
                self.assertTrue((folder / "agent/index.html").exists(), "Cases need their own AI/Agent view")
                url = BASE + prefix + CASE
                output = (folder / "case.md").read_text()
                complete = (ROOT / prefix / "portfolio.md").read_text()
                self.assertIn("## " + case_headings[prefix], complete)
                self.assertIn("Markdown: " + url + "case.md", complete)
                for text in text_nodes(next(Document((folder / "index.html").read_text()).root.descendants("main"))):
                    for document in [output, complete]:
                        self.assertIn(text, normalise(re.sub(r"\\([\\`*\[\]<>_])", r"\1", document)))
                self.assertEqual(output.count("# " + TITLE + "\n"), 1)
                self.assertIn("](" + BASE + prefix + "agent/)", output)
                self.assertNotIn("story.md", output)
                self.assertNotRegex(output, r"Field Notes|mailto:|tel:|<script|/Users/")
                for destination in DESTINATIONS.values():
                    self.assertIn(destination, output)
                    self.assertEqual(agent_url(destination), destination)
                for locale in ["", "it/", "pt/"]:
                    self.assertIn(BASE + locale + CASE + "case.md", output)
                view = Document((folder / "agent/index.html").read_text()).root
                pre = next(view.descendants("pre"))
                def raw_text(node):
                    return node if isinstance(node, str) else "".join(raw_text(n) for n in node.children)
                self.assertEqual(raw_text(pre), output)
                self.assertEqual(next(n.attrs["href"] for n in view.descendants("link") if n.attrs.get("rel") == "canonical"), url)
                self.assertEqual(next(n.attrs["href"] for n in view.descendants("a") if "file-link" in n.classes), url + "case.md")
                self.assertEqual({n.attrs["href"] for n in view.descendants("a") if n.attrs.get("hreflang")}, {BASE + locale + CASE + "agent/" for locale in ["", "it/", "pt/"]})
                for suffix in ["", "index.html", "?reader=1#technical", "index.html?reader=1#technical"]:
                    expected_suffix = suffix.removeprefix("index.html")
                    self.assertEqual(agent_url(url + suffix), url + "agent/" + expected_suffix)
                self.assertEqual(agent_url(url + "case.md"), url + "case.md")
                self.assertEqual(agent_url(BASE + "assets/side-quest-magnolia.png"), BASE + "assets/side-quest-magnolia.png")

    def test_technical_details_have_ordered_subsections(self):
        translations = json.loads((ROOT / "locales/translations.json").read_text())
        headings = ['Runtime architecture', 'Playback and navigation', 'Reading layout and accessibility', 'Content and versioning', 'Testing and releases', 'Development tooling']
        for prefix in ["", "pt/", "it/"]:
            with self.subTest(locale=prefix or "en"):
                doc = Document((ROOT / prefix / CASE / "index.html").read_text()).root
                actual = [normalise(plain(n)) for n in doc.descendants("h3")]
                expected = [translations[h][prefix.rstrip("/")] for h in headings] if prefix else headings
                self.assertEqual(actual, expected)
        self.assertNotRegex(" ".join(PARAGRAPHS[:3]), r"Hermes|Codex")
        self.assertIn("not the game's runtime", PARAGRAPHS[-1])

    def test_home_card_is_concise_and_opens_local_case_in_same_tab(self):
        summaries = {
            "": SUMMARY,
            "pt/": "Um jogo de tabuleiro interativo com histórias ilustradas e perguntas para reflexão, explorado no ritmo de cada jogador.",
            "it/": "Un gioco da tavolo interattivo con storie illustrate e domande di riflessione, da esplorare al proprio ritmo.",
        }
        labels = {"": "Read case study", "pt/": "Ler estudo de caso", "it/": "Leggi il caso di studio"}
        for prefix, summary in summaries.items():
            with self.subTest(locale=prefix or "en"):
                doc = Document((ROOT / prefix / "index.html").read_text()).root
                card = next(n for n in doc.descendants("article") if "side-quest-card" in n.classes)
                self.assertEqual([normalise(plain(n)) for n in card.descendants("p")], [summary])
                self.assertEqual(normalise(plain(next(card.descendants("h3")))), TITLE)
                links = list(card.descendants("a"))
                self.assertEqual(len(links), 1)
                self.assertEqual(links[0].attrs["href"], CASE)
                self.assertNotIn("target", links[0].attrs)
                self.assertEqual(normalise(plain(links[0])), labels[prefix])
                self.assertEqual(urljoin(BASE + prefix, links[0].attrs["href"]), BASE + prefix + CASE)
                self.assertNotIn("opens in a new tab", str(links[0]))
                self.assertNotRegex(normalise(plain(card)), r"Hermes|Codex|12|10")
                exported = (ROOT / prefix / "portfolio.md").read_text()
                self.assertIn(f"[{labels[prefix]}]({BASE}{prefix}{CASE}agent/)", exported)

    def test_case_text_view_uses_case_metadata_and_separates_caption_action(self):
        descriptions = {"": "Case study in Markdown", "pt/": "Estudo de caso em Markdown", "it/": "Caso di studio in Markdown"}
        translations = json.loads((ROOT / "locales/translations.json").read_text())
        for prefix, label in descriptions.items():
            with self.subTest(locale=prefix or "en"):
                folder = ROOT / prefix / CASE
                doc = Document((folder / "agent/index.html").read_text()).root
                description = next(n.attrs["content"] for n in doc.descendants("meta") if n.attrs.get("name") == "description")
                self.assertEqual(description, label + ": " + TITLE)
                translate = lambda value: translations[value][prefix.rstrip("/")] if prefix else value
                markdown = (folder / "case.md").read_text()
                self.assertIn(translate(CAPTION) + " [" + translate("View full-size screenshot") + "]", markdown)

    def test_content_sync_includes_case_markdown_and_generated_case_directory(self):
        import shlex
        workflow = (ROOT / ".github/workflows/sync-agent-content.yml").read_text()
        watched = re.findall(r"^\s+- '([^']+)'$", workflow, re.M)
        for pattern in ["portfolio/**/case.md", "pt/portfolio/**/case.md", "it/portfolio/**/case.md"]:
            self.assertIn(pattern, watched, "Case exports must stay synchronized after edits")
        staged = shlex.split(next(line.strip() for line in workflow.splitlines() if line.strip().startswith("git add --")))
        self.assertIn("portfolio", staged, "Stage generated English cases as well as localized outputs")


if __name__ == "__main__":
    unittest.main()
