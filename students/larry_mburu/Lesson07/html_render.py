#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    
    indent = '   '
    tag = 'html'

    def __init__(self, content=None, **attrs):
        if content is not None:
            self.content = [content]
        else: 
            self.content = []

        self.attributes = attrs # element attributes

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file, cur_ind=""):
        if cur_ind: 
            out_file.write(f"{self.indent}{self.render_opening_tag()}")
        else:
            out_file.write(f"{self.render_opening_tag()}")
        out_file.write("\n")
        for content in self.content:
            try: 
                out_file.write(f"{self.indent}" + content)
            except TypeError: 
                content.render(out_file)
            out_file.write("\n")
        if cur_ind:
            out_file.write(f"{self.indent}</{self.tag}>")
        else:
            out_file.write(f"</{self.tag}>")

    def render_opening_tag(self):
        """
        returns formatted opening tags if given attributes
        """
        self.compose = f"<{self.tag}>" # self.compose - to build out element
        if len(self.attributes) == 0:  # zero attrs given. don't change tag structure!
            return self.compose
        else:
            self.compose = f"<{self.tag}" # one or more attrs given, change tag structure.
            for key in self.attributes: 
                self.compose += f" {key}=\"{self.attributes[key]}\""
            self.compose.rstrip()
            self.compose += ">"
            return self.compose


class Html(Element): 
    doc_type = "<!DOCTYPE html>"
    tag = 'html'
    def render(self, out_file, cur_ind=""):
        out_file.write(f"{self.doc_type}")
        out_file.write("\n")
        Element.render(self, out_file, cur_ind)

class Body(Element): 
    tag = 'body'

class P(Element): 
    tag = 'p'

class Head(Element): 
    tag = 'head'

class OneLineTag(Element): 
    tag = 'title'  #just to test

    def render(self, out_file): 
        #out_file.write(f"<{self.tag}>")
        out_file.write(self.render_opening_tag())
        for content in self.content: 
            try: 
                out_file.write(content)
            except TypeError: 
                content.render(out_file)
        out_file.write(f"</{self.tag}>")


class Title(OneLineTag): 
    tag = 'title'

class SelfClosingTag(Element): 
    tag = 'hr'  #just to test

    def render(self, outfile): 
        if self.content:  #self closing tags shouldn't have content
            raise TypeError
        self.compose = "<"
        self.compose += f"{self.tag}"
        for key in self.attributes:
            self.compose += f" {key}=\"{self.attributes[key]}\""
        self.compose += " />"
        outfile.write(self.compose)


class Hr(SelfClosingTag): 
    tag = 'hr'

class Br(SelfClosingTag): 
    tag = 'br'

class A(Element): 
    tag = 'a'
    def __init__(self, link, content):
        Element.__init__(self, content, href=link)

class Ul(Element): 
    tag = 'ul'

class Li(Element): 
    tag = 'li'

class H(OneLineTag): 
    tag = 'h'
    def __init__(self, level, content):
        self.tag += str(level)
        OneLineTag.__init__(self, content)

class Meta(SelfClosingTag): 
    tag = 'meta'