from block_parser import (
    markdown_to_blocks,
)

from markdown_to_html import markdown_to_html_node
from htmlnode import (HTMLNode, ParentNode, LeafNode)

title = ""

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No Title!")


def file_to_text(file_path):
    file = open(file_path)
    text = file.read()
    # print(f"File Text: {text}")
    return text
