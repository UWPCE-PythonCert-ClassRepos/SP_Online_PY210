#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.style = dict(kwargs)
        if content is not None:
            self.contents = [content]
        else:
            self.contents = []

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        open_tag = ['<{}'.format(self.tag)]
        for key, value in self.style.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append('>\n')
        out_file.write("".join(open_tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))


class Body(Element):
    tag = 'body'


class Html(Element):
    tag = 'html'


class P(Element):
    tag = 'p'


class head(Element):
    tag = 'head'


class OneLineTag(Element):
    tag = 'title'

    def append(self, new_content):
        raise NotImplementedError

    def render(self, out_file):
        out_file.write("<{}> ".format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(" </{}>".format(self.tag))


class SelfClosingTag(Element):
    pass


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'
