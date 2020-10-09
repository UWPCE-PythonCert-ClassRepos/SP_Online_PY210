#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

""" 
belarson (note: pytest)
run results:
1. Issue in title with extra begin tag:  <title>        <title>PythonClass = Revision 1087:</title>
   Would advise adding text to look for single tag
   Title is OneLineTag.  Checking others using that (anchor, header). 
   Found issue with anchor too in run 6: <a href="http://google.com">        <a href="http://google.com">link</a>
   Found issue with header in run 7: <h2>        <h2>PythonClass - Class 6 example</h2>
   
Resolved: class OneLineTag was writing tag twice
"""
# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        return "".join(open_tag)

    def _close_tag(self):
        return "</{}>".format(self.tag)

    def render(self, out_file, cur_ind=""):

        new_indent = cur_ind + self.indent
        out_file.write(cur_ind+self._open_tag())
        out_file.write("\n")

        for content in self.contents:
            try:
                content.render(out_file, cur_ind=new_indent)
            except AttributeError:
                out_file.write(new_indent + content)
            out_file.write("\n")
        out_file.write(cur_ind + self._close_tag())


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<!DOCTYPE html>\n")
        Element.render(self, out_file, cur_ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):
        # oops, only need this one time. Fixed 9/25/2020
        # out_file.write(cur_ind + self._open_tag())
        out_file.write(cur_ind+self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, outfile, cur_ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        outfile.write(cur_ind + tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs["href"] = link
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):
    base_tag = "h"

    def __init__(self, level, content=None, **kwargs):
        self.tag = self.base_tag + str(level)
        super().__init__(content, **kwargs)


class Meta(Element):
    tag = "meta "

    def render(self, out_file, cur_ind=""):

        out_file.write(cur_ind + "<{}".format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file, cur_ind)
            except AttributeError:
                out_file.write(content)
        out_file.write("</>")
        out_file.write('\n')
