#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "   "

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.content = [content]
        else:
            self.content = []

        if kwargs is not None:
            self.attributes = kwargs
        else:
            self.attributes = {}

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file, cur_indentent=""):
        out_file.write(cur_indentent + self.open_tag())
        out_file.write("\n")
        for content in self.content:
            try:
                content.render(out_file, cur_indentent + self.indent)
            except AttributeError:
                out_file.write(cur_indentent + self.indent + content)
                out_file.write("\n")
        out_file.write(cur_indentent + self.close_tag())
        out_file.write("\n")

    def open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(" {}=\"{}\"".format(key, value))
        open_tag.append(">")
        return "".join(open_tag)

    def close_tag(self):
        close_tag = "</{}>".format(self.tag)
        return close_tag

    def get_element_attributes(self):
        attribute = [self.tag]

        if self.attributes is not None:
            attribute.extend([f"{k}=\"{v}\"" for k, v in self.attributes.items()])

        return " ".join(attribute)


class SimpleElement(Element):
    def render(self, out_file, current_indent=""):
        out_file.write(current_indent)
        self.open_tag(out_file)
        out_file.write('>')
        out_file.write((self.content[0]))
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class SelfClosingElement(SimpleElement):
    def __init__(self, **kwargs):
        self.attributes = kwargs


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_indent=""):
        out_file.write(cur_indent + "<!DOCTYPE html>\n")
        super().render(out_file, cur_indent)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file, cur_indentent=""):
        out_file.write(cur_indentent + self.open_tag())
        out_file.write(self.content[0])
        out_file.write(self.close_tag())

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):
    tag = "h"

    def __init__(self, level, content=None, **kwargs):
        self.tag = '{}{}'.format(self.tag, level)
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag cannot contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_indentent=""):
        out_file.write(cur_indentent + self.open_tag()[:-1] + " />\n")

    def append(self, *args):
        raise TypeError("You cannot add content to a SelfClosingTag")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"


class Meta(SelfClosingTag):
    tag = "meta"

