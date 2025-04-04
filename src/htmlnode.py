class HTMLNode():
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html():
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html = ""
        for key in self.props:
            html = html + f' {key}="{self.props[key]}"'
        return html
    
    def __eq__(self, other):
        return ( self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props
        )
    
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"
        
    
    

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag value puuttuu")
        if self.children is None or len(self.children) == 0:
            raise ValueError("children value None tai Tyhjä")
        html = f"<{self.tag}>"
        for child in self.children:
            html = html + child.to_html()
        html = html + f"</{self.tag}>"
        return html
        