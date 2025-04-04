from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
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
