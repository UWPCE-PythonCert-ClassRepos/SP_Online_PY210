#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    indent = 4
    tag = 'html'
    kwargs = {}

    def __init__(self, content=None, **kwargs):
        self.kwargs = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render_opening(self, out_file, tag_close, cur_ind=0):
        out_file.write((cur_ind * ' ' + '<{}').format(self.tag))
        for key, value in self.kwargs.items():
            out_file.write(' {}="{}"'.format(key, value))
        if type(self.contents) == str:
            out_file.write('>{}<'.format(self.contents))
        else:
            pass
        out_file.write(tag_close)

    def render(self, out_file, cur_ind=0):
        self.render_opening(out_file, '>\n')
        cur_ind += self.indent
        for content in self.contents:
            try:
                out_file.write(cur_ind * ' ')
                out_file.write(content)
            except TypeError:
                content.render(out_file, cur_ind)
            out_file.write('\n')
        out_file.write(((cur_ind - self.indent) * ' ' + '</{}>').format(self.tag))


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=0):
        out_file.write('<!DOCTYPE html>\n')
        Element.render(self, out_file)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file, cur_ind=0):
        Element.render_opening(self, out_file, '>')
        for content in self.contents:
            try:
                out_file.write(content)
            except TypeError:
                print('Appending elements within this tag type not allowed.')
                raise
        out_file.write('</{}>'.format(self.tag))


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, out_file, cur_ind=0):
        if self.contents != []:
            raise TypeError('Element may not have content')
        else:
            Element.render_opening(self, out_file, ' />')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(Element):
    tag = 'a'

    def __init__(self, link, content):
        self.kwargs = {'href': link}
        self.contents = content
        
    def render(self, out_file, cur_ind=0):
        Element.render_opening(self, out_file, '/{}>'.format(self.tag))
    
class Ul(Element):
    tag = 'ul'
    

class Li(Element):
    tag = 'li'
    
    
class H(OneLineTag):
    def __init__(self, level, content):
        self.tag = 'h{}'.format(str(level))
        self.contents = [content]
        
        
class Meta(SelfClosingTag):
    tag = 'meta'