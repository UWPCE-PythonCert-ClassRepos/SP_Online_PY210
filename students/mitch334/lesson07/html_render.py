#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = ' ' * 4

    def __init__(self, content=None, **kwargs):
        self.contents = []
        self.kwargs = kwargs

        if content is not None:
            self.contents = [content]


    def append(self, new_content):
        self.contents.append(new_content)


    def _open_tag(self, cur_ind=''):
        open_tag = '{}<{}'.format(cur_ind, self.tag)

        for kwarg in self.kwargs:
            open_tag += ' ' + kwarg + '=\"' + self.kwargs[kwarg] + '\"'
        open_tag += '>'

        return open_tag


    def _close_tag(self, cur_ind=''):
        return '{}</{}>'.format(cur_ind, self.tag)


    def render(self, out_file, cur_ind=''):
        out_file.write(self._open_tag(cur_ind))
        out_file.write('\n')

        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
                out_file.write('\n')

        out_file.write(self._close_tag(cur_ind))
        out_file.write('\n')


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=''):
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file, cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file, cur_ind=''):
        out_file.write(self._open_tag(cur_ind))

        out_file.write(self.contents[0])
        # out_file.write('</{}>'.format(self.tag))
        out_file.write(self._close_tag())
        out_file.write('\n')


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        self.kwargs = kwargs

        if content:
            raise TypeError('Content is not allowed in self closing tags.')


    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


    def render(self, out_file, cur_ind=''):
            out_file.write(self._open_tag(cur_ind)[:-1] + ' />\n')

class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Meta(SelfClosingTag):
    tag = "meta"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content, **kwargs):
        self.contents = []
        self.kwargs = kwargs
        self.kwargs['href'] = link

        if content:
            self.contents.append(content)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):
    tag = "h"

    def __init__(self, level, content, **kwargs):
        self.contents = []
        self.kwargs = kwargs
        self.tag = self.tag + str(level)

        if content:
            self.contents.append(content)
