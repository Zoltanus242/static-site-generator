from htmlnode import LeafNode, HTMLNode
from enum import Enum



class TextType(Enum):
    TEXT = "Normal text"
    BOLD = "Bold text"
    ITALIC = "Italic text"
    CODE = "Code text"
    LINK = "Link text"
    IMAGE = "Image text"
    
class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return ( self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
        )
    
    def __repr__(self):
         return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    
def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case (TextType.TEXT):
            return LeafNode(None, text_node.text)
        case (TextType.BOLD):
            return LeafNode("b", text_node.text)
        case (TextType.ITALIC):
            return LeafNode("i", text_node.text)
        case (TextType.CODE):
            return LeafNode("code", text_node.text)
        case (TextType.LINK):
            return LeafNode("a", text_node.text, "href")
        case (TextType.IMAGE):
            return LeafNode("img", "", {"src" : text_node.url , "alt" : ""})
        case _:
            raise Exception(f"invalid text type: {text_node.text_type}")
            
def text_to_textnodes(text):
    from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link
    text_node = TextNode(text, TextType.TEXT)
    new_textnodes = []
    new_textnodes.append(text_node)
    print(new_textnodes)
    new_textnodes = split_nodes_delimiter(new_textnodes, "**", TextType.BOLD)
    print(new_textnodes)
    new_textnodes = split_nodes_delimiter(new_textnodes, "_", TextType.ITALIC)
    print(new_textnodes)
    new_textnodes = split_nodes_delimiter(new_textnodes, "`", TextType.CODE)
    print(new_textnodes)
    new_textnodes = split_nodes_image(new_textnodes)
    print(new_textnodes)
    new_textnodes = split_nodes_link(new_textnodes)
    print(new_textnodes)

    return new_textnodes