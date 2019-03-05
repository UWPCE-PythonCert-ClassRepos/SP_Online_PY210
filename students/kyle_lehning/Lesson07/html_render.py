#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = []
        if kwargs.__len__() is not 0:
            for item in kwargs.items():
                self.attributes.append(item)

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        first_tag = self.open_tag()
        first_tag.append(">\n")
        out_file.write("".join(first_tag))
        # loop through the list of contents
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                    out_file.write("{}\n".format(content))
        out_file.write("</{}>\n".format(self.tag))

    def open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes:
            open_tag.append(" {}=\"{}\"".format(key, value))
        open_tag.append(">")
        return open_tag


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Html(Element):
    tag = "html"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("".join(self.open_tag()))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        # Keeps the user from trying to append more than one line
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"
