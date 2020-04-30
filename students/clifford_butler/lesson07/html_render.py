#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

import copy

# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content= None, **kwargs):
        # check if self.contents is empty
        if content == None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = copy.deepcopy(kwargs)
            
    def attributes(self, outfile):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(key + "=" + value)
        open_tag.append(">\n")
        out_file.write("".join(open_tag))

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        # loop through the list of contents:
        #self.attributes(out_file)
        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            #out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))
    

class Body(Element):
    tag = "body"
    
class Html(Element):
    tag = "html"
    
class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"
    
class OneLineTag(Element):
    # loop through the list of contents:
    def render(self, out_file):
        #self.attributes(out_file)
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
    def append(self, content):
        raise NotImplementedError
        
class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("not allowed content")
        super().__init__(content=content,**kwargs)
        
    def render(self, out_file):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes:
            open_tag.append(key + "=" + value)
        open_tag.append(" />\n")
        out_file.write("".join(open_tag))
        
class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"
    
#class Title(Element):
    tag = "title"
    
class Title(OneLineTag):
    tag = "title"

class title(OneLineTag):
    tag = "title"
    
