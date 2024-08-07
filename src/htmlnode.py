

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method aren't implementated")

    def props_to_html(self):
        if self.props is None:
            return ""
        prop_line = ""
        for key in self.props:
            prop_line += f" {key}=\"{self.props[key]}\""
        return prop_line

    def __repr__(self):
        return (
                f"HTMLNode:({self.tag}, {self.value}, "
                f"children: {self.children}, {self.props})"
               )

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("I need value!!!")
        if self.tag is None:
            return self.value
        else:
            # print(f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")
            return (
                f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
                )

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid Value: No Input")
        if self.children is None:
            raise ValueError("Invalid Children: No Input!")
        childs = ""
        for child in self.children:
            childs += child.to_html()
        # print(f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")
        return f"<{self.tag}{self.props_to_html()}>{childs}</{self.tag}>"

    def __repr__(self):
        return (
            f"ParentNode({self.tag}, children: {self.children}, {self.props})"
            )
