#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    #tag here allows the test script to test the framework without extending it
    tag = "html"
    indent = "    "
    
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

    def render(self, out_file, ind=""):
        self.open_tag(out_file, ind)
        out_file.write(">\n")
        for line in self.content:
            try:
                line.render(out_file, ind+self.indent)
            except AttributeError:
                out_file.write(f"{ind}{self.indent}{line}\n")
        out_file.write(f"{ind}</{self.tag}>\n")
    
    def open_tag(self, out_file, ind):
        out_file.write(f"{ind}<{self.tag}")
        self.render_attr(out_file);
    
    def render_attr(self, out_file):
        for key, value in self.attrs:
            out_file.write(f' {key}="{value}"')

class OneLineTag(Element):
    """Renders a simple tag, content must be stringable"""
    
    def append(self, new_content):
        raise TypeError("OneLineTags only take one line of text")
        
    def render(self, out_file, ind=""):
        self.open_tag(out_file, ind)
        out_file.write(f"> {self.content[0]} </{self.tag}>\n")

class SelfClosingTag(Element):
    """Renders a self closing tag, ie: <hr/>, <br/>"""
    
    def __init__(self, content = None, *args, **kwargs):
        if content:
            raise TypeError("SelfClosingTags cannot hold content")
        super().__init__(*args, **kwargs)
    
    def append(self, new_content):
        raise TypeError("SelfClosingTags cannot hold content")
    
    def render(self, out_file, ind=""):
        self.open_tag(out_file, ind)
        out_file.write(" />\n")
        
class Html(Element):
    tag = "html"
    
    def render(self, out_file, ind="", *args, **kwargs):
        out_file.write(f"{ind}<!DOCTYPE html>\n")
        super().render(out_file, ind, *args, **kwargs)

class Head(Element):
    tag = "head"

class Title(OneLineTag):
    tag = "title"

class Meta(SelfClosingTag):
    tag = "meta"
    
class Body(Element):
    tag = "body"
    
class P(Element):
    tag = "p"

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"
    
    def __init__(self, link, *args, **kwargs):
        super().__init__(*args, href = link, **kwargs)

class Ul(Element):
    tag = "ul"

class Li(Element):
   tag = "li"

class H(OneLineTag):
    def __init__(self, level, *args, **kwargs):
        self.tag = f"h{level}"
        super().__init__(*args, **kwargs)
