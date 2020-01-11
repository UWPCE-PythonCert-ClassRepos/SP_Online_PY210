#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.contents = content
        if self.contents is None:
            self.contents = []
        else:
            self.contents = [content]

        #print("Contents is: ", self.contents)

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))

        open_tag.append(">")
        return "".join(open_tag) 

    def _close_tag(self):
        close_tag = "</{}>".format(self.tag)
        return close_tag

    def render(self, out_file, cur_ind=""):
        #out_file.write("<{}>\n".format(self.tag))
        #open_tag = ["<{}".format(self.tag)]
        
        #for key, value in self.attributes.items():
        #    open_tag.append(' {}="{}"'.format(key, value))

        #open_tag.append(">\n")
        #out_file.write("".join(open_tag))        
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        #out_file.write("</{}>\n".format(self.tag))
        out_file.write(self._close_tag())
        out_file.write("\n")

class Html(Element):
    tag = "html"
    def render(self, out_file):
        out_file.write("<!DOCTYPE html>\n")
        Element.render(self, out_file)

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class UL(Element):
    tag = "ul"

class Li(Element):
    tag = "li"


class OneLineTag(Element):
    
    def render(self, out_file, cur_ind=""):
        out_file.write(self._open_tag())
        #out_file.write("<{}>".format(self.tag))        
        out_file.write(self.contents[0])
        #out_file.write("</{}>\n".format(self.tag))
        out_file.write(self._close_tag())

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    
    def render(self, out_file, cur_ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class HR(SelfClosingTag):
    tag = "hr"

class BR(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = "h" + str(level)
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"




