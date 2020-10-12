#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "   "

    def __init__(self, content=None, **kwargs):
        self.kwargs = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.kwargs.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        return ''.join(open_tag)

    def _close_tag(self):
        close_tag = "</{}>\n".format(self.tag)
        return close_tag

    def render(self, out_file, cur_indent=""):
        # loop through the list of contents:
        out_file.write(cur_indent)
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_indent + self.indent)
            except AttributeError:
                out_file.write(cur_indent + self.indent)
                out_file.write(content)
                out_file.write("\n")
        out_file.write(cur_indent)
        out_file.write(self._close_tag())

class Body(Element):
    tag = "body"

class Html(Element):
    tag = "html"

    def render(self, out_file, cur_indent=""):
        out_file.write(cur_indent)
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file, cur_indent)

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):

    def render(self, out_file, cur_indent=""):
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
    
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, outfile, cur_indent=""):
        tag = self._open_tag()[:-1] + " />\n"
        outfile.write(tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class Meta(SelfClosingTag):
    tag = "meta"

class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Li(Element):
    tag = "li"

class Ul(Element):
    tag = "ul"

class H(OneLineTag):
    tag = "h"

    def __init__(self, level="", content=None, **kwargs):
        if level is not None:
            self.tag += str(level)
        super().__init__(content, **kwargs)
