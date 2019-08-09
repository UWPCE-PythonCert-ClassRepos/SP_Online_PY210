#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "Html"
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.content = [content] if content else []
        self.attributes = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def _render_open_tag(self, out_file, self_closing=False, curr_ind=''):
        #  Write the beginning of the tag
        out_file.write(curr_ind + "<{}".format(self.tag))
        for attribute, value in self.attributes.items():
            # if attributes exist (style) inject them here
            out_file.write(' "{}={}"'.format(attribute, value))
        if self_closing:
            out_file.write(">\n")
        else:
            out_file.write(">")

    def _render_close_tag(self, out_file, curr_ind='', one_line=False):
        if one_line:
            out_file.write("</{}>".format(self.tag))
        else:
            out_file.write(curr_ind + "</{}>\n".format(self.tag))

    def render(self, out_file, curr_ind=''):
        self._render_open_tag(out_file, curr_ind=curr_ind)
        out_file.write("\n")
        for line in self.content:
            try:
                out_file.write(curr_ind + self.indent + line + "\n")
            except TypeError:
                line.render(out_file, curr_ind + self.indent)
        self._render_close_tag(out_file, curr_ind=curr_ind)


class OneLineTag(Element):
    tag = 'HTML'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.content = content
        if content is None:
            self.content = []
        self.attributes = kwargs

    def render(self, out_file, curr_ind=''):
        if self.attributes is None:
            out_file.write("<{}>".format(self.tag))
        else:
            out_file.write(curr_ind + "<{}".format(self.tag))
            for attribute, value in self.attributes.items():
                out_file.write(' {}={}'.format(attribute, value))
            out_file.write(">")
        for line in self.content:
            try:
                out_file.write(line)
            except TypeError:
                line.render(out_file)
        out_file.write("</{}>\n".format(self.tag))

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError('Self closing tags are not allowed to contain content')
        super().__init__(content=content, **kwargs)

    def append(self, new_content):
        raise TypeError('Self closing tags are not allowed to contain content')

    def render(self, out_file, curr_ind=""):
        self._render_open_tag(out_file, self_closing=True, curr_ind = curr_ind)

class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(OneLineTag):
    tag = "p"


class Head(Element):
    tag = "head"


class Title(OneLineTag):
    tag = "title"


class Hr(SelfClosingTag):
    #
    tag = "hr"


class Meta(SelfClosingTag):
    #
    tag = "meta"


class Br(SelfClosingTag):
    #
    tag = "br"

class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):
    def __init__(self, size, content):
        self.tag = 'h{}'.format(size)
        super().__init__(content)



