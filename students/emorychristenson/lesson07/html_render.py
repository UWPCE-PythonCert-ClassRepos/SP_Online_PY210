#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.contents = []
        if content is not None:
            self.contents = [content]

        if kwargs is not None:
            self.attributes = kwargs
        else:
            self.attributes = {}

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, ind=""):
        out_file.write(ind + self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, self.indent + ind)
            except AttributeError:
                out_file.write(self.indent + ind + content)
            out_file.write("\n")
        out_file.write(ind + self._close_tag())

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(" {}=\"{}\"".format(key, value))
        open_tag.append(">")
        return "".join(open_tag)

    def _close_tag(self):
        close_tag = "</{}>".format(self.tag)
        return close_tag
            
class Html(Element):
    tag = "html"

    def render(self, out_file, ind=""):
        out_file.write(ind + "<!DOCTYPE html>\n")
        super().render(out_file, ind)

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def append(self, content):
        raise NotImplementedError

    def render(self, out_file, ind=""):
        out_file.write(ind + self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("Must not contain any content")
        super().__init__(None, **kwargs)

    def render(self, outfile, ind=""):
        tag = ind + self._open_tag()[:-1] + " />\n"
        outfile.write(tag)

    def append(self, content=None):
        if content is not None:
            raise TypeError("Cannot append to a self closing tag.")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = "h{}".format(level)
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"