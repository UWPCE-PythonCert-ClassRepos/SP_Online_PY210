#!/usr/bin/env python3
#-------------------------------------------#
#Tittle: html_render,py, PYTHON210 - Assignment 6: 
#Desc: HTML Renderer
#Change Log: (Who, When, What)
#Brent Kieszling, <2021-Jan-2>, Imported file, Updated Element

#-------------------------------------------#
"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        
        self.attributes = {**kwargs}

    def append(self, new_content):
        self.content.append(new_content)
        
    def _open_tag(self):
        atts = [("<{}").format(self.tag)]
        for key, value in self.attributes.items():
             atts.append('{}="{}"'.format(key,value))
        wrap_tag = (" ".join(atts))
        wrap_tag += ">\n"
        return wrap_tag

    def _close_tag(self):
        close = "</{}>".format(self.tag)
        return close

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        for item in self.content:
            try:
                item.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent)
                out_file.write(item)
            out_file.write("\n")
        out_file.write(cur_ind)
        out_file.write(self._close_tag())
        

class Html(Element):
    tag = "html"
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<!DOCTYPE html>")
        out_file.write("\n")
        super().render(out_file, cur_ind)
    
class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"
    
class Head(Element):
    tag = "head"
    
class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(self._open_tag()[:-1])
        out_file.write(self.content[0])
        out_file.write(self._close_tag())
    def append(self, *args):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        tag = self._open_tag()[:-2] + " />"
        out_file.write(tag)
        
    def append(self, *args):
        raise TypeError("You can't add content to the SelfClosingTag")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class Meta(SelfClosingTag):
    tag = 'meta charset="UTF-8"'

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
    tag = "h"
    def __init__(self, level, content=None, **kwargs):
        self.tag += (str(level))
        super().__init__(content=content, **kwargs)
    
    