#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content=None, **kwargs):
        self.contents = [content]
        self.attributes = [kwargs]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        open_tag = ["<{}".format(self.tag)]
        for dictPair in self.attributes:
            if dictPair:
                for key, value in dictPair.items():
                    open_tag.append(" ")
                    open_tag.append(key)
                    open_tag.append("=")
                    open_tag.append('"{}"'.format(value))
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        for content in self.contents:
            if content is not None:
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(content)
                out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))

    def _open_tag(self, portion):
        if portion == 1:
            return "<{}>".format(self.tag)
        if portion == 2:
            return "<{}".format(self.tag)
        if portion == 3:
            return ">"

    def _close_tag(self):
        return "</{}>".format(self.tag)




class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"


class OneLineTag(Element):
    tag = "title"

    def render(self, out_file):
        open_tag = ["<{}".format(self.tag)]
        for dictPair in self.attributes:
            if dictPair:
                for key, value in dictPair.items():
                    open_tag.append(" ")
                    open_tag.append(key)
                    open_tag.append("=")
                    open_tag.append('"{}"'.format(value))
        open_tag.append(">")
        out_file.write("".join(open_tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file):
        open_tag = ["<{}".format(self.tag)]
        for dictPair in self.attributes:
            if dictPair:
                for key, value in dictPair.items():
                    open_tag.append(" ")
                    open_tag.append(key)
                    open_tag.append("=")
                    open_tag.append('"{}"'.format(value))
        open_tag.append(" />\n")
        out_file.write("".join(open_tag))

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class A(OneLineTag):

    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

    # def render(self, out_file):
    #     open_tag = ["<{}".format(self.tag)]
    #     open_tag.append(" ")
    #     open_tag.append("href=")
    #     open_tag.append(self.link)
    #     open_tag.append(">")
    #     open_tag.append(self.contents)
    #     open_tag.append("<")
    #     open_tag.append(self.tag)
    #     open_tag.append(">\n")
        
