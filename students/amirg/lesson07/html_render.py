#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    #class attributes
    tag_name = 'html'
    indent = "    "

    #class initialization
    def __init__(self, content = None, **kwargs):
        if content:
            self.elements = [content]
        else:
            self.elements = []
        self.attributes = kwargs

    #adds new content to elements list
    def append(self, new_content):
        self.elements.append(new_content)

    #creates string from attribute list
    def render_atts(self):
        attribute_text = ''
        for key, value in self.attributes.items():
            attribute_text += ' {}="{}"'.format(key, value)
        return attribute_text

    #renders html text
    def render(self, out_file, cur_ind = ""):
        out_file.write(cur_ind + '<{}'.format(self.tag_name) + self.render_atts() + '>' + '\n')
        content_ind = cur_ind + self.indent
        for i in self.elements:
            if hasattr(i, 'render'):
                i.render(out_file, cur_ind + self.indent)
            else:
                out_file.write(content_ind + i)
                out_file.write('\n')
        out_file.write(cur_ind + '</{}>'.format(self.tag_name) + '\n')

'''Subclass of element'''
class Html(Element):
    tag_name = 'html'
    def render(self, out_file, cur_ind = ""):
        out_file.write(cur_ind + '<!DOCTYPE html>\n')
        super().render(out_file, cur_ind)

class Body(Element):
    tag_name = 'body'

class P(Element):
    tag_name = 'p'

class Head(Element):
    tag_name = 'head'

'''Subclass of element for one line tag'''
class OneLineTag(Element):
    def append(self, new_content):
        pass
    def render(self, out_file, cur_ind = ""):
        element_text = ''
        for i in self.elements:
            element_text += element_text + i
        out_file.write(cur_ind + '<{}'.format(self.tag_name) + self.render_atts() + '>' + element_text + '</{}>'.format(self.tag_name) + '\n')

class Title(OneLineTag):
    tag_name = 'title'

'''Self closing tag'''
class SelfClosingTag(Element):
    def append(self, new_content):
        raise TypeError('You cannot add content to SelfClosingTag')
    def render(self, out_file, cur_ind = ""):
        out_file.write(cur_ind + '<{}'.format(self.tag_name) + self.render_atts() + ' />' + '\n')

class Hr(SelfClosingTag):
    tag_name = 'hr'

class Br(SelfClosingTag):
    tag_name = 'br'

class A(OneLineTag):
    tag_name = 'a'

    #reinitializes from one line tag subclass
    def __init__(self, link, content = None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag_name = 'ul'

class Li(Element):
    tag_name = 'li'


class H(OneLineTag):
    def __init__(self, number, content = None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag_name = 'h{:.0f}'.format(number)

class Meta(SelfClosingTag):
    tag_name = 'meta'

