#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None, **kwargs):
        self.contents = [content]
        self.attribs = kwargs


    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        if attribs is not None:
            out_file.write(f"<{self.tag} ")
            for items in self.attribs.items():
                out_file.write(items[0])
                out_file.write("=")
                out_file.write(items[1])
                out_file.write(",")
            out_file.write(">\n")

        else:
            out_file.write(f"<{self.tag}>\n")
            for content in self.contents:
                if content is not None:
                    try:
                        content.render(out_file)
                    except AttributeError:
                        out_file.write(content)
        out_file.write("\n")

        out_file.write(f"</{self.tag}>\n")




class Body(Element):
    tag = 'body'

class Html(Element):
    tag = 'html'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):

    def render(self, out_file):
        out_file.write(f"<{self.tag}>")
        for content in self.contents:
            if content is not None:
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(content)
        out_file.write(f"</{self.tag}>\n")

    def append(self, new_content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'





