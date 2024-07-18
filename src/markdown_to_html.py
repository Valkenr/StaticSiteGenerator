
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
    text_node_to_html_node,
)

from htmlnode import HTMLNode, LeafNode, ParentNode

def markdown_to_html_node(markdown):
    nodes = []
    markdown_text_blocks = markdown_to_blocks(markdown)
    # print(f"mtb: {markdown_text_blocks}")
    for markdown_text_block in markdown_text_blocks:
        block_type = block_to_block_type(markdown_text_block)
        # print(f"Found a {block_type}!")
        if block_type == block_type_heading:
            nodes.append(generate_heading_node(markdown_text_block))
        if block_type == block_type_code:
            nodes.append(generate_code_node(markdown_text_block))
        if block_type == block_type_quote:
            nodes.append(generate_quote_node(markdown_text_block))
        if block_type == block_type_unordered_list:
            nodes.append(generate_ul_node(markdown_text_block))
        if block_type == block_type_ordered_list:
            nodes.append(generate_ol_node(markdown_text_block))
        if block_type == block_type_paragraph:
            nodes.append(generate_paragraph_node(markdown_text_block))

    return ParentNode("div", nodes)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    leaf_nodes = []
    for text_node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(text_node))
    return leaf_nodes

def generate_heading_node(text):
    # print("Generating heading node...")
    heading_level = 0
    for i in range(8):
        if text[i] == "#":
            heading_level += 1
        if text[i] == " ":
            continue
    child_nodes = text_to_children(text[(heading_level + 1):])
    html_node = ParentNode(f"h{heading_level}", child_nodes)
    return html_node

def generate_code_node(text):
    # print("Generating code node...")
    code_node = TextNode(text[3:len(text)-3], text_type_code)
    html_node = text_node_to_html_node(code_node)
    return  html_node

def generate_quote_node(text):
    # print("Generating quote node...")
    split_quote = text.split("\n")
    quote_text = ""
    for line in split_quote:
        quote_text += f"{line[1:].strip()}\n"
    quote_nodes = text_to_children(quote_text.rstrip("\n"))
    html_node = ParentNode("blockquote", quote_nodes)
    return html_node

def generate_ul_node(text):
    # print("Generating ulist node...")
    split_list = text.split("\n")
    list_nodes = []
    for line in split_list:
        list_nodes.append(ParentNode("li", text_to_children(line[2:])))
    html_node = ParentNode("ul", list_nodes)
    return html_node

def generate_ol_node(text):
    # print("Generating olist node...")
    split_list = text.split("\n")
    list_nodes = []
    for line in split_list:
        list_nodes.append(ParentNode("li", text_to_children(line[3:])))
    html_node = ParentNode("ol", list_nodes)
    return html_node

def generate_paragraph_node(text):
    # print("Generating paragraph node...")
    return ParentNode("p", text_to_children(text))

