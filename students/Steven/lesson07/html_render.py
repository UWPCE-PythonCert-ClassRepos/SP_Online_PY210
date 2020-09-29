#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.attributes = kwargs
        if content is not None:
            self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind + self.open_tag() + "\n")  # Beginning tag

        # Looping through the list of "content"
        for contents in self.content:
            try:
                contents.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + contents)
            out_file.write("\n")  # New line after before closing tag
        out_file.write(cur_ind + self.close_tag())  # Closing tag

    def open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(" {}='{}'".format(key, value))
        open_tag.append('>')
        return ''.join(open_tag)

    def close_tag(self):
        close_tag = '</{}>'.format(self.tag)
        return close_tag

class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    # Overwriting the render method from Element
    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind + self.open_tag())  # creates HTML tag
        out_file.write(self.content[0])  # Title tag
        out_file.write(self.close_tag())  # closes HTML tag

    def append(self, content):
            raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can't contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, outfile, cur_ind=''):
        tag = self.open_tag()[:-1] + " />\n"
        outfile.write(tag)

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
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
    def __init__(self, level, content=None, **kwargs):
        self.tag = "h{}".format(level)
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"