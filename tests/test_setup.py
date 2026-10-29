"""Check that categorized equipment and links survive the setup's Markdown export."""
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from agent_content import build_detail_document,Document,Markdown,BASE,normalise,plain
class SetupTests(unittest.TestCase):
 def test_markdown_keeps_availability_status_but_omits_decorative_cta(self):
  doc=Document('<div><span class="story-open">Explore my setup →</span><span class="story-open setup-card-status">Coming soon</span></div>')
  output=Markdown(BASE).render(next(doc.root.descendants('div')))
  self.assertIn('Coming soon',output)
  self.assertNotIn('Explore my setup',output)
 def test_table_keeps_headers_images_and_product_links(self):
  doc=Document('<table><thead><tr><th>Photo</th><th>Item</th></tr></thead><tbody><tr><td><img src="assets/test.webp" alt="Keyboard"></td><td><a href="https://example.com/item">MX Keys</a></td></tr></tbody></table>')
  output=Markdown(BASE).render(next(doc.root.descendants('table')))
  self.assertIn('| Photo | Item |',output)
  self.assertIn('| --- | --- |',output)
  self.assertIn('![Keyboard]('+BASE+'assets/test.webp)',output)
  self.assertIn('[MX Keys](https://example.com/item)',output)
 def test_setup_exports_all_categorized_equipment_and_product_links(self):
  for prefix in ['', 'pt','it']:
   folder=ROOT/prefix if prefix else ROOT
   main=Document((folder/'setup/my-setup/index.html').read_text())
   output=build_detail_document(ROOT,prefix,'my-setup','setup')
   sections=[n for n in main.root.descendants('section') if 'setup-uses' in n.classes]
   self.assertEqual(len(sections),3)
   self.assertEqual(len(list(main.root.descendants('table'))),0)
   items=[n for section in sections for n in section.descendants('li')]
   self.assertEqual(len(items),9)
   images=[image for item in items for image in item.descendants('img')]
   self.assertEqual(len(images),9)
   for image in images:
    self.assertIn('assets/'+image.attrs['src'].split('assets/',1)[1],output)
   links=[n.attrs.get('href','') for item in items for n in item.descendants('a')]
   self.assertEqual(len(links),9)
   self.assertEqual(sum('link.amazon/' in link for link in links),7)
   for link in links:self.assertIn(link,output)
   for section in sections:
    heading=next(section.descendants('h2'))
    self.assertIn('## '+normalise(plain(heading)),output)
