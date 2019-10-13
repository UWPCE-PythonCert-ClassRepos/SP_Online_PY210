#!/usr/bin/env python

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = dict()
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        for key, value in kwargs.items():
            self.attributes[key] = value

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<{}".format(self.tag))
        if len(self.attributes.items()) > 0:
            for key, value in self.attributes.items():
                out_file.write(" {}=\"{}\"".format(key, value))
        out_file.write(">\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent)
                out_file.write(content)
                out_file.write("\n")
        out_file.write(cur_ind)
        out_file.write("</{}>\n".format(self.tag))


class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<{}".format(self.tag))
        for key, value in self.attributes.items():
            out_file.write(" {}=\"{}\"".format(key, value))
        out_file.write(">")
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, new_content):
        raise NotImplementedError


class Html(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)

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
        if content is not None:
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

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
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


class Meta(SelfClosingTag):
    tag = "meta"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content):
        self.attributes = dict()
        self.attributes['href'] = link
        self.contents = [content]


class H(OneLineTag):

    def __init__(self, level, content, **kwargs):
        self.tag = "h" + str(level)
        super().__init__(content, **kwargs)


class Li(Element):
    tag = "li"


class Ul(Element):
    tag = "ul"

    def __init__(self, **kwargs):
        self.attributes = dict()
        self.contents = []
        for key, value in kwargs.items():
            self.attributes[key] = value

    def append(self, content):
        self.contents.append(content)
