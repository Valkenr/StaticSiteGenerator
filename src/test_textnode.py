import unittest

from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
        text_type_link,
        text_type_image,
      
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_false_text(self):
        node = TextNode("Tacos are good", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    
    def test_eq_type_type_variance(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)
    
    def test_eq_false_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_eq_w_url(self):
        node = TextNode("This is a text node", "bold", "https://www.funtimez.gg")
        node2 = TextNode("This is a text node", "bold", "https://www.funtimez.gg")
        self.assertEqual(node, node2)
    
    def test_eq_false_text_w_url(self):
        node = TextNode("This is a text node", "bold", "https://www.funtimez.gg")
        node2 = TextNode("This is a sext node", "bold", "https://www.funtimez.gg")
        self.assertNotEqual(node, node2)
    
    def test_eq_false_url(self):
        node = TextNode("This is a text node", "bold", "https://www.funtimez.gg")
        node2 = TextNode("This is a text node", "italic", "https://www.funtimez.god")
        self.assertNotEqual(node, node2)

    def test_eq_false_url(self):
        node = TextNode("This is a text node", "bold", "https://www.funtimez.gg")
        self.assertEqual("TextNode(This is a text node, bold, https://www.funtimez.gg)", repr(node))

if __name__ == "__main__":
    unittest.main()
