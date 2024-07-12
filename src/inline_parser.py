import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #print(f"\n! {old_nodes}")
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        split_node = old_node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise ValueError("Invalid Markdown, unclosed section")
        for i in range(len(split_node)):
            if split_node[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_node[i], text_type_text))
            else:
                split_nodes.append(TextNode(split_node[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    #print(f"\n! {old_nodes}")
    new_nodes = []
    for old_node in old_nodes:
        ##print(f"Noo! {old_node}")
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        extracted = extract_markdown_images(node_text)
        if len(extracted) == 0:
            new_nodes.append(old_node)
            continue
        #print(f"extracted: {extracted}")
        for extract in extracted:
            #print(f"node_text: {node_text}")
            desc = extract[0]
            addr = extract[1]
            split_text = node_text.split(f"![{desc}]({addr})", 1)
            #print(f"split_text: {split_text}")
            if len(split_text) != 2:
                raise ValueError("Invalid markdown! image not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            node_text = split_text[1]
            new_nodes.append(TextNode(desc, text_type_image, addr))
            #print(f"new_nodes: {new_nodes}")
        if node_text != "":
            new_nodes.append(TextNode(node_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    #print(f"\n! {old_nodes}")
    new_nodes = []
    for old_node in old_nodes:
        ##print(f"Noo! {old_node}")
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        extracted = extract_markdown_links(node_text)
        if len(extracted) == 0:
            new_nodes.append(old_node)
            continue
        #print(f"extracted: {extracted}")
        for extract in extracted:
            #print(f"node_text: {node_text}")
            desc = extract[0]
            addr = extract[1]
            split_text = node_text.split(f"[{desc}]({addr})", 1)
            #print(f"split_text: {split_text}")
            if len(split_text) != 2:
                raise ValueError("Invalid markdown! link not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            node_text = split_text[1]
            new_nodes.append(TextNode(desc, text_type_link, addr))
            #print(f"new_nodes: {new_nodes}")
        if node_text != "":
            new_nodes.append(TextNode(node_text, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    return split_nodes_delimiter(
        split_nodes_delimiter(
            split_nodes_delimiter(
                split_nodes_link(
                    split_nodes_image(
                        [TextNode(text, text_type_text)]
                    )
                ), "**", text_type_bold
            ), "*", text_type_italic
        ), "`", text_type_code
    )

