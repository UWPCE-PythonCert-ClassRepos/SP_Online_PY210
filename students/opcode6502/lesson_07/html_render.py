#!/usr/bin/env python3
#
# html_render.py
# opcode6502: SP_Online_PY210
"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.contents = content
        if self.contents is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def _close_tag(self):
        #
        # Closing <tag>.
        return '</{}>'.format(self.tag)

    def _open_tag(self):
        #
        # Open the opening <tag>.
        open_tag = ['<{}'.format(self.tag)]
        #
        # Write attributes.
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        #
        # Close the opening <tag>.
        open_tag.append('>')
        return ''.join(open_tag)

    def render(self, out_file, cur_ind=''):
        #
        # Check indentation.
        # next_ind = cur_ind + self.indent
        #
        # Opening <tag>.
        out_file.write(cur_ind + self._open_tag() + '\n')
        # out_file.write(self._open_tag() + '\n')
        #
        # Write the content.
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
                # content.render(out_file)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content +'\n')
        #
        # Closing </tag>.
        out_file.write(cur_ind + self._close_tag() +'\n')


class OneLineTag(Element):

    def render(self, out_file, cur_ind=''):
        #
        # Opening <tag>.
        out_file.write(cur_ind + self._open_tag())
        #
        # Write the content.
        out_file.write(self.contents[0])
        #
        # Closing </tag>.
        out_file.write(self._close_tag() + '\n')

    def append(self, content):
        raise NotImplementedError


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError('SelfClosingTag can not contain any content')
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=''):
        tag = self._open_tag()[:-1] + ' />\n'
        out_file.write(cur_ind + tag)

    def append(self, *args):
        raise TypeError('You can not add content to a SelfClosingTag')


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Body(Element):
    tag = 'body'


class Br(SelfClosingTag):
    tag = 'br'


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h' + str(level)
        super().__init__(content, **kwargs)


class Head(Element):
    tag = 'head'


class Hr(SelfClosingTag):
    tag = 'hr'


class Html(Element):
    tag = 'html'
    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind + '<!DOCTYPE html>\n')
        Element.render(self, out_file, cur_ind)


class Li(Element):
    tag = 'li'


class Meta(SelfClosingTag):
    tag = 'meta'


class P(Element):
    tag = 'p'


class Title(OneLineTag):
    tag = 'title'


class Ul(Element):
    tag = 'ul'
