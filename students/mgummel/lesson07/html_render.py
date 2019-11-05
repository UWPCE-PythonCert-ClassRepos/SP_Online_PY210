#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = 2

    def __init__(self, content=None, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                self.tag += f' {key}="{value}"'

        if content:
            self.content = [content]
        else:
            self.content = list()


    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write(f'<{self.tag}>\n')
        for elements in self.content:
            try:
                elements.render(out_file)
            except AttributeError:
                out_file.write(f'{elements}\n')
        out_file.write(f'</{self.tag}>\n')
                

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, out_file):
        out_file.write(f'<{self.tag}>{self.content[0]}</{self.tag}>\n')


    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"

