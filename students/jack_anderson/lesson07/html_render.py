#!/usr/bin/env python3
"""
Jack Anderson
03/01/2020
UW PY210
Lesson 07
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    indent = "    "

    tag = "html"


    def __init__(self, content=None, **kwargs):
        self.attribs = dict()
        for k, v in kwargs.items():
            self.attribs[k] = v
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(f"<{self.tag}")
        if len(self.attribs.items()) > 0:
            for k, v in self.attribs.items():
                out_file.write(f' {k}="{v}"')
        out_file.write(">\n")
        for content in self.contents:

            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(self.indent + cur_ind)
                out_file.write(content)
                out_file.write("\n")
        out_file.write(cur_ind)
        out_file.write(f"</{self.tag}>\n")



class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(f"<{self.tag}")
        for k, v in self.attribs.items():
            out_file.write(f' {k}="{v}"')
        out_file.write(">")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(content)
        out_file.write(f"</{self.tag}>")
        out_file.write("\n")

    def append(self, new_content):
        raise NotImplementedError


class SelfClosingTag(Element):

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(f"<{self.tag}")
        if len(self.attribs.items()) > 0:
            for k, v in self.attribs.items():
                out_file.write(f' {k}="{v}"')
        out_file.write(" />\n")


    def append(self, new_content):
        raise TypeError




class A(OneLineTag):

    tag = 'a'

    def __init__(self, link, content):
        x = link
        self.attribs = dict()
        self.attribs['href']= link
        self.contents = [content]



class Title(OneLineTag):
    tag = 'title'

class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'

class Body(Element):
    tag = 'body'

class Html(Element):
    tag = 'html'

    doc_tag = "<!DOCTYPE html>\n"

    def render(self, out_file, cur_ind=""):
        out_file.write(self.doc_tag)
        Element.render(self, out_file, cur_ind)


class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class Ul(Element):
    tag = "ul"

    def __init__(self, **kwargs):
        self.attribs = dict()
        self.contents = []
        for key, value in kwargs.items():
            self.attribs[key] = value

    def append(self, content):
        self.contents.append(content)


class Li(Element):
    tag = "li"


class H(OneLineTag):

    def __init__(self, size, content):
        try:
            header_size = int(size)
        except:
            raise ValueError

        self.attribs = dict()
        self.contents = [content]
        self.tag = f'h{header_size}'



class Meta(SelfClosingTag):
    tag = 'meta'