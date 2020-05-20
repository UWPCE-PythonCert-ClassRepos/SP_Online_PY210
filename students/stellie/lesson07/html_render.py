#!/usr/bin/env python3

# Stella Kim
# Assignment 5: HTML Renderer Exercise

"""
A class-based system for rendering HTML.
"""


# Base class framework
class Element(object):
    tag_name = 'html'
    indent = '   '

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    # Place attributes in an element's tag
    def _open_tag(self):
        open_tag = ['<{}'.format(self.tag_name)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append('>\n')
        return ''.join(open_tag)

    def _close_tag(self):
        return '</{}>\n'.format(self.tag_name)

    def render(self, out_file, cur_ind=''):
        new_ind = cur_ind + self.indent
        out_file.write(cur_ind + self._open_tag())
        for content in self.contents:   # loop through list of contents
            try:
                content.render(out_file, cur_ind=new_ind)
            except AttributeError:
                out_file.write(new_ind + content)
            out_file.write('\n')
        out_file.write(cur_ind + self._close_tag())


class Html(Element):
    tag_name = 'html'

    def render(self, out_file, cur_ind=''):
        # Place doctype tag at the top of page
        out_file.write(cur_ind + '<!DOCTYPE html>\n')
        super().render(out_file, cur_ind)


class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'


class Head(Element):
    tag_name = 'head'


# One line tags such as links
class OneLineTag(Element):
    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind)
        out_file.write(self._open_tag()[:-1])
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag_name = 'title'


# Self closing tags such as <hr /> and <br />
class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError('You can not add content to a SelfClosingTag')
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError('You can not add content to a SelfClosingTag')

    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind)
        tag = self._open_tag()[:-2] + ' />\n'
        out_file.write(tag)


class Hr(SelfClosingTag):
    tag_name = 'hr'


class Br(SelfClosingTag):
    tag_name = 'br'


class A(OneLineTag):
    tag_name = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul(Element):
    tag_name = 'ul'


class Li(Element):
    tag_name = 'li'


class Header(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag_name = 'h{}'.format(level)
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    tag_name = 'meta'
