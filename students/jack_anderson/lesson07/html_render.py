#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

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
        new_line = "\n"
        self.contents.append(new_content)
       # self.contents.append(new_line)

    def render(self, out_file):
        out_file.write(f"<{self.tag}")
        if len(self.attribs.items()) > 0:
            for k, v in self.attribs.items():
                out_file.write(f' {k}="{v}"')
        out_file.write(">\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(f"</{self.tag}>\n")


    #
    # def list_attributes(self, out_file):
    #     out_file.write(f"<{self.tag}")
    #     if len(self.attribs.items()) > 0:
    #         for k, v in self.attribs.items():
    #             out_file.write(f' {k}="{v}"')



class OneLineTag(Element):

    def render(self, out_file):
        out_file.write(f"<{self.tag}")
        if len(self.attribs.items()) > 0:
            for k, v in self.attribs.items():
                out_file.write(f' {k}="{v}"')
        out_file.write(">")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(f"</{self.tag}>")
        out_file.write("\n")

    def append(self, new_content):
        raise NotImplementedError


class SelfClosingTag(Element):

    def render(self, out_file):
        out_file.write(f"<{self.tag}")
        if len(self.attribs.items()) > 0:
            for k, v in self.attribs.items():
                out_file.write(f' {k}="{v}"')
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(" />\n")



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

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

