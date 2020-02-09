#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    
    tag = "html"
    tag_attributes = dict()
    indent = 0

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        
        self.tag_attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            if isinstance(content,str):
                out_file.write((self.indent + 1) * '    ') #Add indent to content
                out_file.write(content)
                out_file.write("\n")
            else:
                content.indent = self.indent + 1 #Set next indent level
                content.render(out_file)
        out_file.write(self._close_tag())

    def _open_tag(self):
        open_tag = [self.indent * '    ']
        open_tag.append("<{}".format(self.tag))
        for key, value in self.tag_attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        return "".join(open_tag)
    
    def _close_tag(self):
        close_tag = [self.indent * '    ']
        close_tag.append("</{}>\n".format(self.tag))
        return "".join(close_tag)
        
class Html(Element):
    tag = "html"
    
    def render(self, out_file):
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file)

class Body(Element):
    tag = "body"
    
class P(Element):
    tag = "p"
    
class Head(Element):
    tag = "head"
    
class OneLineTag(Element):
    
    def append(self, new_content):
        raise NotImplementedError
        
    def render(self, out_file):
        out_file.write(self._open_tag())
        for content in self.contents:
            if isinstance(content,str):
                out_file.write(content)
            else:
                content.render(out_file)
        out_file.write(self._close_tag().lstrip()) #pull out the indents
        
class Title(OneLineTag):
    tag = "title"
    
class SelfClosingTag(Element):
    def render(self, out_file):
        out_file.write(self._open_tag()[:-1] + " />\n")

class Hr(SelfClosingTag):
    tag = 'hr'
    
class Br(SelfClosingTag):
    tag = 'br'
    
    def __init__(self, content = None, **kwargs):
        if content is not None:
            raise TypeError
            
    def append(self, new_content):
        raise TypeError

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'
    
class H(OneLineTag):
    tag = 'h'
    def __init__(self, level, content, **kwargs):
        self.tag = self.tag+str(level)
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = 'meta'