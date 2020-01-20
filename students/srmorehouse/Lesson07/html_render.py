#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = '   '
    
    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs if kwargs is not None else {}
        self.contents = [content] if content is not None else []

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        open_tag = ['<{}'.format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(f' {key}="{value}"')
        open_tag.append('>')           
        return ''.join(open_tag)

    def _close_tag(self):
        return '</{}>'.format(self.tag)
        
    def render(self, out_file, ind=''):
        # loop through the list of contents
        open_tag = [ind]
        open_tag.append(self._open_tag())
        open_tag.append('\n')
        out_file.write(''.join(open_tag))
        for content in self.contents:
            if hasattr(content, 'render'):
                content.render(out_file, ind=self.indent + ind)
            else:
                out_file.write(f'{self.indent + ind}{content}\n')
        out_file.write(f'{ind}')
        out_file.write(self._close_tag())
        out_file.write('\n')
        
# class Text(Element):
#     content = []
#     tag = ''
# 
#     def render(self, out_file):
        # for content in self.content:
        #     if len(tag) == 0: content
        #     out_file.write(content)


class Html(Element):
    tag = 'html'

    def _open_tag(self):
        return '<!DOCTYPE html>\n' + super()._open_tag()


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file, ind=''):
        out_file.write(ind)
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
        out_file.write('\n')

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    self_closing_typeerror = TypeError('SelfClosingTag can not contain any content')

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise self.self_closing_typeerror
        super().__init__(content=content, **kwargs)

    def render(self, out_file, ind=''):
        out_file.write(ind)
        tag = self._open_tag()[:-1] + ' />\n'
        out_file.write(tag)
    
    def append(self, *args):
        raise self.self_closing_typeerror


class Hr (SelfClosingTag):
    tag = 'hr'


class Br (SelfClosingTag):
    tag = 'br'


class Meta (SelfClosingTag):
    tag = 'meta'


class A (OneLineTag):
    tag = 'a'
    
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul (Element):
    tag = 'ul'


class Li (Element):
    tag = 'li'


class H (OneLineTag):
    tag = 'h'

    def __init__(self, level, content=None, **kwargs):
        self.tag = f'{self.tag}{level}'
        super().__init__(content, **kwargs)
