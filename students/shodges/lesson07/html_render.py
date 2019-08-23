#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=''):
        self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag))
        for this_content in self.contents:
            try:
                this_content.render(out_file)
            except AttributeError:
                out_file.write(this_content)
            else:
                out_file.write('\n')
        out_file.write("</{}>\n".format(self.tag))

class SimpleElement(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        for this_content in self.contents:
            try:
                this_content.render(out_file)
            except AttributeError:
                out_file.write(this_content)
        out_file.write("</{}>\n".format(self.tag))

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'
