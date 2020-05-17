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

    def _open_tag(self, indent):
        open_tag = indent + "<{}".format(self.tag_name)
        open_tag = open_tag + self._render_attributes()
        open_tag = open_tag + ">\n"
        return open_tag

    def _render_attributes(self):
        element_attributes = ""
        if len(self.attributes) > 0:
            attrs = []
            for k, v in self.attributes.items():
                attrs.append(k + "=" + "\"" + str(v) + "\"")
            element_attributes = " " + " ".join(attrs)
        return element_attributes

    def _render_content(self, content, indent):
        content_out = indent + str(content)
        if (content == self.content_list[-1]):
            content_out = content_out + "\n"
        return content_out

    def _close_tag(self, indent):
        return indent + "</{}>\n".format(self.tag_name)

    def render(self, out_file, curr_ident=""):
        out_file.write(self._open_tag(curr_ident))
        for content in self.content_list:
            if hasattr(content, 'render'):
                content.render(out_file, curr_ident + self.indent)
            else:
                out_file.write(self._render_content(content, curr_ident + self.indent))
        out_file.write(self._close_tag(curr_ident))


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

    def _open_tag(self, indent):
        open_tag = indent + "<{}".format(self.tag_name)
        open_tag = open_tag + self._render_attributes()
        open_tag = open_tag + ">"
        return open_tag

    def _render_content(self, content, indent):
        return str(content)

    def _close_tag(self, indent):
        return "</{}>\n".format(self.tag_name)


class Title(OneLineTag):
    tag_name = "title"


class SelfClosingTag(Element):
    tag_name = "selfclosing"

    def __init__(self, Content=None, **kwargs):
        if Content is not None:
            raise ValueError("SelfClosingTag cannot have content")
        else:
            Element.__init__(self, **kwargs)

    def _open_tag(self, indent):
        open_tag = indent + "<{}".format(self.tag_name)
        open_tag = open_tag + self._render_attributes()
        open_tag = open_tag + " />\n"
        return open_tag

    def _close_tag(self, indent):
        return ""


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
