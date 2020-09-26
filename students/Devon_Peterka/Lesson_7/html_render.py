#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.content = [] if content is None else [content]
        self.attributes = kwargs.copy()
       # print(self.attributes)

    def append(self, new_content):
        self.content.append(new_content)

    def _open_tag(self, out_file):
        pass

    def _close_tag(self, out_file):
        pass

    def render(self, out_file):
        out_file.write(f'<{self.tag}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write('>\n')
        for content in self.content:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write('\n')
        out_file.write(f'</{self.tag}>\n')

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    def render(self, out_file):
        out_file.write(f'<{self.tag}> ')
        out_file.write(' '.join(self.content))
        out_file.write(f' </{self.tag}>\n')

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    def render(self, out_file):
        out_file.write(f'<{self.tag}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(' />\n')

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'
