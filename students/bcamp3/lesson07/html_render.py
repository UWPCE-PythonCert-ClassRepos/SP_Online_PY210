#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.content = [content] if content else []
        self.attributes = kwargs

    def append(self, new_content):
        if hasattr(new_content, 'render'):
            self.content.append(new_content)
        else:
            self.content.append(TextWrapper(str(new_content)))

    def render(self, out_file, cur_ind=''):
        self._open(out_file, cur_ind=cur_ind)
        out_file.write('\n')
        for line in self.content:
            if hasattr(line, 'render'):
                line.render(out_file, cur_ind + self.indent)
            else:
                out_file.write(cur_ind + self.indent + line + '\n')
        self._close(out_file, cur_ind=cur_ind)

    def _open(self, out_file, cur_ind='', self_closing=False):
        out_file.write(cur_ind + f'<{self.tag}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}=\"{value}\"')
        if self_closing:
            out_file.write(' />\n')
        else:
            out_file.write('>')

    def _close(self, out_file, cur_ind='', one_line_tag=False):
        if one_line_tag:
            out_file.write(f'</{self.tag}>\n')
        else:
            out_file.write(cur_ind + f'</{self.tag}>\n')


class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text.
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, cur_ind=''):
        file_out.write(cur_ind + self.text + '\n')


class Html(Element):
    tag = 'html'
    def render(self, out_file, cur_ind=''):
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file, cur_ind=cur_ind)

    def _close(self, out_file, cur_ind='', one_line_tag=False):
        out_file.write(cur_ind + f'</{self.tag}>')

class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    tag = 'OneLineTag'
    # Make sure append cannot be used
    def append(self, new_content):
        raise TypeError('One line tags are not allowed to add content')

    # Override render method to print a single line
    def render(self, out_file, cur_ind=''):
        """
        Render single line tag.
        """
        self._open(out_file, cur_ind=cur_ind)
        out_file.write(f'{self.content[0]}')
        self._close(out_file, cur_ind=cur_ind, one_line_tag=True)


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    tag = 'SelfClosingTag'

    def __init__(self, content=None, **kwargs):
        super().__init__(None, **kwargs)

    # Make sure append cannot be used
    def append(self, new_content):
        raise NotImplementedError

    def render(self, out_file, cur_ind=''):
        self._open(out_file, cur_ind=cur_ind, self_closing=True)


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    tag = 'a'
    def __init__(self, link=None, content=None, **kwargs):
        super().__init__(content, href=link)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, num, content=None):
        self.tag = f'h{num:d}'
        super().__init__(content)


class Meta(SelfClosingTag):
    tag = 'meta'
