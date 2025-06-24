
from textnode import TextNode, TextType


def main():
    node = TextNode("hello",TextType.LINK, "http://google.com")
    print(node)

main()
