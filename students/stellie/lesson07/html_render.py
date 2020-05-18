#!/usr/bin/env python3

# Stella Kim
# Assignment 5: HTML Renderer Exercise

"""
A class-based system for rendering HTML.
"""


# Base class framework
class Element(object):
    tag_name = 'html'

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag_name))
        for content in self.contents:   # loop through list of contents
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag_name))


class Html(Element):
    tag_name = 'html'


class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'


class Head(Element):
    tag_name = 'head'


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag_name))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag_name))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag_name = 'title'
