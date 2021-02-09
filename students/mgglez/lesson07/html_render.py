#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag_name = 'html'
    indent = 4

    def __init__(self, content=None, **kwargs):
        self.contents = []
        if content is not None:
            self.contents.append(content)
        self.attrs = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, curr_ind=None):

        if curr_ind is not None:
            self_indentation = self.indent * curr_ind * " "
            next_elem_indentation = curr_ind + 1
            not_an_elem_indentation = self.indent * (curr_ind + 1) * " "
        else:
            self_indentation = ""
            next_elem_indentation = None
            not_an_elem_indentation = ""

        if self.attrs:
            open_tag_attrs = " ".join(["{}='{}'".format(k, v) for k, v in self.attrs.items()])
            out_file.write("{}<{} {}>\n".format(self_indentation, self.tag_name, open_tag_attrs))
        else:
            out_file.write("{}<{}>\n".format(self_indentation, self.tag_name))

        for content in self.contents:
            try:
                content.render(out_file, next_elem_indentation)
            except AttributeError:
                out_file.write("{}{}\n".format(not_an_elem_indentation, content))
        out_file.write("{}</{}>\n".format(self_indentation, self.tag_name))


class Html(Element):
    tag_name = 'html'

    def render(self, out_file, curr_ind=None):
        if curr_ind is not None:
            self_indentation = self.indent * curr_ind * " "
        else:
            self_indentation = ""

        out_file.write("{}<!DOCTYPE html>\n".format(self_indentation))
        super().render(out_file, curr_ind)


class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'


class Head(Element):
    tag_name = 'head'


class OneLineTag(Element):
    def render(self, out_file, curr_ind=None):

        if curr_ind is not None:
            self_indentation = self.indent * curr_ind * " "
            not_an_elem_indentation = self.indent * (curr_ind + 1) * " "
        else:
            self_indentation = ""
            not_an_elem_indentation = ""

        if self.attrs:
            open_tag_attrs = " ".join(["{}='{}'".format(k, v) for k, v in self.attrs.items()])
            out_file.write("{}<{} {}>".format(self_indentation, self.tag_name, open_tag_attrs))
        else:
            out_file.write("{}<{}>".format(self_indentation, self.tag_name))
        out_file.write("{}".format(self.contents[0]))
        out_file.write("</{}>\n".format(self.tag_name))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag_name = 'title'


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("Self Closing Tags do not contain any content")
        super().__init__(content=content, **kwargs)


    def render(self, out_file, curr_ind=None):

        if curr_ind is not None:
            self_indentation = self.indent * curr_ind * " "
        else:
            self_indentation = ""

        if self.attrs:
            open_tag_attrs = " ".join(["{}='{}'".format(k, v) for k, v in self.attrs.items()])
            out_file.write("{}<{} {} />\n".format(self_indentation, self.tag_name, open_tag_attrs))
        else:
            out_file.write("{}<{} />\n".format(self_indentation, self.tag_name))

    def append(self, content):
        raise TypeError("Self Closing Tags do not contain any content")


class Hr(SelfClosingTag):
    tag_name = "hr"


class Br(SelfClosingTag):
    tag_name = "br"


class A(OneLineTag):
    tag_name = 'a'

    def __init__(self, link, content=None, **kwargs):
        super().__init__(content=content, href=link, **kwargs)


class Ul(Element):
    tag_name = "ul"


class Li(Element):
    tag_name = "li"


class Header(OneLineTag):
    tag_name = "h"

    def __init__(self, header_level, content, **kwargs):
        self.tag_name += str(header_level)
        super().__init__(content=content, **kwargs)

class Meta(SelfClosingTag):
    tag_name = "meta"
