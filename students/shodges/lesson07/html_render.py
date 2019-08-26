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
        for k, v in self.elem_attributes.items():
            out_file.write(" {}=\"{}\"".format(k, v))
        if isinstance(self, SelfClosingElement):
            out_file.write(" /")
        out_file.write(">")
        if newline == True:
            out_file.write("\n")

class SimpleElement(Element):
    def render(self, out_file):
        self.print_open_tag(out_file, False)
        if not isinstance(self, SelfClosingElement):
            out_file.write(self.contents[0])
            out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError

class SelfClosingElement(SimpleElement):
    def __init__(self, **kwargs):
        self.elem_attributes = kwargs

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

class Hr(SelfClosingElement):
    tag = 'hr'

class Br(SelfClosingElement):
    tag = 'br'

class A(SimpleElement):
    tag = 'a'

    def __init__(self, link, content):
        SimpleElement.__init__(self, content)
        self.elem_attributes = {'href': link}
