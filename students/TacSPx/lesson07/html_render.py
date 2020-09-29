#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.contents = [content]
        else:
            self.contents = []

        if kwargs is not None:
            self.attributes = kwargs
        else:
            self.attributes = {}

    ##################################################

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(f' {key}="{value}"')
        open_tag.append(">")
        return ''.join(open_tag)

    def _close_tag(self):
        return '</{}>'.format(self.tag)

    def append(self, new_content):
        return self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        # loop through the list of contents:
        out_file.write(cur_ind + self._open_tag() + '\n')
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content + '\n')
        out_file.write(cur_ind + self._close_tag() + '\n')


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Html(Element):
    tag = "html"


class Head(Element):
    tag = "head"


class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag() + '\n')

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


# Step 5

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, outfile, cur_ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        outfile.write(cur_ind + tag)

    def append(self, *args):
        raise TypeError("You cannot add content to SelfClosingTag")

    def _open_tag(self):
        return super()._open_tag()[:-2]

    def _close_tag(self):
        return " />\n".format(self.tag)


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


# Step 6

class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


# Step 7

class Li(Element):
    tag = "li"


class Ul(Element):
    tag = "ul"


# class Ol(Element):
#     tag = "ol"


class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        self.tag = "h{}".format(level)
        super().__init__(content, **kwargs)
