#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content=None, **kwargs):
        self.contents = [content]
        self.attributes = [kwargs]
        print(self.attributes)

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        open_tag = ["<{}".format(self.tag)]
        for dictPair in self.attributes:
            if dictPair:
                for key, value in dictPair.items():
                    open_tag.append(" ")
                    open_tag.append(key)
                    open_tag.append("=")
                    open_tag.append('"{}"'.format(value))
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        for content in self.contents:
            if content is not None:
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(content)
                out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))

    # def render(self, out_file):
    #     out_file.write("<{}".format(self.tag))
    #     for dictPair in self.attributes:
    #         if dictPair:
    #             for key, value in dictPair.items():
    #                 out_file.write(" ")
    #                 out_file.write(key)
    #                 out_file.write("=")
    #                 out_file.write('"{}"'.format(value))
    #     out_file.write(">\n")
    #     for content in self.contents:
    #         if content is not None:
    #             try:
    #                 content.render(out_file)
    #             except AttributeError:
    #                 out_file.write(content)
    #             out_file.write("\n")
    #     out_file.write("</{}>\n".format(self.tag))


class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"


class OneLineTag(Element):
    tag = "title"

    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def render(self, out_file):
        # loop through the list of contents:
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(self._close_tag())
        out_file.write("\n")

class Hr(SelfClosingTag):
    tag = "hr"
