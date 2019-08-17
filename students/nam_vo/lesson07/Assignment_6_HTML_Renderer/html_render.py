#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, cur_ind=''):
        # add indentation
        if cur_ind:
            file_out.write(cur_ind)
        file_out.write(self.text)
        file_out.write('\n')

# This is the framework for the base class
class Element(object):
    # Class attribute
    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = kwargs

    def append(self, content):
        if hasattr(content, 'render'):
            self.contents.append(content)
        else:
            self.contents.append(TextWrapper(str(content)))
            
    def _open_tag(self):
        # loop through the list of attributes:
        open_tag = ['<{}'.format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append('>')
        return ''.join(open_tag)

    def _close_tag(self):
        return '</{}>'.format(self.tag)

    def render(self, out_file, cur_ind=''):
        # add indentation
        if cur_ind:
            out_file.write(cur_ind)
        # loop through the list of attributes:
        out_file.write(self._open_tag())
        out_file.write('\n')
        # loop through the list of contents:
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent)
                out_file.write('{}\n'.format(content))
        # add indentation
        if cur_ind:
            out_file.write(cur_ind)
        # Close tag
        out_file.write(self._close_tag())
        out_file.write('\n')

class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=''):
        out_file.write('<!DOCTYPE html>\n')
        Element.render(self, out_file)
        
class Body(Element):
    tag = 'body'

    def render(self, out_file, cur_ind=''):
        Element.render(self, out_file, '    ')
        
class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

    def render(self, out_file, cur_ind=''):
        Element.render(self, out_file, '    ')
        
class OneLineTag(Element):

    def append(self, new_content):
        raise NotImplementedError

    def _open_tag(self):
        # loop through the list of attributes:
        open_tag = ['<{}'.format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append('>')
        return ''.join(open_tag)

    def _close_tag(self):
        return '</{}>'.format(self.tag)

    def render(self, out_file, cur_ind=''):
        # add indentation
        if cur_ind:
            out_file.write(cur_ind)
        # loop through the list of attributes:
        out_file.write(self._open_tag())
        # loop through the list of contents:
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write('{}'.format(content))
        # Close tag
        out_file.write(self._close_tag())
        out_file.write('\n')

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, out_file, cur_ind=''):
        # add indentation
        if cur_ind:
            out_file.write(cur_ind)
        tag = self._open_tag()[:-1] + ' />\n'
        out_file.write(tag)

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs = {'href': link}
        super().__init__(content=content, **kwargs)
 
class Ul(Element):
    tag = 'ul'
   
class Li(Element):
    tag = 'li'
   
class H(OneLineTag):
    tag = 'h'

    def __init__(self, level=1, content=None, **kwargs):
        self.tag = 'h{}'.format(level)
        super().__init__(content=content, **kwargs)

class Meta(SelfClosingTag):
    tag = 'meta'
