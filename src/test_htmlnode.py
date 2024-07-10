import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        node = HTMLNode(
                "p",
                "Test Node",
                None,
                {"href": "https://www.test.com", "target": "_target"}
                )
        self.assertEqual(
                node.props_to_html(),
                " href=\"https://www.test.com\" target=\"_target\""
                )

    def test_none(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_LeafNode_1(self):
        node = LeafNode("a", "Test Node", {"href": "https://www.test.com"})
        self.assertEqual(
                node.to_html(),
                "<a href=\"https://www.test.com\">Test Node</a>"
                )

    def test_LeafNode_2(self):
        node = LeafNode("p", "Test Node")
        self.assertEqual(node.to_html(), "<p>Test Node</p>")

    def test_parent_node_1(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
                node.to_html(),
                (
                    "<p><b>Bold text</b>Normal text"
                    "<i>Italic text</i>Normal text</p>"
                )
            )

    def test_parent_node2(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("i", "Italic text"),
                        LeafNode("b", "Bold text"),
                    ],
                ),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
                node.to_html(),
                (
                    "<p><b>Bold text</b>Normal text<p><i>Italic text</i>"
                    "<b>Bold text</b></p>Normal text</p>"
                )
            )


if __name__ == "__main__":
    unittest.main()
