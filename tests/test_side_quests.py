"""Regressions for the public Side Quests section and generated exports."""
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from agent_content import Document, plain, normalise

class SideQuestsTests(unittest.TestCase):
    def test_first_side_quest_is_reachable_after_experience(self):
        doc = Document((ROOT / "index.html").read_text()).root
        sections = list(doc.descendants("section"))
        ids = [node.attrs.get("id") for node in sections]
        self.assertIn("side-quests", ids, "The selected project needs its own section")
        self.assertLess(ids.index("journey"), ids.index("side-quests"))
        self.assertLess(ids.index("side-quests"), ids.index("stories"))
        section = next(node for node in sections if node.attrs.get("id") == "side-quests")
        self.assertEqual(len(list(section.descendants("article"))), 1)
        self.assertIn("Jogo da Vida - Magnólia", normalise(plain(section)))
        links = {node.attrs.get("href") for node in section.descendants("a")}
        self.assertEqual(links, {
            "https://paulosanches.github.io/magnolia-jogo-da-vida/",
            "https://paulosanches.github.io/magnolia-jogo-da-vida/backstage/",
            "https://github.com/PauloSanches/magnolia-jogo-da-vida",
        })
        nav = next(node for node in doc.descendants("nav") if "explore-nav" in node.classes)
        self.assertIn("#side-quests", [node.attrs.get("href") for node in nav.descendants("a")])

    def test_localized_pages_and_agent_exports_include_the_selected_project(self):
        for prefix in ["", "pt/", "it/"]:
            with self.subTest(language=prefix or "en"):
                document = Document((ROOT / prefix / "index.html").read_text()).root
                sections = [n for n in document.descendants("section") if n.attrs.get("id") == "side-quests"]
                self.assertEqual(len(sections), 1, "The project must exist in every language")
                exported = (ROOT / prefix / "portfolio.md").read_text()
                self.assertIn("Portfolio/Side Quests", exported)
                self.assertIn("Jogo da Vida - Magnólia", exported)
                self.assertIn("https://paulosanches.github.io/magnolia-jogo-da-vida/backstage/", exported)
                self.assertNotIn("/backstage/v2/", exported)
                agent = (ROOT / prefix / "agent/index.html").read_text()
                self.assertIn("Jogo da Vida - Magnólia", agent)

if __name__ == "__main__":
    unittest.main()
