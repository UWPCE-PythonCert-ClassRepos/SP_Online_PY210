#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

class Element(object):
    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.attributes = []
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        if kwargs.__len__() != 0:
            for item in kwargs.items():
                self.attributes.append(item)

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))

class OneLineTag(Element):

    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write("</{}>\n".format(self.tag))
    
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = 'title'

class Html(Element):
    tag = 'html'

class Head(Element):
    tag = 'head'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

