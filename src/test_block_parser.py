import unittest

from block_parser import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
    block_type_paragraph,
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

    def test_block_type_heading(self):
        block = "#### Weeeee!"
        block_type = block_to_block_type(block)
        # print(f"Heading? {block_type}")
        self.assertEqual(block_type_heading, block_to_block_type(block))

    def test_block_type_code(self):
        block = """```weeeee!"
uaaoeuaoe```"""
        block_type = block_to_block_type(block)
        # print(f"Code? {block_type}")
        self.assertEqual(block_type_code, block_to_block_type(block))

    def test_block_type_quote(self):
        block = """>Weeeee!
>Wooooo!"""
        block_type = block_to_block_type(block)
        # print(f"Quote? {block_type}")
        self.assertEqual(block_type_quote, block_to_block_type(block))

    def test_block_type_unordered_list(self):
        block = """- Wa
- Wa
- We
- Wa"""
        block_type = block_to_block_type(block)
        # print(f"Unordered List? {block_type}")
        self.assertEqual(block_type_unordered_list, block_to_block_type(block))

    def test_block_type_ordered_list(self):
        block = """1. Juan
2. Too
3. Tree"""
        block_type = block_to_block_type(block)
        # print(f"Ordered List? {block_type}")
        self.assertEqual(block_type_ordered_list, block_to_block_type(block))

    def test_block_type_ordered_list_false(self):
        block = """1.Juan
2.Too
5.Tree"""
        block_type = block_to_block_type(block)
        # print(f"Ordered List? {block_type}")
        self.assertNotEqual(block_type_ordered_list, block_to_block_type(block))

    def test_block_type_paragraph(self):
        block = "Oooga Booga Booga!"
        block_type = block_to_block_type(block)
        # print(f"Paragraph? {block_type}")
        self.assertEqual(block_type_paragraph, block_to_block_type(block))


if __name__ == "__main__":
    unittest.main()
