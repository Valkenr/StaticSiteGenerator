import unittest

from inline_parser import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)

from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
)


class TestInlineParser(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(
                [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("bold", text_type_bold),
                    TextNode(" word", text_type_text),
                ],
                new_nodes,
            )

    def test_delim_italic(self):
        node = TextNode("This is text with a *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(
                [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("italic", text_type_italic),
                    TextNode(" word", text_type_text),
                ],
                new_nodes,
            )

    def test_delim_code(self):
        node = TextNode("This is text with a `code` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
                [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("code", text_type_code),
                    TextNode(" word", text_type_text),
                ],
                new_nodes,
            )

    def test_delim_double_bold(self):
        node = TextNode(
                "**Bold** hua! what is it **GOOD FOR**",
                text_type_text
                )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(
                [
                    TextNode("Bold", text_type_bold),
                    TextNode(" hua! what is it ", text_type_text),
                    TextNode("GOOD FOR", text_type_bold),
                ],
                new_nodes,
            )

    def test_image_1(self):
        extraction = extract_markdown_images(
            "This is text with an ![image](https://www.wee.com/Z.png) and"
            "![another](https://rage.goo.com/d.png)"
        )
        self.assertEqual(
            [
            ("image", "https://www.wee.com/Z.png"),
            ("another", "https://rage.goo.com/d.png"),
            ],
            extraction,
        )

    def test_image_2(self):
        extraction = extract_markdown_images(
            "This is text with a ![link](https://www.wee.com/Z.png) and"
            "![another](https://rage.goo.com/d.png)"
        )
        self.assertEqual(
            [
            ("link", "https://www.wee.com/Z.png"),
            ("another", "https://rage.goo.com/d.png"),
            ],
            extraction,
        )


if __name__ == "__main__":
    unittest.main()
