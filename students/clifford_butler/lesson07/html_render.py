#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content= None, **kwargs):
        # check if self.contents is empty
        if content == None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        # loop through the list of contents:
        #out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))
            
    def attributes(self, file_):
        pass
        

class Body(Element):
    tag = "body"
    
class Html(Element):
    tag = "html"
    
class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"
    
class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
    def append(self, content):
        raise NotImplementedError
    
class Title(Element):
    tag = "title"