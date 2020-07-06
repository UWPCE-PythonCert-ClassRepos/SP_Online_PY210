#!/usr/bin/env python3

#Mark McDuffie
#6/8/2020
#html render

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.content = []
        if content:
            self.content = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file, cur_ind = ''):
        out_file.write(cur_ind + self.open_tag() + '\n')
        for content in self.content:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content + '\n')
        out_file.write(cur_ind + self.close_tag() + '\n')

    def open_tag(self):
        open_tag = ['<{}'.format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        return "".join(open_tag) + '>'

    def close_tag(self):
        return "</{}>".format(self.tag)

class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=''):
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file, cur_ind='')

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    def render(self, out_file, cur_ind =''):
        out_file.write(cur_ind + self.open_tag())
        out_file.write(self.content[0])
        out_file.write(self.close_tag() + '\n')

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError("Self-Closing Tag should not contain any content")
        super().__init__(content = content, **kwargs)
    def render(self, out_file, cur_ind=''):
        tag = self.open_tag()[:-1] + ' />\n'
        out_file.write(cur_ind + tag)
    def append(self, *args):
        raise TypeError("You should not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = "h{}".format(level)
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = 'meta'