#!/usr/bin/env python3

# html_render.py
# opcode6502: SP_Online_PY210

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.contents = content
        if self.contents is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write('<{}>\n'.format(self.tag))
        for content in self.contents:
            out_file.write(content)
            out_file.write('\n')
        out_file.write('</{}>\n'.format(self.tag))


class Body(Element):

    tag = 'body'


class Html(Element):

    tag = 'html'

class P(Element):

    tag = 'p'