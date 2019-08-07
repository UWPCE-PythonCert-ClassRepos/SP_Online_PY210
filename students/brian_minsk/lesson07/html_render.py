#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag_name = "html"

    def __init__(self, content=None):
        self.content = []
        if content:
            self.append(content)        

    def append(self, new_content):
        if hasattr(new_content, 'render'):
            self.content.append(new_content)
        else:
            self.content.append(TextWrapper(str(new_content)))

    def render(self, out_file):
        opening_tag = self.create_opening_tag(self.tag_name)
        closing_tag = self.create_closing_tag(self.tag_name)
        out_file.write(opening_tag)
        for item in self.content:
            item.render(out_file)
        out_file.write(closing_tag)

    def create_opening_tag(self, tag_name):
        return "".join(["<", tag_name, ">"]) + "\n"

    def create_closing_tag(self, tag_name):
        return "".join(["</", tag_name, ">"]) + "\n"

class Html(Element):
    tag_name = "html"

class Body(Element):
    tag_name = "body"

class P(Element):
    tag_name = "p"

class TextWrapper():
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out):
        file_out.write(self.text + "\n")
