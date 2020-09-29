#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


#Step 1

# This is the framework for the base class
class Element(object):

    tagname = "html"

    indent = " "

    def __init__(self, content=None, **kwargs):
        if content == None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.opentag())
        out_file.write("\n")
        for line in self.content:
            try:
                out_file.write(cur_ind + self.indent + line)
                out_file.write("\n")
            except TypeError:
                line.render(out_file, cur_ind + self.indent)
        out_file.write(cur_ind + self.closetag())
        out_file.write("\n")

    def opentag(self):
        opentag = "<{}".format(self.tagname)
        for k, v in self.attributes.items():
            opentag += ' {}="{}"'.format(k, v)
        opentag += ">"
        return opentag

    def closetag(self):
        return "</{}>".format(self.tagname)

#Step 2


class Html(Element):

    tagname = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Body(Element):

    tagname = "body"


class P(Element):

    tagname = "p"

#Step 3


class Head(Element):

    tagname = "head"


class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.opentag())
        for line in self.content:
            try:
                out_file.write(line)
            except TypeError:
                line.render(out_file)
        out_file.write(self.closetag())
        out_file.write("\n")


class Title(OneLineTag):

    tagname = "title"


#Step 5


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("Self-closing tags cannot have content.")
        self.attributes = kwargs

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.opentag())
        out_file.write("\n")

    def opentag(self):
        opentag = "<{}".format(self.tagname)
        for k, v in self.attributes.items():
            opentag += ' {}="{}"'.format(k, v)
        opentag += " />"
        return opentag


class Hr(SelfClosingTag):

    tagname = "hr"


class Br(SelfClosingTag):

    tagname = "br"


#Step 6


class A(OneLineTag):

    tagname = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs["href"] = link
        super().__init__(content, **kwargs)
        '''
        Question: am I able to call super().__init__ here without giving it the self argument
        because it "already knows" about self at this point?
        (This doesn't seem a very accurate way of explaining it,
        and I'm trying to clarify my understanding.)
        '''


#Step 7


class Ul(Element):

    tagname = "ul"


class Li(Element):

    tagname = "li"


class H(OneLineTag):

    tagname = "h"

    def __init__(self, headerlevel, content=None, **kwargs):
        self.headerlevel = headerlevel
        self.tagname += str(headerlevel)
        super().__init__(content, **kwargs)


#Step 8


class Meta(SelfClosingTag):

    tagname = "meta"

    def __init(self, charset, content=None, **kwargs):
        kwargs["charset"] = charset
        super().__init__(content, **kwargs)
