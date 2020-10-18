#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    #tag here allows the test script to test the framework without extending it
    tag = "html"
    
    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)        

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write(f"<{self.tag}>")
        for line in self.content:
            try:
                line.render(out_file)
            except AttributeError:
                out_file.write(line)
        out_file.write(f"</{self.tag}>")

class OneLineTag(Element):
    """Renders a simple tag, content replaced by a string"""
    def __init__(self, content = ""):
        self.content = content
        
    def render(self, out_file):
        out_file.write(f"<{self.tag}> {self.content} </{self.tag}>")
        
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