#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content='', **kwargs):
        self.contents = [content]
        self.elem_attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        self.print_open_tag(out_file)
        for this_content in self.contents:
            try:
                this_content.render(out_file)
            except AttributeError:
                out_file.write(this_content)
        out_file.write("</{}>\n".format(self.tag))

    def print_open_tag(self, out_file, newline=True):
        out_file.write("<{}".format(self.tag))
        for k, v in enumerate(self.elem_attributes):
            out_file.write(" {}=\"{}\"".format(k, v))
        out_file.write(">")
        if newline == True:
            out_file.write("\n")

class SimpleElement(Element):
    def render(self, out_file):
        self.print_open_tag(out_file, False)
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class Title(SimpleElement):
    tag = 'title'
