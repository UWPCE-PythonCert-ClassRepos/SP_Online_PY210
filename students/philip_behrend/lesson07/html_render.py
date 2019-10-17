#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'
    ind = "    "

    def __init__(self, content="", **kwargs):
        self.content = [content]
        self.kwargs = kwargs

    def append(self, new_content):
        self.content.append(new_content)


    def render(self, out_file, cur_ind = ""):
        out_file.write("{}<{} ".format(cur_ind,self.tag))
        for key, value in self.kwargs.items():
            out_file.write("{}=\"{}\"".format(key, value))
        out_file.write(">\n")
        for item in self.content:
            try:
                item.render(out_file,cur_ind+self.ind)
            except AttributeError:
                out_file.write(cur_ind+self.ind)
                out_file.write(item)
                out_file.write("\n")
            out_file.write(cur_ind)
            out_file.write("</{}>\n".format(self.tag))

class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind = ""):
        out_file.write("<!DOCTYPE html>\n") 
        out_file.write(self.ind)
        out_file.write("<{} ".format(self.tag))
        for key, value in self.kwargs.items():
            out_file.write("{}=\"{}\"".format(key, value))
        out_file.write(">\n")
        for item in self.content:
            try:
                item.render(out_file, cur_ind+self.ind)
            except AttributeError:
                out_file.write(item)
                out_file.write("\n")
        out_file.write(cur_ind)
        out_file.write("</{}>\n".format(self.tag))


class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

    def render(self, out_file, cur_ind = ""):
        out_file.write("<{}>\n".format(self.tag))
        Meta(charset="UTF-8").render(out_file)
        for item in self.content:
            try:
                item.render(out_file, cur_ind+self.ind)
            except AttributeError:
                out_file.write(cur_ind)
                out_file.write(item)
        out_file.write("\n</{}>\n".format(self.tag))


class OneLineTag(Element):
    tag = 'title'

    def render(self, out_file, cur_ind = ""):
        out_file.write("<{}> ".format(self.tag))
        for item in self.content:
            try:
                item.render(out_file)
            except AttributeError:
                out_file.write(cur_ind)
                out_file.write(item)
        out_file.write(" </{}>\n".format(self.tag))

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    tag = 'hr'

    def __init__(self, content=None, **kwargs):
        self.content = content
        if self.content is not None:
            raise TypeError
        self.kwargs = kwargs


    def render(self,out_file,cur_ind=""):
        out_file.write("<{} ".format(self.tag))
        if self.kwargs != {}:
            for key, value in self.kwargs.items():
                out_file.write(cur_ind)
                out_file.write("{}=\"{}\"".format(key, value))
        out_file.write(" />\n")

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(Element):
    tag = 'a'
    def __init__(self, link="",content=""):
        self.link = link
        self.content = content

    def render(self, out_file, cur_ind = ""):
        out_file.write(cur_ind)
        out_file.write("<{} href={}>".format(self.tag,self.link))
        out_file.write("{}</{}>\n".format(self.content,self.tag))

class Ul(Element):
    tag = 'ul'

class Li(OneLineTag):
    tag = 'li'

class H(OneLineTag):
    tag = 'h'

    def __init__(self, level = "", content = ""):
        self.level = level
        self.content = content

    def render(self, out_file, cur_ind = ""):
        out_file.write("<{}{}>".format(self.tag,self.level))
        for item in self.content:
            try:
                item.render(out_file)
            except AttributeError:
                out_file.write(cur_ind)
                out_file.write(item)
        out_file.write(" </{}{}>\n".format(self.tag,self.level))

class Meta(SelfClosingTag):
    tag = 'meta'











####Example KWARG function for reference. Please ignore for grading 
def func(fore_color='na',back_color='na',link_color='na',visited_color='na'):
    return fore_color, back_color, link_color, visited_color

func('red', 'blue', 'yellow', 'chartreuse')
func(link_color='red', back_color='blue')
func('purple', link_color='red', back_color='blue')
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
func(*regular, **links)

def func_arg(*args, **kwargs):
    return args, kwargs
func_arg('red', 'blue', 'yellow', 'chartreuse')
func_arg(link_color='red', back_color='blue')
func_arg('purple', link_color='red', back_color='blue')
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
func_arg(*regular, **links)

