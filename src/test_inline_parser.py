import unittest

from inline_parser import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
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
        extraction = extract_markdown_links(
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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://www.wee.com/Z.png) and"
                "![another](https://rage.goo.com/d.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://www.wee.com/Z.png"),
                TextNode(" and", text_type_text),
                TextNode(
                    "another", text_type_image, "https://rage.goo.com/d.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "Yis ys yext yith yn [link](https://yyy.yee.yom/Z.yeeng) yand"
                "[yanother](https://yage.yoo.yom/d.yeeng)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("Yis ys yext yith yn ", text_type_text),
                TextNode("link", text_type_link, "https://yyy.yee.yom/Z.yeeng"),
                TextNode(" yand", text_type_text),
                TextNode(
                    "yanother", text_type_link, "https://yage.yoo.yom/d.yeeng"
                ),
            ],
            new_nodes,
        )

    def test_it_all(self):
        new_nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block`"
                " and an ![image](https://wee.image.com/Z.png)"
                " and a [link](https://groot.dev)"
        )
        self.assertEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://wee.image.com/Z.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://groot.dev"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
