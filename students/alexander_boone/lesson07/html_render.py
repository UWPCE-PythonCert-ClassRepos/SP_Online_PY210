#!/usr/bin/env python

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None, **kwargs):
        self.attributes = dict()
        if content == None:
            self.contents = []
        else:
            self.contents = [content]
        for key, value in kwargs.items():
            self.attributes[key] = value

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write("<{}".format(self.tag))
        if len(self.attributes.items()) > 0:
            for key, value in self.attributes.items():
                out_file.write(" {}=\"{}\"".format(key, value))
        out_file.write(">\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}".format(self.tag))
        for key, value in self.attributes.items():
                out_file.write(" {}=\"{}\"".format(key, value))
        out_file.write(">")
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
    def append(self, new_content):
        raise NotImplementedError

class Html(Element):
    pass

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        self.attributes = dict()
        if content != None:
            print("A SelfClosingTag cannot be initialized with contents.")
            raise TypeError
        for key, value in kwargs.items():
            self.attributes[key] = value
        pass

    def _open_tag(self):
        return "<" + self.tag


    def _close_tag(self):
        return " />"


    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


    def render(self, out_file):
        out_file.write(self._open_tag())
        if len(self.attributes.items()) > 0:
            for key, value in self.attributes.items():
                out_file.write(" {}=\"{}\"".format(key, value))
        out_file.write(self._close_tag())
        out_file.write("\n")

class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content):
        self.attributes = dict()
        self.attributes['href'] = link
        self.contents = [content]
