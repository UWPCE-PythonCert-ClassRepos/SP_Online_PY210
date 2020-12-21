#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = 0*" "

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.contents = [content]
        self.attributes = dict(**kwargs)

    def _open_tag(self):
        return "<{}".format(self.tag)

    def _close_tag(self):
        return ">\n"

    def append(self, new_content):
        try:
            self.contents.append(new_content)
        except AttributeError:
            self.contents = []
            self.contents.append(new_content)

    def render(self, out_file, ind=""):
        if ind is "":
            ind = self.indent
        tag = [self._open_tag()]
        for key, value in self.attributes.items():
            attribute = " " + key + "=" + "\"" + value + "\""
            tag.append(attribute)
        tag.append(self._close_tag())
        out_file.write(ind)
        out_file.write("".join(tag))
        try:
            for content in self.contents:
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(ind+4*" ")
                    out_file.write(content)
        except AttributeError:
            pass 
        out_file.write("\n")
        out_file.write(ind)
        out_file.write("</{}>\n".format(self.tag))

class Html(Element):
    tag= "html"
    indent = ""
    
    def render(self, out_file, ind=""):
        if ind is "":
            ind=self.indent
        out_file.write("<!DOCTYPE html>\n")
        encoding = Meta()
        encoding.render(out_file)
        Element.render(self, out_file, ind)

class Body(Element):
    tag = "body"
    indent = 4*" "

class P(Element):
    tag = "p"
    indent = 8*" "

class Head(Element):
    tag = "head"
    indent = 4*" "

class OneLineTag(Element):
    def render(self, out_file, ind=""):
        out_file.write(ind)
        out_file.write("<{}> ".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write(ind)
        out_file.write(" </{}>".format(self.tag))
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"
    indent = 8*""

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag cannot contain any content")
        Element.__init__(self, content=content, **kwargs)

    def append(self, new_content):
        raise TypeError("You cannot add content to a SelfClosingTag")

    def render(self, out_file, ind=""):
        tag = [self._open_tag()]
        for key, value in self.attributes.items():
            attribute = " " + str(key) + "=" + "\"" + str(value) + "\""
            tag.append(attribute)
        try:
            tag.append(" " + self.content)
        except AttributeError:
            pass
        tag.append(" />\n")
        out_file.write(ind)
        out_file.write("".join(tag))


class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class Meta(SelfClosingTag):
    tag = "meta"
    def __init__(self, content=None, **kwargs):
        self.content = 'charset="UTF-8"'
        Element.__init__(self, content=content, **kwargs)

class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs["href"] = link
        super().__init__(content, **kwargs)

    def render(self, out_file, ind=""):
        tag = [self._open_tag()]
        for key, value in self.attributes.items():
            href = " " + str(key) + "=" + "\"" + str(value) + "\"" + ">"
        tag.append(href)
        tag.append(self.contents[0])
        tag.append("</a>\n")
        out_file.write(ind)
        out_file.write("".join(tag))

class Ul(Element):
    tag = "ul"
    indent = 8*""

class Li(Element):
    tag = "li"
    indent = 12*""

class H(OneLineTag):
    tag = "h"

    def __init__(self, level, content=None, **kwargs):
        self.tag = self.tag + str(level)
        super().__init__(content, **kwargs)