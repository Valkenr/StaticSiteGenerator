block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        stripped_blocks.append(block.strip())
    return stripped_blocks

def is_heading(block):
    heading_check = False
    for i in range(7):
        if block[i] == "#":
            heading_check = True
            continue
        if block[i] == " " and heading_check == True:
            return True
        return False

def is_code(block):
    # print(f"Code Test: {block[:3]}|{block[len(block) - 3:]}")
    if block[:3] == "```" and block[len(block) - 3:] == "```":
        return True

def is_quote(block):
    lines = block.split("\n")
    for line in lines:
        if line[:1] == ">":
            continue
        return False
    return True

def is_unordered_list(block):
    lines = block.split("\n")
    for line in lines:
        # print(f"Line: {line[:2]}")
        if line[:2] == "* " or line[:2] == "- ":
            continue
        return False
    return True

def is_ordered_list(block):
    lines = block.split("\n")
    for i in range(len(lines)):
        if lines[i][:2] == f"{i + 1}.":
            continue
        return False
    return True

def block_to_block_type(block):
    if is_heading(block) == True:
        return block_type_heading
    if is_code(block) == True:
        return block_type_code
    if is_quote(block) == True:
        return block_type_quote
    if is_unordered_list(block) == True:
        return block_type_unordered_list
    if is_ordered_list(block) == True:
        return block_type_ordered_list
    return block_type_paragraph

