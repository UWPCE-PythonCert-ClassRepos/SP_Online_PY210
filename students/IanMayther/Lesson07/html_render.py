#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'

    def __init__(self, content=None):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    @classmethod
    def render(cls, out_file):
        #loop through the contents
        out_file.write("<{}>\n".format(cls.tag))
        for content in self.contents:            
            out_file.write(content)
            out_file.write("\n")
        
        out_file.write("</{}>\n".format(cls.tag))


class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'