from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph block"
    HEADING = "heading block"
    CODE = "code block"
    QUOTE = "quote block"
    UNORDERED_LIST = "unodered list block"
    ORDERED_LIST = "ordered list block"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        new_block = block.strip()
        filtered_blocks.append(new_block)
    return filtered_blocks

def block_to_block_type(block):
    match block[0]:
        case '#':
            if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
                return BlockType.HEADING
        case "`":
            if block[:3] == "```" and block[-3:] == "```":
                return BlockType.CODE
        case '>':
            lines = block.splitlines()
            for line in lines:
                if line[0] != '>':
                    return BlockType.PARAGRAPH
            return BlockType.QUOTE
        case '-':
            lines = block.splitlines()
            for line in lines:
                if line[0] != '-':
                    print(line)
                    return BlockType.PARAGRAPH
            return BlockType.UNORDERED_LIST
        case '1':
            lines = block.splitlines()
            order_number = 1
            for line in lines:
                if line[0] != str(order_number) or line[1:3] != ". ":
                    return BlockType.PARAGRAPH
                order_number += 1
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

