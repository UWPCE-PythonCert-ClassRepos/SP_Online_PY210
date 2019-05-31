#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None, **kwargs):
        self.contents = []
        self.kwargs = kwargs

        if content is not None:
            self.contents = [content]
        # print("contents is:", self.contents)

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        # print('self.contents: ', self.contents)

        if self.kwargs:
            attribute = ''
            for kwarg in self.kwargs:
                attribute += ' ' + kwarg + '=\"' + self.kwargs[kwarg] + '\"'

            out_file.write('<{}{}>\n'.format(self.tag, attribute))
        else:
            out_file.write('<{}>\n'.format(self.tag))

        for content in self.contents:

            if hasattr(content, 'render'):
                content.render(out_file)
            else:
                out_file.write(content + '\n')

        out_file.write('</{}>\n'.format(self.tag))


class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write('<{}>'.format(self.tag))

            if hasattr(content, 'render'):
                content.render(out_file)
            else:
                out_file.write(content)

            out_file.write('</{}>\n'.format(self.tag))

class Title(OneLineTag):
    tag = "title"
