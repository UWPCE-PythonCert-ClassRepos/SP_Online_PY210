#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.content = [content] if content else []
        self.attributes = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def _render_open_tag(self, out_file, self_closing=False):
        # Write opening tag, then attributes, then close it
        out_file.write('<{}'.format(self.tag))
        for attribute, value in self.attributes.items():
            out_file.write(' {}=\"{}\"'.format(attribute, value))
        if self_closing:
            out_file.write(' />\n')
        else:
            out_file.write('>')

    def _render_close_tag(self, out_file):
        out_file.write('</{}>\n'.format(self.tag))

    def render(self, out_file):
        self._render_open_tag(out_file)
        out_file.write('\n')
        for line in self.content:
            try:
                out_file.write(line + '\n')
            except TypeError:
                line.render(out_file)
        self._render_close_tag(out_file)

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    # Make sure append cannot be used
    def append(self, new_content):
        raise NotImplementedError
    # Override render method to print to a single line
    def render(self, out_file):
        self._render_open_tag(out_file)
        out_file.write('{}'.format(self.content[0]))
        self._render_close_tag(out_file)

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError('Self closing tags are not allowed to contain content')
        super().__init__(content=content, **kwargs)

    def append(self, new_content):
        raise TypeError('Self closing tags are not allowed to contain content')

    def render(self, out_file):
        self._render_open_tag(out_file, self_closing=True)

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)
