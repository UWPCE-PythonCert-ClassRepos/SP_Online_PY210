#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content:
            self.contents = [content]
        else:
            self.contents = []
        self.attributes = kwargs
             
    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=0):
        out_file.write( f'{self.indent*cur_ind}<{self.tag}')
        for attribute in self.attributes:
            out_file.write(f' {attribute}="{self.attributes[attribute]}"')            
        out_file.write(">\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + 1)
            except AttributeError:
                cur_ind += 1
                out_file.write(f"{self.indent*cur_ind}{content}")
                cur_ind -= 1
                out_file.write("\n")
        out_file.write(f"{self.indent*cur_ind}</{self.tag}>\n")

class OneLineTag(Element):
    def render(self, out_file, cur_ind=0):
        out_file.write(f"{self.indent*cur_ind}<{self.tag}")
        for attribute in self.attributes:
                out_file.write(f' {attribute}="{self.attributes[attribute]}"')
        out_file.write(">")
        out_file.write(self.contents[0])
        out_file.write(f"</{self.tag}>\n")

    def append(self, content):
        raise NotImplementedError

class SelfClosingTag(OneLineTag):
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def render(self, out_file, cur_ind=0):
        out_file.write(f"{self.indent*cur_ind}<{self.tag}")
        for attribute in self.attributes:
                out_file.write(f' {attribute}="{self.attributes[attribute]}"')
        out_file.write(" />")

class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=0):
        out_file.write(f"{self.indent*cur_ind}<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

    def render(self, out_file, cur_ind=0):
        out_file.write( f'{self.indent*cur_ind}<{self.tag}')
        for attribute in self.attributes:
            out_file.write(f' {attribute}="{self.attributes[attribute]}"')            
        out_file.write(">\n")
        Meta(charset="UTF-8").render(out_file)
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + 1)
            except AttributeError:
                cur_ind += 1
                out_file.write(f"{self.indent*cur_ind}{content}")
                cur_ind -= 1
                out_file.write("\n")
        out_file.write(f"{self.indent*cur_ind}</{self.tag}>\n")

class Title(OneLineTag):
    tag = "title"

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        self.link = link
        super().__init__(content, **kwargs)
    
    def render(self, out_file, cur_ind=0):
        out_file.write(f'<{self.tag} href="{self.link}"')
        for attribute in self.attributes:
            out_file.write(f' {attribute}="{self.attributes[attribute]}"')
        out_file.write(">")
        out_file.write(self.contents[0])
        out_file.write(f"</{self.tag}>\n")   

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):
    def __init__(self, type, content=None, **kwargs):
        self.tag = f"h{type}"
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"
