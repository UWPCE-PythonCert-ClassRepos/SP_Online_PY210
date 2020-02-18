#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "  "

    def __init__(self, contents=None, **kwargs):
        if contents is None:
            self.contents = []
        else:
            self.contents = [contents]
        if kwargs is None:
            self.attributes = {}
        else:
            self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.indent)
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except (TypeError, AttributeError):
                out_file.write(cur_ind + self.indent + content)
            out_file.write("\n")
        out_file.write(cur_ind + self.indent)
        out_file.write(self._close_tag())

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for k, v in self.attributes.items():
            open_tag.append(" {}=\"{}\"".format(k, v))
        open_tag.append(">")
        return "".join(open_tag)

    def _close_tag(self):
        close_tag = "</{}>".format(self.tag)
        return close_tag


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"
    indent = "  "


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write(self.indent + cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Ul(Element):
    tag = "ul"
    indent = "    "


class Li(Element):
    tag = "li"
    indent = "    "


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    tag = "title"
    indent = "  "

    def append(self, contents):
        raise NotImplementedError

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.indent)
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):

    def __init__(self, contents=None, **kwargs):
        if contents:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(contents=contents, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, out_file):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(tag)


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Meta(SelfClosingTag):
    tag = "meta"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, contents, **kwargs):
        kwargs["href"] = link
        super().__init__(contents, **kwargs)


class H(OneLineTag):

    def __init__(self, level, contents, **kwargs):
        self.tag = "h" + str(level)
        super().__init__(contents, **kwargs)


