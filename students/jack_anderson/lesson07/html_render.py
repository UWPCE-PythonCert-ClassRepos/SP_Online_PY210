#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None):
        self.contents = [content]


    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write(f"<{self.tag}>\n")
        for content in self.contents:
            if content is not None:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(f"</{self.tag}>\n")

class Body(Element):
    tag = 'body'

class Html(Element):
    tag = 'html'

class P(Element):
    tag = 'p'
