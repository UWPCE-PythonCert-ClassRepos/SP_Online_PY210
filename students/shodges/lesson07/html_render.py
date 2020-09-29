#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = '  '

    def __init__(self, content=None, **kwargs):
        self.contents = [content]
        self.elem_attributes = kwargs


    def append(self, new_content):
        self.contents.append(new_content)


    def render(self, out_file, current_indent=''):
        out_file.write(current_indent)
        self.print_open_tag(out_file)
        out_file.write('>\n')
        for this_content in self.contents:
            try:
                this_content.render(out_file, current_indent + this_content.indent)
            except AttributeError:
                try:
                    out_file.write(current_indent + self.indent + this_content)
                    out_file.write("\n")
                except TypeError:
                    pass
        out_file.write("{}</{}>\n".format(current_indent, self.tag))


    def print_open_tag(self, out_file):
        out_file.write("<{}".format(self.tag))
        for k, v in self.elem_attributes.items():
            out_file.write(" {}=\"{}\"".format(k, v))


class SimpleElement(Element):
    def render(self, out_file, current_indent=''):
        out_file.write(current_indent)
        self.print_open_tag(out_file)
        out_file.write('>')
        out_file.write((self.contents[0]))
        out_file.write("</{}>\n".format(self.tag))


    def append(self, content):
        raise NotImplementedError


class SelfClosingElement(SimpleElement):
    def __init__(self, **kwargs):
        self.elem_attributes = kwargs


    def render(self, out_file, current_indent=''):
        out_file.write(current_indent)
        self.print_open_tag(out_file)
        out_file.write(" />\n")


class Html(Element):
    tag = 'html'
    indent = ''


    def render(self, out_file, current_indent=''):
        out_file.write(current_indent + "<!DOCTYPE html>\n")
        Element.render(self, out_file, current_indent)


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

    def __init__(self, link, content, **kwargs):
        SimpleElement.__init__(self, content, **kwargs)
        self.elem_attributes['href'] = link


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(SimpleElement):
    tag = 'h'

    def __init__(self, level, content='', **kwargs):
        if not str(level).isdigit():
            raise TypeError
        self.tag = '{}{}'.format(self.tag, level)
        SimpleElement.__init__(self, content, **kwargs)


class Meta(SelfClosingElement):
    tag = 'meta'


class Img(SelfClosingElement):
    tag = 'img'

    def __init__(self, link, **kwargs):
        SimpleElement.__init__(self, '', **kwargs)
        self.elem_attributes['src'] = link
