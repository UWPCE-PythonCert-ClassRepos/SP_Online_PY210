#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'

    def __init__(self, content=None):
        """
        Initialize each instance of element.
        """
        if content:
            self.content_list = [content]
        else:
            self.content_list = []

    def append(self, new_content):
        self.content_list.append(new_content)

    def render(self, out_file):
        """
        Render the element.
        """
        out_file.write("".join(['<', self.tag, '>\n']))

        for content in self.content_list:
            out_file.write("".join([content, '\n']))

        out_file.write("".join(['</', self.tag, '>\n']))


class Html(Element):
    """
    HTML subclass of element.
    """
    tag = 'html'


class Body(Element):
    """
    Body subclass of element
    """
    tag = 'body'


class P(Element):
    """
    Paragraph subclass of element.
    """
    tag = 'p'
