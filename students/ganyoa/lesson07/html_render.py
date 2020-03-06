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
        #print("contents is:", self.contents)


    def append(self, new_content):
        self.contents.append(new_content)


    def open_tag(self):
        open_tag = ["<{}>".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}'.format(key, value))
            open_tag = "".join(open_tag)
        return open_tag

    def close_tag(self):
        close_tag = '</{}>'.format(self.tag)
        return close_tag


    def render(self, out_file):
        out_file.write(self.open_tag()) #out_file.write(self.open_tag() + '\n')
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write("\n")
        out_file.write(self.close_tag() + '\n')
        #out_file.write("</{}>\n".format(self.tag))


class Body(Element):
    #class exactly the same as the Element class, except with a different tag
    tag = 'body'


class Html(Element):
    tag = 'html'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = 'title'