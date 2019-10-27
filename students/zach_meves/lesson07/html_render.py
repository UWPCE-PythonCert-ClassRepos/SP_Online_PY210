#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

from typing import Union


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content: str = None):
        self.content = [content] if content else []

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        # out_file.write("just something as a place holder...")
        out_file.write(f"<{self.tag}>\n")
        for elem in self.content:
            if isinstance(elem, str):
                out_file.write(f"{elem}\n")
            else:
                elem.render(out_file)
        out_file.write(f"</{self.tag}>\n")


class Html(Element):
    pass


class Body(Element):

    tag = "body"


class P(Element):

    tag = "p"


class Head(Element):

    tag = "head"


class OneLineTag(Element):

    def render(self, out_file):
        out_file.write(f"<{self.tag}> ")
        for elem in self.content:
            if isinstance(elem, str):
                out_file.write(f"{elem} ")
            else:
                elem.render(out_file)
        out_file.write(f"</{self.tag}>\n")


class Title(OneLineTag):

    tag = "title"
