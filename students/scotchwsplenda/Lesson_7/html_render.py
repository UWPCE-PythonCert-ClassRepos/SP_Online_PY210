#!/usr/bin/env python3

"""
A class-based system for rendering html.
https://www.youtube.com/watch?v=RSl87lqOXDE&list=RDCMUCCezIgC97PvUuR4_gbFUs5g&index=8
STEP 3 - 3/8
STEP 4 - 3/9
STEP 7 - 3/13
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = '  '

    def __init__(self, content=None, **kwargs):

        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        open_tag = [f'<{self.tag}']
        for key, value in self.attributes.items():
            open_tag.append(f' {key}="{value}"')
        open_tag.append('>')
        open_tag = ''.join(open_tag)
        return open_tag

    def _close_tag(self):
        close_tag = f'</{self.tag}>'
        return close_tag

    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind + self._open_tag() + '\n')

        for content in self.contents:
            try:
                content.render(out_file, (cur_ind + self.indent))
            except AttributeError:
                out_file.write(cur_ind + self.indent + content + '\n')
        out_file.write(cur_ind + self._close_tag() + '\n')


# <p style="text-align: center" id="intro"> a paragraph of text </p>
class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<{}".format(self.tag))
        for key, value in self.attributes.items():
            out_file.write(" {}=\"{}\"".format(key, value))
        out_file.write(">")
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class Li(Element):
    tag = "li"


class Ul(Element):
    tag = "ul"


class Meta(Element):
    tag = "meta"


class Html(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file, cur_ind)


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=''):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(tag)

    def append(self, content):
        raise TypeError


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):

    tag = 'a'

    def __init__(self, link, content):
        self.attributes = dict()
        self.attributes['href'] = link
        self.contents = [content]


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = (f'h{level}')
        super().__init__(content, **kwargs)
