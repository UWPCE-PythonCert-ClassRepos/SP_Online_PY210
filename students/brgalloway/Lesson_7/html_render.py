#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    tag = "html"
    attributes = {}
    open_tag = []
    close_tag = []

    def __init__(self, content=None, **kwargs):
        self.content = [content]
        # capture attributes passed in for element
        self.attributes = kwargs
        # prevent empty elements from being created with type None
        if None in self.content:
            self.content = []

    def append(self, new_content):
        self.content.append(new_content)

    def _opening_tag(self):
        self.open_tag = [f"<{self.tag}"]
        for k,v in self.attributes.items(): 
            self.open_tag.append(f" {k}=\"{v}\"")
        self.open_tag.append(">")
     
        return self.open_tag

    def _closing_tag(self):
        self.close_tag = [f"</{self.tag}>\n"]
        return self.close_tag

    def render(self, out_file):
        out_file.write("".join(self._opening_tag()))
        out_file.write("\n")
        for content in self.content:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write("".join(self._closing_tag()))

class Html(Element):

    tag = "html"
    
class Body(Element):

    tag = "body"
    
class P(Element):

    tag = "p"
        
class Head(Element):
    
    tag = "head"

class OneLineTag(Element):

    def render(self, out_file):
        out_file.write("".join(self._opening_tag()))
        out_file.write(self.content[0])
        out_file.write("".join(self._closing_tag()))

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):

    tag = "title"

class SelfClosingTag(OneLineTag):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")
    
    def render(self, out_file):
        out_file.write(f"<{self.tag} />\n")

class Hr(SelfClosingTag):

    tag = "hr"

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write("".join(self._opening_tag()[:-1]))
        out_file.write("".join(self.content))
        out_file.write(" />\n")
            
class Br(SelfClosingTag):

    tag = "br"

class A(OneLineTag):
    
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)
 