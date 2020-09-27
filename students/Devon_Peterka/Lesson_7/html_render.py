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

    def _open_tag(self):
        open_tag = f'<{self.tag}'
        for key, value in self.attributes.items():
            open_tag += f' {key}="{value}"'
        return open_tag + ('>\n')

    def _close_tag(self):
        return f'</{self.tag}>\n'

    def render(self, out_file):
        out_file.write(self._open_tag())
        for content in self.content:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write('\n')
        out_file.write(self._close_tag())

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
        out_file.write(self._open_tag()[:-1])
        out_file.write(' '.join(self.content))
        out_file.write(self._close_tag())

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    def __init__(self, **kwargs):
        self.attributes = kwargs.copy()

    def render(self, out_file):
        out_file.write(self._open_tag()[:-2] + ' />\n')

class Hr(SelfClosingTag):
    tag = 'hr'
    

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)
