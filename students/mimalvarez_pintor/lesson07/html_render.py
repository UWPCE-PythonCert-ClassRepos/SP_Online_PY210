#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""
import pytest
# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = '    '


    def __init__(self, content=None, **kwargs):
        self.content = []
        if content:
            self.append(content)
        self.attributes = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def _open_tag(self, cur_ind=''):
        open_tag = ['{}<{}'.format(cur_ind, self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append('>')
        open_tag = "".join(open_tag)
        return open_tag

    def _close_tag(self, cur_ind=''):
        return '{}</{}>'.format(cur_ind, self.tag)

    def render(self, file_out, cur_ind = ''):
        file_out.write(self._open_tag(cur_ind))
        file_out.write('\n')
        for content in self.content:
            try:
                content.render(file_out, cur_ind + self.indent)
            except AttributeError:
                file_out.write(cur_ind + self.indent + content)
                file_out.write('\n')
        file_out.write(self._close_tag(cur_ind))
        file_out.write('\n')

class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind = ''):
        file_out.write('<!DOCTYPE html>\n')
        super().render(file_out, cur_ind='')

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'     

class OneLineTag(Element):

    def render(self, file_out, cur_ind=''):
        file_out.write("<{}>".format(self.tag))
        file_out.write(self.contents[0])
        file_out.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError('SelfClosingTag can not contain any content')
        super().__init__(content=content, **kwargs)

    def render(self, file_out, cur_ind=''):
        tag = self._open_tag()[:-1] + ' />\n'
        file_out.write(cur_ind)
        file_out.write(tag)

    def append(self, *args):
        raise TypeError('You can not add content to a SelfClosingTag')

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class Meta(SelfClosingTag):
    tag = 'meta'

class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content,**kwargs)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h{}'.format(level)
        super().__init__(content, **kwargs)
