#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "  "

    def __init__(self, content=None, **kwargs):
        self.contents = [content] if content is not None else []
        self.attributes = kwargs if kwargs is not None else {}

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, curr_indent=""):

        out_file.write(curr_indent + self._open_tag() + "\n")
        # loop through the list of contents:
        for content in self.contents:
            try:
                print(content)
                content.render(out_file, curr_indent + self.indent)
            except AttributeError:
                out_file.write(curr_indent + self.indent + content + "\n")
        out_file.write(curr_indent + self._close_tag() + "\n")

    def _open_tag(self):

        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        return "".join(open_tag)

    def _close_tag(self):
        return "</{}>".format(self.tag)


# This is the subclass for the html tag
class Html(Element):
    tag = "html"

    def render(self, out_file, curr_ind="", **kwargs):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, curr_ind)


# This is the subclass for the head tag
class Head(Element):
    tag = "head"


# This is the subclass for the body tag
class Body(Element):
    tag = 'body'


# This is the subclass for the P tag
class P(Element):
    tag = 'p'


# This is the subclass for the list element
class Ul(Element):
    tag = 'ul'

    def __init__(self, content=None, **kwargs):
        if content is not None and not isinstance(content, Li):
            # print("The content is:", content)
            raise TypeError
        super().__init__(content, **kwargs)


# This is the subclass for the list element
class Li(Element):
    tag = 'li'


# This is the class for the one line tage element. It overwrites the append and render methods
class OneLineTag(Element):

    # Make sure no content can be appended
    def append(self, content):
        raise NotImplementedError

    # Render the element and any attributes
    def render(self, out_file,  curr_ind="", **kwargs):

        out_file.write(curr_ind + self._open_tag())

        # loop through the list of contents:
        for content in self.contents:
            try:
                content.render(out_file, curr_ind + self.indent)
            except AttributeError:
                out_file.write(content)

        out_file.write("</{}>".format(self.tag))
        out_file.write("\n")


class Title(OneLineTag):
    tag = "title"


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
            raise TypeError("Self Closing Tags can not contain content")
        super().__init__(content=content, **kwargs)

    def append(self, content):
        raise TypeError

    def render(self, out_file, curr_ind="", **kwargs):
        out_file.write(curr_ind + "{}/>\n".format(self._open_tag()[:-1]))


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Meta(SelfClosingTag):
    tag = "meta"
