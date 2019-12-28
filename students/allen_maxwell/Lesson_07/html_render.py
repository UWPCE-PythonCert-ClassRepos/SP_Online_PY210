#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 12/28/2019
# html_render.py

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwarks):
        self.attributes = kwarks
        self.contents = []
        if content is not None:
            self.contents = [content]

    def append(self, content):
        self.contents.append(content)

    def render(self, out_file, cur_ind=''):
        out_file.write(self._open_tag(cur_ind) + '\n')
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(self.indent + cur_ind + content + '\n')
        out_file.write(self._close_tag(cur_ind))

    def _open_tag(self, cur_ind=''):
        open_tag = ["{}<{}".format(cur_ind, self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append('>')
        return "".join(open_tag)

    def _close_tag(self, cur_ind=''):
        return '{}</{}>\n'.format(cur_ind, self.tag)


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=''):
        out_file.write('{}<!DOCTYPE html>\n'.format(cur_ind))
        super().render(out_file, cur_ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class OneLineTag(Element):
    def render(self, out_file, cur_ind=''):
        out_file.write(self._open_tag(cur_ind))
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = ('h{}'.format(level))
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, outfile, cur_ind=''):
        outfile.write(cur_ind + self._open_tag()[:-1] + ' />\n')

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class Meta(SelfClosingTag):
    tag = 'meta'
