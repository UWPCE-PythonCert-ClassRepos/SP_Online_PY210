#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = ""

    def __init__(self, content=None, **element_attribute):

        if content is not None:
            self.contents = [content]
        else:
            self.contents = [""]
        if element_attribute:
            self.attributes = element_attribute

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        try:
            open_tag = [f"<{self.tag}"]
            for k, v in self.attributes.items():
                open_tag.append(f' {k}="{v}"')
            open_tag.append(">")
            return "".join(open_tag)
        except AttributeError:
            return f"<{self.tag}>"

    def _close_tag(self):
        return f"</{self.tag}>"

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.indent)
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent * 2 + content)
            out_file.write("\n")
        out_file.write(cur_ind + self.indent)
        out_file.write(self._close_tag())
        out_file.write("\n")


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write(self.indent + cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind="")


class Head(Element):
    tag = "head"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"
    indent = "    "


class OneLineTag(Element):
    tag = "title"
    indent = "    "

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.indent)
        out_file.write(f"{self._open_tag()}")
        out_file.write(self.contents[0])
        out_file.write(f"{self._close_tag()}")

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    tag = "hr"
    # indent = "    "

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.indent)
        out_file.write(self._open_tag()[:-1] + " />\n")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class A(Element):

    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul(Element):

    tag = "ul"
    indent = "    "


class Li(Element):

    tag = "li"
    indent = "    "


class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        self.tag = f"h{level}"
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):

    tag = "meta"

    def __init__(self, content=None, **kwargs):
        kwargs['charset'] = "UTF-8"
        super().__init__(content, **kwargs)
