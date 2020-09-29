#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "  "

    def __init__(self, content=None, **kwargs):
        if content:
            self.contents = [content]
        else:
            self.contents = []
        if kwargs:
            self.attributes = kwargs
        else:
            self.attributes = {}

    def append(self, new_content):
        if hasattr(new_content, 'render'):
            self.contents.append(new_content)
        else:
            self.contents.append((str(new_content)))

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

    def _open_tag(self, cur_ind=""):
        open_tag = ["{}<{}".format(cur_ind, self.tag)]
        for k, v in self.attributes.items():
            open_tag.append(" {}=\"{}\"".format(k, v))
        open_tag.append(">")
        return "".join(open_tag)

    def _close_tag(self, cur_ind=""):
        return "{}</{}>".format(cur_ind, self.tag)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def append(self, contents):
        raise NotImplementedError

    def render(self, out_file, cur_ind=""):
        out_file.write(self._open_tag(cur_ind))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, out_file, cur_ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(cur_ind)
        out_file.write(tag)


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Meta(SelfClosingTag):
    tag = "meta"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs["href"] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        self.tag = "h{}".format(level)
        super().__init__(content, **kwargs)


