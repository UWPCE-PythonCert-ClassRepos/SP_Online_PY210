#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.content = []
        if content is not None:
            self.content = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def opening_tag(self, cur_ind=""):
        opening_tag = [f"{cur_ind}<{self.tag}"]
        for key, value in self.attributes.items():
            opening_tag.append(f' {key}="{value}"')
        opening_tag.append(">")
        return "".join(opening_tag)

    def closing_tag(self, cur_ind=""):
        return f"{cur_ind}</{self.tag}>"

    def render(self, out_file, cur_ind=""):
        out_file.write(self.opening_tag(cur_ind) + '\n')
        for item in self.content:
            try:
                item.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + str(item) + '\n')
        out_file.write(self.closing_tag(cur_ind) + '\n')


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(self.opening_tag(cur_ind))
        for item in self.content:
            try:
                item.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(str(item))
        out_file.write(self.closing_tag(cur_ind="") + '\n')


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag has tag only")
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.opening_tag()[:-1] + ' />\n')

    def append(self, new_content):
        raise TypeError("SelfClosingTag has tag only")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Meta(SelfClosingTag):
    tag = "meta"


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
    tag = "h"

    def __init__(self, level=1, content=None, **kwargs):
        self.tag += str(level).strip()
        super().__init__(content, **kwargs)
