#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = ""
    
    def __init__(self, content = None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
            
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)
        
    def _open_tag(self, additions = ""):
        
        open_string = "<{}".format(self.tag)
        for key, value in self.attributes.items():
            open_string = open_string + (' {}="{}"'.format(key, value))
        open_string = open_string + additions
        open_string = open_string + ">"
        
        return open_string
    
#        out_file.write("<{}".format(self.tag))
#        #print any style
#        for key, value in self.attributes.items():
#            out_file.write(' {}="{}"'.format(key, value))
#        #close first line
#        out_file.write(additions)
#        out_file.write(">\n")
        
    def _closed_tag(self):
        return "</{}>".format(self.tag)
        
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self._open_tag())
        out_file.write("\n")
        
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(cur_ind + content)
                out_file.write("\n")
        out_file.write(cur_ind + self._closed_tag())
        out_file.write("\n")
        
        
        
#    def render(self, out_file):
#        #print tag
#        out_file.write("<{}".format(self.tag))
#        #print any style
#        for key, value in self.attributes.items():
#            out_file.write(' {}="{}"'.format(key, value))
#        #close first line
#        out_file.write(">\n")
#
#        # loop through the list of contents:
#        for content in self.contents:
#            try:
#                content.render(out_file)
#            except AttributeError:
#                out_file.write(content)
#            out_file.write("\n")
        #Ending
        


class Html(Element):
    doctype = '!DOCTYPE html'
    tag = 'html'
    
    def _open_tag(self, additions = "", cur_ind = ""):    
        open_string = cur_ind + "<{}>".format(self.doctype)
        open_string = open_string + ("\n")
        open_string = open_string + cur_ind + "<{}".format(self.tag)
        

        for key, value in self.attributes.items():
            open_string = open_string + (self.indent + cur_ind + ' {}="{}"'.format(key, value))
        open_string = open_string + self.indent + cur_ind + additions
        open_string = open_string + self.indent + cur_ind + ">"
        
        return open_string

class Head(Element):
    tag = "head"
        
class Body(Element):
    tag = 'body'
    
class P(Element):
    tag = 'p'
    indent = "    "
    
    
    
class OneLineTag(Element):
    indent = "    "
    def append(self, content):
        raise NotImplementedError
    
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.indent)
        out_file.write(cur_ind + self._open_tag())
        out_file.write(cur_ind + self.contents[0])
        out_file.write(cur_ind + self._closed_tag())
        
        
#        out_file.write("<{}>".format(self.tag))
#        out_file.write(self.contents[0])
#        out_file.write("</{}>\n".format(self.tag))
        
class Title(OneLineTag):
    tag = "title"
    
class A(OneLineTag):
    tag = "a" 
    
    def __init__(self, link, content = None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)
       
        
        
class H(OneLineTag):
    
    def __init__(self, number, content = None, **kwargs):
       self.tag = "h" + str(number)
       super().__init__(content, **kwargs)


    
    
class SelfClosingTag(Element):
    
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
        
    def append(self, *args):
        raise TypeError
    
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.indent)
        out_file.write(cur_ind + self._open_tag(' /'))
#        out_file.write("<{}".format(self.tag))
#        #print any style
#        for key, value in self.attributes.items():
#            out_file.write(' {}="{}"'.format(key, value))
#        #close first line
#        out_file.write(" />\n")
        
        
    
class Hr(SelfClosingTag):
    tag = "hr"
    
class Br(SelfClosingTag):
    tag = "br"
    
class Ul(Element):
    tag = 'ul'
    indent = "    "

class Li(Element):
    tag = 'li'
    indent = "    "
    
class Meta(SelfClosingTag):
    tag = "meta"

    def __init__(self, content=None, **kwargs):
        kwargs['charset'] = "UTF-8"
        super().__init__(content, **kwargs)
