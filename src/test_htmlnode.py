
import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_values(self):
        node = HTMLNode("div","I wish I could read")

        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


    def test_to_html_props(self):
        node = HTMLNode("a","hello world",None,{"href":"https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

    def test_repr(self):
        node = HTMLNode("a","hello world",None,{"href":"https://google.com"})
        self.assertEqual(node.__repr__(),"HTMLNode(tag=a, value=hello world, children=None, props={'href': 'https://google.com'}")

    def test_leaf_to_html_p(self):
        node = LeafNode("p","Hello, world!")
        self.assertEqual(node.to_html(),"<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a","Hello, world!",{"href":"https://google.com"})
        self.assertEqual(node.to_html(),'<a href="https://google.com">Hello, world!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()

