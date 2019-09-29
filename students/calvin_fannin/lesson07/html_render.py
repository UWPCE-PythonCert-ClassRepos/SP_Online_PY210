#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag))
        for content in self.content:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class Title(Element):
    tag = "title"

class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        for content in self.content:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write("</{}>".format(self.tag))

class title(OneLineTag):
    tag = "title"

