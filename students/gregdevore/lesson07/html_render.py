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

    def render_open_tag(self, out_file):
        # Write opening tag, then attributes, then close it
        out_file.write('<{}'.format(self.tag))
        for attribute, value in self.attributes.items():
            out_file.write(' {}=\"{}\"'.format(attribute, value))
        out_file.write('>')

    def render(self, out_file):
        self.render_open_tag(out_file)
        out_file.write('\n')
        for line in self.content:
            try:
                out_file.write(line + '\n')
            except TypeError:
                line.render(out_file)
        out_file.write('</{}>\n'.format(self.tag))

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
        self.render_open_tag(out_file)
        out_file.write('{} </{}>\n'.format(self.content[0], self.tag))

class Title(OneLineTag):
    tag = 'title'
