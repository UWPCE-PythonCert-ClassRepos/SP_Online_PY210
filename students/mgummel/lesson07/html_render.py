#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    attrs = ""
    indent = 3 * ' '

    def __init__(self, content=None, **kwargs):
        self.content = list()
        if content:
            self.content = [content]

        if kwargs:
            for key,value in kwargs.items():
                self.attrs += f' {key}=\"{value}\"'
        

    def append(self, new_content):
        self.content += [new_content]


    def render(self, out_file, curr_ind=""):
        if self.tag != "html":
            curr_ind = curr_ind + self.indent
        out_file.write(self._open_tag(curr_ind))

        for item in self.content:
            try:
                item.render(out_file, curr_ind)
            except AttributeError:
                out_file.write(curr_ind + self.indent)
                out_file.write(f'{item}'.strip())
            out_file.write('\n')

        out_file.write(self._close_tag(curr_ind))


    def _open_tag(self, open_indent=""):
        open_tag = f'{open_indent}<{self.tag}'
        if self.attrs:
            open_tag += f'{self.attrs}'
        open_tag += f'>\n'
        return open_tag


    def _close_tag(self, close_indent=""):
        return f'{close_indent}</{self.tag}>'


class Html(Element):
    def render(self, out_file, curr_ind=""):
        out_file.write(f'{curr_ind}<!DOCTYPE html>\n')
        super().render(out_file, curr_ind)


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

    def render(self, out_file, curr_ind=""):
        out_file.write(curr_ind + self.indent)
        one_line = f'{self._open_tag()}{self.content[0]}{self._close_tag()}'.replace('\n', '')
        out_file.write(one_line)


class H(OneLineTag):
    tag = "h"

    def __init__(self, header_level, content=None, **kwargs):
        self.tag += str(header_level)
        super().__init__(content, **kwargs)


class Title(OneLineTag):
    tag = "title"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content, **kwargs):
        kwargs['href']= f'{link}'
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):

        if content is not None:
            raise TypeError("Can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, new_content):
        raise TypeError("Can not contain any content")

    def render(self, out_file, curr_ind=""):
        out_file.write(curr_ind + self.indent)
        closing_tag = f'<{self.tag} />\n'
        if self.attrs:
            closing_tag = closing_tag.replace(' ', f'{self.attrs} ')
        out_file.write(closing_tag)


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Meta(SelfClosingTag):
    tag = "meta"