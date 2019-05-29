#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None):
        self.content = [content]

        # prevent empty elements from being created with type None
        if None in self.content:
            self.content = []
        
    def append(self, new_content):
        self.content.append(new_content)
        
    def render(self, out_file):
        out_file.write(f"<{self.tag}>\n")
        for content in self.content:
            out_file.write(content)
            out_file.write("\n")
        out_file.write(f"</{self.tag}>")

class Html(Element):

    def __init__(self, content=None):
        self.content = [content]

        # prevent empty elements from being created with type None
        if None in self.content:
            self.content = []
    
class Body(Element):

    tag = "body"

    def __init__(self, content=None):
        self.content = [content]

        # prevent empty elements from being created with type None
        if None in self.content:
            self.content = []

class P(Element):

    tag = "p"

    def __init__(self, content=None):
        self.content = [content]

        # prevent empty elements from being created with type None
        if None in self.content:
            self.content = []
  
class Head(Element):
    
    tag = "head"

    def __init__(self, content=None):
        self.content = [content]

        # prevent empty elements from being created with type None
        if None in self.content:
            self.content = []
  
