#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag ='html'
    def __init__(self, content=None, **kwargs):
        self.kw_dict = kwargs

        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        print("contents is:",self.contents)

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        #loop through list of contents
        assembled_string = "<{}".format(self.tag)
        for key, value in self.kw_dict.items():
            assembled_string += ' ' + key + '=' + '"{}"'.format(value)

        assembled_string += ">"
        out_file.write(assembled_string)

        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)

            out_file.write("\n")

        out_file.write("</{}>\n".format(self.tag))

class Body(Element):
    tag = 'body'

class Html(Element):
    tag = 'html'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    pass
    def render(self, out_file):
        #loop through list of contents
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"