import unittest
from markdown_blocks import markdown_to_blocks , BlockType , block_to_block_type


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):

        heading_block = "### Porotarha"
        block = block_to_block_type(heading_block)
        self.assertEqual(block, BlockType.HEADING)

        code_block = "```coodi moodi roodi```"
        block = block_to_block_type(code_block)
        self.assertEqual(block, BlockType.CODE)

        quote_block = """>lollero
>pollero
>pox"""
        block = block_to_block_type(quote_block)
        self.assertEqual(block, BlockType.QUOTE)

        unordered_list_block = """-tämä
-on
-järjestämätön
-lista"""

        block = block_to_block_type(unordered_list_block)
        self.assertEqual(block, BlockType.UNORDERED_LIST)

        ordered_list = """1. ensimmäinen
2. toinen
3. kolmas"""
        block = block_to_block_type(ordered_list)
        self.assertEqual(block, BlockType.ORDERED_LIST)

        


if __name__ == "__main__":
    unittest.main()
