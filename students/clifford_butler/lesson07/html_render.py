#!/usr/bin/env python3

"""
A class-based system for rendering html.

Author: Clifford Butler
"""

# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "   "

    def __init__(self, content= None, **kwargs):
        # check if self.contents is empty
        if content == None:
            self.contents = []
        else:
            self.contents = [content]
            
        if kwargs is not None:
            self.attributes = kwargs
        else:
            self.attributes = {}

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        # loop through the list of content:
        self._open_tag(out_file,cur_ind)
        for content in self.contents:
            try:
                content.render(out_file,cur_ind + self.indent)
            except AttributeError:
                out_file.write("{}".format(cur_ind + self.indent))
                #out_file.write(content)
            out_file.write("\n")
        out_file.write("{}</{}>\n".format(cur_ind + self.indent,self.tag))
        
    def _open_tag(self,out_file,cur_ind=""):
        open_tag = ["{}<{}".format(cur_ind + self.indent,self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(" " + key + "=" + value)
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        
    def close_tag(self):
        close_tag = "</{}>".format(self.tag)
        return close_tag
        
    def get_attributes(self):
        attribute = [self.tag]

        if self.attributes is not None:
            attribute.extend([f"{k}=\"{v}\"" for k, v in self.attributes.items()])

        return " ".join(attribute)        
class SimpleElement(Element):
    def render(self, out_file, current_ind=""):
        out_file.write(current_ind)
        self.open_tag(out_file)
        out_file.write('>')
        out_file.write((self.content[0]))
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError
        
class SelfClosingElement(SimpleElement):
    def __init__(self, **kwargs):
        self.attributes = kwargs

class Body(Element):
    tag = "body"
    
class Html(Element):
    tag = "html"
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)  
    
class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"
    
class OneLineTag(Element):
    # loop through the list of contents:
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.open_tag())
        out_file.write(self.content[0])
        out_file.write(self.close_tag())   
    def append(self, content):
        raise NotImplementedError
        
class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag cannot contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.open_tag()[:-1] + " />\n")

    def append(self, *args):
        raise TypeError("You cannot add content to a SelfClosingTag")
        
class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"
    
class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"    
    
class Title(OneLineTag):
    tag = "title"
    

class A(Element):
    tag = "a"
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class H(OneLineTag):
    tag = "h"
    def __init__(self, level, content=None, **kwargs):
        self.tag = '{}{}'.format(self.tag, level)
        super().__init__(content, **kwargs)
        
class Meta(SelfClosingTag):
    tag = "meta"
    
