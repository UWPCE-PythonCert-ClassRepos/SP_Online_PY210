#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "  "

    def __init__(self, content=None, **kwargs):
        self.attributes = {**kwargs}
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        self.indent = cur_ind
        out_file.write(self.indent + self._open_tag())
        for content in self.contents:
            try:
                content.render(out_file, self.indent + "  ")
            except AttributeError:
                out_file.write(self.indent + "  " + content)
                out_file.write("\n")
        out_file.write(self.indent + self._close_tag())

    def _open_tag(self):
        if self.attributes:
            open_tag = ["<{}".format(self.tag)]
            for key, value in self.attributes.items():
                open_tag.append(" {}=\"{}\"".format(key, value))
            open_tag.append(">\n")
            _open_tag = "".join(open_tag)
        else:
            _open_tag = "<{}>\n".format(self.tag)
        return _open_tag

    def _close_tag(self):
        _close_tag = "</{}>\n".format(self.tag)
        return _close_tag


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write("<!DOCTYPE html>")
        out_file.write("\n")
        Element.render(self, out_file, cur_ind)


class Head(Element):
    tag = "head"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class OneLineTag(Element):

    def append(self, content):
        raise NotImplementedError

    def render(self, out_file, cur_ind=""):
        self.indent = cur_ind + "  "
        out_file.write(self.indent + self._open_tag().strip())
        out_file.write(self.contents[0].strip())
        out_file.write(self._close_tag())


class Title(OneLineTag):
    tag = "title"


class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        self.tag = "h{}".format(level)
        super().__init__(content, **kwargs)


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, outfile, cur_ind=""):
        self.indent = cur_ind + "  "
        tag = self._open_tag()[:-2] + " />\n"
        outfile.write(self.indent + tag)


class Meta(SelfClosingTag):
    tag = "meta"


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"
