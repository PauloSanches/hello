"""Check that equipment images and links survive the setup's Markdown export."""
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from agent_content import build_detail_document,Document,Markdown,BASE
class SetupTests(unittest.TestCase):
 def test_table_keeps_headers_images_and_product_links(self):
  doc=Document('<table><thead><tr><th>Photo</th><th>Item</th></tr></thead><tbody><tr><td><img src="assets/test.webp" alt="Keyboard"></td><td><a href="https://example.com/item">MX Keys</a></td></tr></tbody></table>')
  output=Markdown(BASE).render(next(doc.root.descendants('table')))
  self.assertIn('| Photo | Item |',output)
  self.assertIn('| --- | --- |',output)
  self.assertIn('![Keyboard]('+BASE+'assets/test.webp)',output)
  self.assertIn('[MX Keys](https://example.com/item)',output)
 def test_setup_exports_all_equipment_and_named_notes(self):
  for prefix in ['', 'pt','it']:
   folder=ROOT/prefix if prefix else ROOT
   main=Document((folder/'setup/my-setup/index.html').read_text())
   output=build_detail_document(ROOT,prefix,'my-setup','setup')
   table=next(main.root.descendants('table'))
   images=list(table.descendants('img'))
   self.assertEqual(len(images),8)
   for image in images:
    self.assertIn('assets/'+image.attrs['src'].split('assets/',1)[1],output)
    self.assertIn('### '+image.attrs['alt'],output)
   links=[n.attrs.get('href','') for n in main.root.descendants('a') if 'link.amazon/' in n.attrs.get('href','')]
   self.assertEqual(len(links),7)
   for link in links:self.assertIn(link,output)
   self.assertIn('| --- | --- | --- |',output)
