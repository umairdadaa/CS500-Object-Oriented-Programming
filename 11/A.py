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

# Concrete Html class
class Html(Node):
    def get_tag(self) -> str:
        return "html"

# Concrete Head class
class Head(Node):
    def get_tag(self) -> str:
        return "head"

# Concrete Title class
class Title(Node):
    def get_tag(self) -> str:
        return "title"

# Concrete Body class
class Body(Node):
    def get_tag(self) -> str:
        return "body"

# Concrete Div class
class Div(Node):
    def get_tag(self) -> str:
        return "div"

# Concrete B class
class B(Node):
    def get_tag(self) -> str:
        return "b"

# Main function
def main():
    # Create Div elements with attributes
    divAtts = {'id': 'first', 'class': 'foo'}
    divA = Div('This is a test A', divAtts)
    
    divAtts = {'id': 'second', 'class': 'bar'}
    divB = Div('This is a test B', divAtts)
    
    divAtts = {'id': 'third', 'class': 'dump'}
    divC = Div('This is a test C', divAtts)
    
    # Create B element and append to divC
    b = B('This is a simple HTML file')
    divC.appendChild(b)
    
    # Create Body and append Div elements
    body = Body()
    body.appendChild(divA)
    body.appendChild(divB)
    body.appendChild(divC)
    
    # Create Head and Title
    title = Title('Example')
    head = Head()
    head.appendChild(title)
    
    # Create Html element with lang attribute
    htmlAtts = {'lang': 'en'}
    html = Html('', htmlAtts)
    html.appendChild(head)
    html.appendChild(body)
    
    # Print the complete HTML
    print(f"<!DOCTYPE html>{html.html()}")

if __name__ == "__main__":
    main()
