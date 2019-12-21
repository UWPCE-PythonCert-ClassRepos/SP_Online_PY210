#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

from typing import Union


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = '  '
    newline = "\n"

    def __init__(self, content: str = None, **kwargs):
        self.content = []

        if content:
            self.append(content)
        self.attr = dict(**kwargs)

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file, indentation: str = ""):

        out_file.write(indentation + self.start_tag() + self.newline)
        for elem in self.content:
            if isinstance(elem, str):
                out_file.write(f"{self.content_indent(indentation + self.indent)}{elem}{self.newline}")
            else:
                elem.render(out_file, indentation + self.indent)
        out_file.write(self.content_indent(indentation) + self.close_tag() + "\n")

    def content_indent(self, indentation: str):
        return indentation if self.newline == "\n" else ''

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

    def start_tag(self) -> str:
        return f"<!DOCTYPE html>\n{super().start_tag()}"


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

    def __init__(self, **kwargs):
        if 'content' in kwargs:
            raise TypeError("Self closing tags cannot have any content")
        super().__init__(**kwargs)

    def start_tag(self) -> str:
        return super().start_tag()[:-1]

    def close_tag(self) -> str:
        return " />"

    def append(self, new_content):
        raise TypeError("Self closing tags cannot have any content")


class Hr(SelfClosingTag):

    tag = 'hr'


class Br(SelfClosingTag):

    tag = 'br'


class A(OneLineTag):

    tag = 'a'

    def __init__(self, link, content):
        super().__init__(content, href=link)


class Ul(Element):

    tag = 'ul'

    def __init__(self, content=None, **kwargs):
        """Content must be a str, :py:class:`Li` or sequence of str or Li"""
        super().__init__(None, **kwargs)

        if content:
            if type(content) in (str, Li):
                self.append(content)
            else:  # Try to add each Li
                try:
                    for elem in content:
                        self.append(elem)
                except TypeError:  # Not an iterable content
                    raise TypeError("Provided content must be a string, Li, or sequence of "
                                    "these types.")

    def append(self, new_content):
        if isinstance(new_content, str):
            new_content = Li(new_content)
        elif not isinstance(new_content, Li):
            raise TypeError("Only objects of type str or Li can be added to a Ul")
        super().append(new_content)


class Li(Element):

    tag = "li"


class H(OneLineTag):

    def __init__(self, level: int, content: str = None, **kwargs):
        self.tag = f"h{level}"

        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):

    tag = 'meta'

