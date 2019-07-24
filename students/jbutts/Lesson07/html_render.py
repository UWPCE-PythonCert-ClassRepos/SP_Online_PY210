#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    indent = "   "

    def __init__(self, content=None, **kwargs):
        self.content = content
        self.attributes = kwargs
        if content is None:
            self.content = []

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write("".join(self.content))


class Html(object):

    def __init__(self, content=None, **kwargs):
        self.content = content
        self.attributes = kwargs
        if content is None:
            self.content = []

    tag = "<html>"

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        for content in self.content:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)




class Body(object):

    def __init__(self, content=None, **kwargs):
        self.content = content
        self.attributes = kwargs
        if content is None:
            self.content = []

    tag = "body"

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write(self.content)



class P(object):

    def __init__(self, content=None, **kwargs):
        self.content = content
        self.attributes = kwargs
        if content is None:
            self.content = []

    tag = "P"

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write("".join(self.content))
