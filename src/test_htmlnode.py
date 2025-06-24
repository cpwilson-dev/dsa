
import unittest
from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()

