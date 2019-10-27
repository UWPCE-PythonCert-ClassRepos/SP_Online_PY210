#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

from typing import Union


# This is the framework for the base class
class Element(object):

    tag = "html"
    newline = "\n"

    def __init__(self, content: str = None, **kwargs):
        self.content = []
        if content:
            self.append(content)
        self.attr = dict(**kwargs)

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        # out_file.write("just something as a place holder...")
        out_file.write(self.start_tag() + self.newline)
        for elem in self.content:
            if isinstance(elem, str):
                out_file.write(f"{elem}{self.newline}")
            else:
                elem.render(out_file)
        out_file.write(self.close_tag() + "\n")

    def start_tag(self) -> str:
        return f"<{self.tag}{self.print_attr()}>"

    def close_tag(self) -> str:
        return f"</{self.tag}>"

    def print_attr(self) -> str:
        attr = ' '.join([f'{k}="{v}"' for k, v in self.attr.items()])
        if attr:
            return ' ' + attr
        else:
            return attr


class Html(Element):
    pass


class Body(Element):

    tag = "body"


class P(Element):

    tag = "p"


class Head(Element):

    tag = "head"


class OneLineTag(Element):

    newline = ""


class Title(OneLineTag):

    tag = "title"


class SelfClosingTag(Element):

    newline = ''

    def start_tag(self) -> str:
        return super().start_tag()[:-1]

    def close_tag(self) -> str:
        return "/>"

    def append(self, new_content):
        raise TypeError("Self closing tags cannot have any content")


class Hr(SelfClosingTag):

    tag = 'hr'


class Br(SelfClosingTag):

    tag = 'br'


