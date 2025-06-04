def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        new_block = block.strip()
        filtered_blocks.append(new_block)
    return filtered_blocks