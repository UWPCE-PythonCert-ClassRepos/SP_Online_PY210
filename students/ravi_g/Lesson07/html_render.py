#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes_d = {}
        if content is not None:
            self.contents = [content]
        else:
            self.contents = []
        for k,v in kwargs.items():
            self.attributes_d[k] = v

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        # loop through the list of file_contents
        out_file.write(cur_ind)
        out_file.write("<{}".format(self.tag))
        if len(self.attributes_d.items()) > 0:
            for k,v in self.attributes_d.items():
                out_file.write(" {}=\"{}\"".format(k,v))
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

# Subclass of Element for Body
class Body(Element):

    tag = "body"


# Subclass of Element for Html
class Html(Element):

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


# Subclass of Element for Para
class P(Element):

    tag = "p"


# Subclass of Element for Head
class Head(Element):

    tag = "head"


# Class for OneLineTag
class OneLineTag(Element):
    def render(self, out_file, cur_ind = ""):
        out_file.write(cur_ind)
        out_file.write("<{}".format(self.tag))
        for k,v in self.attributes_d.items():
            out_file.write(" {}=\"{}\"".format(k,v))
        out_file.write(">")
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
    def append(self, new_content):
        raise NotImplementedError

# Subclass for Title
class Title(OneLineTag):
    tag = "title"


#subclass for SelfClosingTag
class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        self.attributes_d = dict()
        if content is not None:
            print("A SelfClosingTag cannot be initialized with contents.")
            raise TypeError
        for k, v in kwargs.items():
            self.attributes_d[k] = v
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
        if len(self.attributes_d.items()) > 0:
            for k, v in self.attributes_d.items():
                out_file.write(" {}=\"{}\"".format(k, v))
        out_file.write(self._close_tag())
        out_file.write("\n")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Li(Element):
    tag = "li"

# Anchor class
class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content):
        self.attributes_d = dict()
        self.attributes_d['href'] = link
        self.contents = [content]


class H(OneLineTag):

    def __init__(self, level, content, **kwargs):
        self.tag = "h" + str(level)
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"


class Ul(Element):
    tag = "ul"

    def __init__(self, **kwargs):
        self.attributes = dict()
        self.contents = []
        for k, v in kwargs.items():
            self.attributes[k] = v


    def append(self, content):
        self.contents.append(content)
