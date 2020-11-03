#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = ""
    add_new_line = True
    indent_spaces = 4
    indent = " " * indent_spaces

    def __init__(self, content=None, **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        self.attributes = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def get_opening_tag_string(self):
        opening_tag_string = ""
        opening_tag_string += f"<{self.tag}"
        for k, v in self.attributes.items():
            opening_tag_string += f' {k}="{v}"'
        opening_tag_string += ">"
        if self.add_new_line:
            opening_tag_string += "\n"
        return opening_tag_string

    def render(self, out_file=None, cur_ind=""):
        output_string = cur_ind
        if self.tag:
            output_string += self.get_opening_tag_string()
        for line in self.content:
            if not isinstance(line, str):
                output_string += line.render(out_file, cur_ind + self.indent)
            else:
                output_string += cur_ind + self.indent
                output_string += f"{line}"
            if self.add_new_line:
                output_string += "\n"
        if self.tag:
            output_string += cur_ind
            output_string += f"</{self.tag}>"
        if out_file:
            out_file.write(output_string)
        return output_string


class Html(Element):
    tag = "html"

    def render(self, out_file=None, cur_ind=""):
        header_string = "<!DOCTYPE html>\n"
        output_string = Element.render(self, out_file=None)
        if out_file:
            out_file.write(header_string + output_string)
        return header_string + output_string


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class OneLineTag(Element):
    add_new_line = False

    def render(self, out_file=None, cur_ind=""):
        output_string = cur_ind
        if self.tag:
            output_string += self.get_opening_tag_string()
        for line in self.content:
            output_string += f"{line}"
        if self.tag:
            output_string += f"</{self.tag}>"
        if out_file:
            out_file.write(output_string)
        return output_string


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            raise TypeError("SelfClosingTag can not have content")
        self.content = []
        self.attributes = kwargs

    def get_opening_tag_string(self):
        opening_tag_string = ""
        opening_tag_string += f"<{self.tag}"
        for k, v in self.attributes.items():
            opening_tag_string += f' {k}="{v}"'
        opening_tag_string += " />"
        return opening_tag_string

    def render(self, out_file=None, cur_ind=""):
        output_string = cur_ind
        if self.tag:
            output_string += self.get_opening_tag_string()
        if out_file:
            out_file.write(output_string)
        return output_string


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Meta(SelfClosingTag):
    tag = "meta"


class A(OneLineTag):  # Want links to be one line
    tag = "a"
    add_new_line = False

    def __init__(self, link, content, **kwargs):
        Element.__init__(self, content=content, href=link, **kwargs)


class H(OneLineTag):
    def __init__(self, level, content):
        try:
            int(level)
        except ValueError:
            raise TypeError("Level of H must be convertible to int")
        self.tag = f"h{level}"
        Element.__init__(self, content=content)
