import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from htmlnode import *
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a html node")
        node2 = HTMLNode("p", "This is a html node")
        self.assertEqual(node, node2)
        node3 = HTMLNode("p", "This is a html node", None, None)
        self.assertEqual(node, node3)
        node4 = HTMLNode("p", "This is a html node", [node2])
        node5 = HTMLNode("p", "This is a html node", [node2])
        self.assertEqual(node4, node5)
        node6 = HTMLNode("p", "This is a html node", None, {"href": "https://www.google.com", "jotain" : "www.jotain.com"})
        props = node6.props_to_html()
        #print(props)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_not_eq(self):
        node = HTMLNode(("p", "This is a html node"))
        node2 = HTMLNode(("h1", "This is a html node"))
        self.assertNotEqual(node, node2)
        node3 = HTMLNode(("p", "This is a different html node"))
        self.assertNotEqual(node, node3)
        node4 = HTMLNode(("p", "This is a html node", [node, node2], None))
        node5 = HTMLNode(("p", "This is a html node", [node, node3], None))
        self.assertNotEqual(node4, node5)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        #print(parent_node.to_html())

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        #print(parent_node.to_html())





if __name__ == "__main__":
    unittest.main()