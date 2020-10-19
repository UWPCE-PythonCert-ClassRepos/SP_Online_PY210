#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    #tag here allows the test script to test the framework without extending it
    tag = "html"
    
    def __init__(self, content=None, **kwargs):
        """
        initializes an element that can be rendered into html
        class is a keyword in both python and html
        pass clas into kwargs for a html class
        """
        self.content = []
        if content:
            self.content.append(content)
        if "clas" in kwargs: 
            kwargs["class"] = kwargs.pop("clas")
        self.attrs = [(key, value) for key, value in kwargs.items()]

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write(f"<{self.tag}")
        self.render_attr(out_file);
        out_file.write(">\n")
        for line in self.content:
            try:
                line.render(out_file)
            except AttributeError:
                out_file.write(f"{line}\n")
        out_file.write(f"</{self.tag}>\n")
    
    def render_attr(self, out_file):
        for key, value in self.attrs:
            out_file.write(f' {key}="{value}"')

class OneLineTag(Element):
    """Renders a simple tag"""
        
    def render(self, out_file):
        out_file.write(f"<{self.tag}")
        self.render_attr(out_file)
        out_file.write(f"> {self.content[0]} </{self.tag}>")
        
class Html(Element):
    tag = "html"

class Head(Element):
    tag = "head"

class Title(OneLineTag):
    tag = "title"
    
class Body(Element):
    tag = "body"
    
class P(Element):
    tag = "p"