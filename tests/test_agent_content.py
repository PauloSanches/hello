"""Check completeness, public-only output and automatic refresh of agent exports."""
from pathlib import Path
import re
import sys
import tempfile
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from agent_content import BASE, LANGUAGES, Document, Markdown, build, build_document, normalise, omitted, page_main


def text_nodes(node):
    if isinstance(node, str):
        if normalise(node):
            yield normalise(node)
    elif not omitted(node):
        for child in node.children:
            yield from text_nodes(child)


class AgentContentTests(unittest.TestCase):
    def test_disclosures_and_all_carousel_items_without_ui_or_scripts(self):
        source = '<main><nav>navigation only</nav><details><summary>show more</summary><p>Full experience.</p></details><ol class="carousel-track"><li><p>First.</p></li><li hidden><p>Last.</p></li></ol><button>Next</button><svg><text>decoration</text></svg><script>private script</script></main>'
        output = Markdown(BASE).render(next(Document(source).root.descendants("main")))
        for value in ["Full experience.", "First.", "Last."]:
            self.assertIn(value, output)
        for value in ["navigation only", "show more", "Next", "decoration", "private script"]:
            self.assertNotIn(value, output)

    def test_inline_formatting_links_and_punctuation(self):
        source = '<main><p>Meet <a href="field-notes/test/">Paulo</a>. <strong>Ready</strong> to go.</p><img src="assets/test.png" alt="A [diagram]"><p><span>Issued</span><time>Oct 2023</time></p></main>'
        output = Markdown(BASE).render(next(Document(source).root.descendants("main")))
        self.assertIn(f"Meet [Paulo]({BASE}field-notes/test/). **Ready** to go.", output)
        self.assertIn(f"![A \\[diagram\\]]({BASE}assets/test.png)", output)
        self.assertIn("Issued Oct 2023", output)

    def test_complete_public_content_in_each_language(self):
        for prefix in LANGUAGES:
            with self.subTest(locale=prefix or "en"):
                folder = ROOT / prefix if prefix else ROOT
                output = build_document(ROOT, prefix)
                # Remove formatting escapes for content comparison, not URLs.
                visible_output = normalise(re.sub(r"\\([\\`*\[\]<>_])", r"\1", output))
                sources = [folder / "index.html", *sorted((folder / "field-notes").glob("*/index.html"))]
                for source in sources:
                    main = page_main(source)
                    for text in text_nodes(main):
                        self.assertIn(text, visible_output, f"Missing public content from {source.relative_to(ROOT)}")
                self.assertEqual(output.count("# Paulo Sanches\n"), 1)
                self.assertNotRegex(output, r"(?i)mailto:|tel:|<script|dataLayer|G-1ZQYS54JD0")
                # Published credential descriptions/dates and complete stories
                # are covered above, including content not initially visible.
                home = page_main(folder / "index.html")
                for node in home.descendants("a"):
                    if "story-card-link" in node.classes:
                        slug = urlsplit(node.attrs["href"]).path.strip("/").split("/")[-1]
                        self.assertIn(f"field-notes/{slug}/", output)
                for url in re.findall(r"\]\(([^)]+)\)", output):
                    self.assertTrue(url.startswith(("https://", "http://")), url)
                    if url.startswith(BASE):
                        path = urlsplit(url).path.removeprefix("/hello/")
                        local = ROOT / path
                        self.assertTrue(local.exists(), f"Broken public link: {url}")

    def test_refresh_after_home_story_and_new_story_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for prefix in LANGUAGES:
                folder = root / prefix if prefix else root
                folder.mkdir(parents=True, exist_ok=True)
                (folder / "index.html").write_text('<main><h1>Initial headline</h1><a href="field-notes/a/"><div><h2>Story A</h2></div></a></main>')
                story = folder / "field-notes/a/index.html"
                story.parent.mkdir(parents=True)
                story.write_text('<main><article><h1>Story A</h1><p>Entire first story.</p></article><section><p>Conversation CTA.</p></section></main>')
            self.assertEqual(len(build(root)), 6)
            self.assertEqual(build(root), [])
            self.assertEqual(build(root, check=True), [])
            (root / "index.html").write_text('<main><h1>Changed headline</h1></main>')
            (root / "field-notes/a/index.html").write_text('<main><h1>Updated story</h1><p>Changed full story.</p></main>')
            new_story = root / "field-notes/b/index.html"
            new_story.parent.mkdir()
            new_story.write_text('<main><h1>New story</h1><p>A newly published story.</p></main>')
            with self.assertRaises(SystemExit):
                build(root, check=True)
            self.assertEqual(build(root), ["portfolio.md", "agent/index.html"])
            output = (root / "portfolio.md").read_text()
            for value in ["Changed headline", "Changed full story.", "A newly published story."]:
                self.assertIn(value, output)
            self.assertNotIn("Initial headline", output)
            self.assertEqual(build(root, check=True), [])


if __name__ == "__main__":
    unittest.main()
