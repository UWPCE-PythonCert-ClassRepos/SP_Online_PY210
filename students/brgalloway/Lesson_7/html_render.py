#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "   "

    def __init__(self, content=None, **kwargs):
        self.content = [content]
        # capture attributes passed in for element
        self.attributes = kwargs
        # prevent empty elements from being created with type None
        if None in self.content:
            self.content = []

    # append new content 
    def append(self, new_content):
        self.content.append(new_content)

    # separate the tags for elements
    # and gather any attributes to place inside
    def _opening_tag(self, cur_ind=""):
        self.open_tag = [f"{cur_ind}<{self.tag}"]
        # loop over attributes in dictionary and format them
        for k,v in self.attributes.items(): 
            self.open_tag.append(f" {k}=\"{v}\"")
        self.open_tag.append(">")
     
        return self.open_tag

    # close tags that aren't self closing
    def _closing_tag(self, cur_ind=""):
        self.close_tag = [f"{cur_ind}</{self.tag}>\n"]
        return self.close_tag

    # render out opening tag
    # and loop over content
    def render(self, out_file, cur_ind=""):
        out_file.write("".join(self._opening_tag(cur_ind)))
        out_file.write("\n")
        for content in self.content:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
        out_file.write("".join(self._closing_tag(cur_ind)))

class Html(Element):

    tag = "html"
    # override render and call parent render
    def render(self, out_file, cur_ind=""):
        out_file.write(f"<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)

class Ul(Element):

    tag = "ul"

class Li(Element):

    tag = "li"  

class Head(Element):

    tag = "head"

class Body(Element):

    tag = "body"
    
class P(Element):

    tag = "p"

# self closing tags on one line
class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")
    
    def render(self, out_file, cur_ind=""):
        out_file.write("".join(self._opening_tag()[:-1]))
        out_file.write("".join(self.content))
        out_file.write(" />\n")

class Br(SelfClosingTag):

    tag = "br"

class Hr(SelfClosingTag):

    tag = "hr"

class Meta(SelfClosingTag):

    tag = "meta"

# single line tags that can contain content
class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):
        out_file.write("".join(self._opening_tag(cur_ind)))
        out_file.write(self.content[0])
        out_file.write("".join(self._closing_tag()))

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):

    tag = "title"   

class A(OneLineTag):
    
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)
        
class H(OneLineTag):

    tag = "h"
    def __init__(self, num, content=None, **kwargs):
        assert type(num) == int
        self.tag = f"h{num}"
        super().__init__(content, **kwargs)



 