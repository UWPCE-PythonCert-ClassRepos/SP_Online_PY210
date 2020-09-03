#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        if new_content is not None:
            self.contents.append(new_content)

    def render(self, out_file):
        # Loop through list of contents, having tags on front and back
        out_file.write(f"<{self.tag}>\n")
        for content in self.contents:
            # out_file.write(content)
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(f"</{self.tag}>\n")


class Body(Element):

    tag = "body"

class P(Element):

    tag = "p"

class Html(Element):

    tag = "html"

class Head(Element):

    tag = "head"

class OneLineTag(Element):

    def render(self, out_file):
        out_file.write(f"<{self.tag}>")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(f"</{self.tag}>\n")

class Title(OneLineTag):

    tag = "title"

if __name__ == "__main__":
    pass