#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag_name = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content_list = []
        else:
            self.content_list = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.content_list.append(new_content)

    def render(self, out_file, curr_ident=""):
        out_file.write(curr_ident + "<" + self.tag_name + render_attributes(self.attributes))
        if isinstance(self, SelfClosingTag):
            out_file.write(" />\n")
        else:
            out_file.write(">")
            if not isinstance(self, OneLineTag):
                out_file.write("\n")

            for content in self.content_list:
                if hasattr(content, 'render'):
                    content.render(out_file, curr_ident + self.indent)
                else:
                    if not isinstance(self, OneLineTag):
                        out_file.write(curr_ident + self.indent)
                    out_file.write(str(content))
                    if not isinstance(self, OneLineTag) and content == self.content_list[-1]:
                        out_file.write("\n")
            if not isinstance(self, OneLineTag):
                out_file.write(curr_ident)
            out_file.write("</" + self.tag_name + ">" + "\n")


class Html(Element):
    tag_name = "html"

    def render(self, out_file, curr_ident=""):
        out_file.write(curr_ident + "<!DOCTYPE html>\n")
        Element.render(self, out_file, curr_ident)


class Body(Element):
    tag_name = "body"


class P(Element):
    tag_name = "p"


class Head(Element):
    tag_name = "head"


class OneLineTag(Element):
    tag_name = "onelinetag"
    indent = ""

class Title(OneLineTag):
    tag_name = "title"


class SelfClosingTag(Element):
    tag_name = "selfclosing"

    def __init__(self, Content=None, **kwargs):
        if Content is not None:
            raise ValueError("SelfClosingTag cannot have content")
        else:
            Element.__init__(self, **kwargs)


class Hr(SelfClosingTag):
    tag_name = "hr"


class Br(SelfClosingTag):
    tag_name = "br"


class A(OneLineTag):
    tag_name = "a"

    def __init__(self, link, content):
        kwargs = {"href": link}
        Element.__init__(self, content, **kwargs)


class Ul(Element):
    tag_name = "ul"


class Li(Element):
    tag_name = "li"


class H(OneLineTag):
    tag_name = "h"

    def __init__(self, level, content):
        self.tag_name = self.tag_name + str(level)
        OneLineTag.__init__(self, content)


class Meta(SelfClosingTag):
    tag_name = "meta"


# Helper methods
def render_attributes(attributes):
    element_attributes = ""
    if len(attributes) > 0:
        attrs = []
        for k, v in attributes.items():
            attrs.append(k + "=" + "\"" + str(v) + "\"")
        element_attributes = " " + " ".join(attrs)
    return element_attributes


