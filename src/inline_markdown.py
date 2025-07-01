from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        if delimiter not in node.text or node.text.count(delimiter) < 2:
            new_nodes.append(node)
            continue
        text_list = node.text.split(delimiter)
        if len(text_list) < 3 or (len(text_list) % 2) == 0:
            raise ValueError("Invalid Markdown syntax. Matching delimiter not found")
        for i in range(len(text_list)):
            if i % 2 == 0:
                if text_list[i] != "":
                    new_node = TextNode(f"{text_list[i]}", TextType.TEXT)
                    new_nodes.append(new_node)
            else:
                new_node = TextNode(text_list[i], text_type)
                new_nodes.append(new_node)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes(old_nodes, extract_type, extract_text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if old_node is None:
            continue
        image_extract = extract_type(old_node.text)
        if len(image_extract) == 0:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        sections = []
        for i in range(len(image_extract)):
            first_extract = image_extract[i][0]
            second_extract = image_extract[i][1]
            if len(image_extract[i][0]) == 0 or len(image_extract[i][1]) == 0:
                continue
            match extract_text_type:
                case TextType.IMAGE:
                    sections = text.split(f"![{first_extract}]({second_extract})", 1)
                case TextType.LINK:
                    sections = text.split(f"[{first_extract}]({second_extract})", 1)
            if len(sections) > 1 and sections[1] != "":
                text = sections[1]
            new_node = TextNode(f"{sections[0]}", TextType.TEXT)
            if len(sections[0]) != 0:
                new_nodes.append(new_node)
            new_extract_node = TextNode(f"{first_extract}", extract_text_type, f"{second_extract}")
            new_nodes.append(new_extract_node)
        if len(sections) > 1:
            if len(sections[1]) != 0:
                new_node = TextNode(f"{sections[1]}", TextType.TEXT)
                new_nodes.append(new_node)
    return new_nodes
    
def split_nodes_image(old_nodes):
    return split_nodes(old_nodes, extract_markdown_images, TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_nodes(old_nodes, extract_markdown_links, TextType.LINK)

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    new_textnodes = []
    new_textnodes.append(text_node)
    new_textnodes = split_nodes_delimiter(new_textnodes, "**", TextType.BOLD)
    new_textnodes = split_nodes_delimiter(new_textnodes, "_", TextType.ITALIC)
    new_textnodes = split_nodes_delimiter(new_textnodes, "`", TextType.CODE)
    new_textnodes = split_nodes_image(new_textnodes)
    new_textnodes = split_nodes_link(new_textnodes)
    return new_textnodes


    

