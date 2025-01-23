from abc import ABC, abstractmethod

# Base class Node
class Node(ABC):
    def __init__(self, content: str = '', attributes: dict = None) -> None:
        self._content = content
        self._attributes = attributes if attributes else {}
        self._children = []

    @property
    def content(self) -> str:
        return self._content

    @property
    def attributes(self) -> dict:
        return self._attributes

    @property
    def children(self):
        return self._children

    def appendChild(self, child) -> None:
        self._children.append(child)

    @abstractmethod
    def get_tag(self) -> str:
        pass

    def html(self) -> str:
        tag = self.get_tag()
        output = f"<{tag}"

        # Add attributes
        for k, v in self.attributes.items():
            output += f' {k}="{v}"'
        output += ">"

        # Add content
        output += self.content

        # Add children
        for child in self.children:
            output += child.html()

        output += f"</{tag}>"
        return output

# Concrete node classes
class Html(Node):
    def get_tag(self) -> str:
        return "html"

class Head(Node):
    def get_tag(self) -> str:
        return "head"

class Title(Node):
    def get_tag(self) -> str:
        return "title"

class Body(Node):
    def get_tag(self) -> str:
        return "body"

class Div(Node):
    def get_tag(self) -> str:
        return "div"

class B(Node):
    def get_tag(self) -> str:
        return "b"

# Abstract Factory
class AbstractNodeFactory(ABC):
    @abstractmethod
    def makeNode(self, tag: str, content: str = '', attributes: dict = None):
        pass

# Standard Factory
class StandardNodeFactory(AbstractNodeFactory):
    def makeNode(self, tag: str, content: str = '', attributes: dict = None):
        if tag == 'html':
            return Html(content, attributes)
        elif tag == 'head':
            return Head(content, attributes)
        elif tag == 'title':
            return Title(content, attributes)
        elif tag == 'body':
            return Body(content, attributes)
        elif tag == 'div':
            return Div(content, attributes)
        elif tag == 'b':
            return B(content, attributes)
        else:
            raise ValueError("Unknown tag")

# Main function using the factory
def main():
    factory = StandardNodeFactory()
    
    # Create Div elements with attributes
    divAtts = {'id': 'first', 'class': 'foo'}
    divA = factory.makeNode('div', 'This is a test A', divAtts)
    
    divAtts = {'id': 'second', 'class': 'bar'}
    divB = factory.makeNode('div', 'This is a test B', divAtts)
    
    divAtts = {'id': 'third', 'class': 'dump'}
    divC = factory.makeNode('div', 'This is a test C', divAtts)
    
    # Create B element and append to divC
    b = factory.makeNode('b', 'This is a simple HTML file')
    divC.appendChild(b)
    
    # Create Body and append Div elements
    body = factory.makeNode('body')
    body.appendChild(divA)
    body.appendChild(divB)
    body.appendChild(divC)
    
    # Create Head and Title
    title = factory.makeNode('title', 'Example')
    head = factory.makeNode('head')
    head.appendChild(title)
    
    # Create Html element with lang attribute
    htmlAtts = {'lang': 'en'}
    html = factory.makeNode('html', '', htmlAtts)
    html.appendChild(head)
    html.appendChild(body)
    
    # Print the complete HTML
    print(f"<!DOCTYPE html>{html.html()}")

if __name__ == "__main__":
    main()
