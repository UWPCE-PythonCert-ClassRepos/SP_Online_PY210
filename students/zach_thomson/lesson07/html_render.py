#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'

    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.style = dict(kwargs)
        if content is not None:
            self.contents = [content]
        else:
            self.contents = []

    def append(self, new_content):
        self.contents.append(new_content)

    def _opentag(self):
        open_tag = ['<{}'.format(self.tag)]
        for key, value in self.style.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append('>')
        return "".join(open_tag)

    def _closetag(self):
        return "</{}>".format(self.tag)

    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind + self._opentag())
        out_file.write('\n')
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
                out_file.write("\n")
        out_file.write(cur_ind + self._closetag())
        out_file.write('\n')



class Body(Element):
    tag = 'body'


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=''):
        out_file.write("<!DOCTYPE html>\n")
        Element.render(self, out_file, cur_ind=cur_ind)


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def append(self, new_content):
        raise NotImplementedError

    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind + self._opentag())
        for content in self.contents:
            try:
                content.render(out_file, cur_ind)
            except AttributeError:
                out_file.write(content)
        out_file.write(self._closetag())
        out_file.write('\n')


class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    def render(self, out_file, cur_ind=''):
        tag = self._opentag()[:-1] + ' />\n'
        out_file.write(cur_ind + tag)

    def append(self, *args):
        raise TypeError('You can not add content to a SelfClosingTag')

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError('SelfClosingTag can not contain any content')
        super().__init__(content=content, **kwargs)


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
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class Header(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h' + str(level)
        super().__init__(content, **kwargs)

class H(Header):
    pass
