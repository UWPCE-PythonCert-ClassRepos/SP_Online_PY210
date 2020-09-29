#!/usr/bin/env python

import copy
"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag="html"
    indent = "    "
    def __init__(self, content=None, **kwargs):
        self.kwargs = kwargs 
        self.contents=[]
        if content is not None:
            self.contents= [content]
    def append(self, n_content):
        self.contents.append(n_content)

    def _open_tag(self,out_file):
        open_tag = ["<{}".format(self.tag)]
        for key in self.kwargs:
            open_tag.append(" " + key + "=" + '"'+ str(self.kwargs[key]) + '"')
        out_file.write("".join(open_tag))

    def render(self, out_file,cur_ind=""):
        open_tag = ["<{}>".format(self.tag)]
        #open_tag.append(">\n")
        for key in self.kwargs:
            open_tag.append(" " + key + "=" + str(self.kwargs[key]))
        out_file.write("".join(open_tag))
        for content in self.contents:
            try:
                content.render(out_file,cur_ind+self.indent)
            except AttributeError:
                    out_file.write("{}".format(cur_ind + self.indent))
                    out_file.write(content)
        out_file.write("</{}>\n".format(self.tag))

class Html(Element):
    tag="html"
    indind=0
    
    def render(self,out_file,cur_ind=""):
        self.cur_ind=cur_ind+str(self.indent*self.indind)
        #self.contents.insert(0,'<!DOCTYPE html>\n')
        open_tag = ["<{}>\n".format(self.tag)]
        out_file.write("".join('<!DOCTYPE html>\n'))
        out_file.write("".join(open_tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write("{}".format(cur_ind + self.indent))
                out_file.write(content)
                out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))



class Body(Element):
    tag="body"
class P(Element):
    tag="p"
class Head(Element):
    tag="head"

class OneLineTag(Element):
    def render(self,out_file,cur_ind=""):
            out_file.write("<{}>".format(self.tag))
            out_file.write(self.contents[0])
            out_file.write("</{}>\n".format(self.tag))
    def append(self,content):
        raise NotImplementedError

class Title(OneLineTag):
    tag="title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        self.content = []
        self.kwargs = kwargs
        if content is not None:
            raise TypeError("SelfClosing can not contain any content")
        super().__init__(content=content,**kwargs)
    def append(self,content):
        raise TypeError("You can not add content to selfclosingtag")

    def render(self,out_file,cur_ind=''):
        self._open_tag(out_file)
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(" />\n")

class Hr(SelfClosingTag):
    tag="hr"

class Br(SelfClosingTag):
    tag="br"

class Meta(SelfClosingTag):
    tag='meta charset="UTF-8"'

class A(OneLineTag):
    tag='a href'
    def __init__(self,link,content=None,**kwargs):
        #kwargs['href']=link
        super().__init__(content,**kwargs)
class Ul(Element):
    tag="ul"

class Li(Element):
    tag="li"

class H(OneLineTag):
    tag="h"
    def __init__(self,head_no,content=None,**kwargs):
        self.tag=self.tag + str(head_no)
        super().__init__(content,**kwargs)
    


#Element([])
