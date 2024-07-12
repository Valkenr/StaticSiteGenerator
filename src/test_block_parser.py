import unittest

from block_parser import (
    markdown_to_blocks,
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

    def test_1(self):
        text = (
            "# This is a heading\n"
                "\n"
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"
                "\n"
                "* This is the first list item in a list block\n"
                "* This is a list item\n"
                "* This is another list item"
        )
        self.assertEqual(
            markdown_to_blocks(text),
            [
                '# This is a heading',
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
                '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ],
        )

    def test_2(self):
        text = """
# This is a heading







This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        self.assertEqual(
            markdown_to_blocks(text),
            [
                '# This is a heading',
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
                '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ],
        )


if __name__ == "__main__":
    unittest.main()
