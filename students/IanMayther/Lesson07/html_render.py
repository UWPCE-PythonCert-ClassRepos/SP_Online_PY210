#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def form_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(" {0}=\"{1}\"".format(key, value))
        open_tag.append(">\n")
        output_file = "".join(open_tag)
        output_file = "Test Text"
        #return output_file

    #@classmethod
    def render(self, out_file):
        #loop through the contents
        # open_tag = ["<{}".format(self.tag)]
        # for key, value in self.attributes.items():
        #     open_tag.append(" {0}=\"{1}\"".format(key, value))
        # open_tag.append(">\n")
        place_text = form_tag()
        out_file.write(place_text)
        for content in self.contents:           
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))
        
class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'Head'

class OneLineTag(Element):
    tag = 'OneLineTag'

    def append(self, new_content):
        raise NotImplementedError

    def render(self, out_file):
        #loop through the contents
        for content in self.contents:  
            out_file.write("<{}>{}</{}>".format(self.tag, content, self.tag))          

class Title(OneLineTag):
    tag = 'title'