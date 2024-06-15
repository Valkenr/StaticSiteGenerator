from textnode import TextNode

def main():

    new_node = TextNode()
    new_node.text = "This is a text node"
    new_node.text_type = "bold"
    new_node.url = "https://www.bootdev.com"
    print(new_node.__repr__())
main()






