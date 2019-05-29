#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=None):
        self.content = [content] if content else []

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write('<{}>\n'.format(self.tag))
        for line in self.content:
            try:
                out_file.write(line + '\n')
            except TypeError:
                line.render(out_file)
        out_file.write('</{}>\n'.format(self.tag))

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'
