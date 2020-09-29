#!/usr/bin/env python3
"""
A class-based system for rendering html.
"""
# This is the framework for the base class
class Element(object):
    tag="html"
    indent="    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            self.content = []
        else:
            self.contents = [content]
    def append(self, new_content):
        self.contents.append(new_content)

    def open_tag(self, current_index=""):
        open_tag["{}<{}".format(current_index, self.tag)]
        for key, value in self.attributes.items():
            open_tag.appnd('{}="{}"'.format(key, value))
        return "".join(open_tag)
    
    def close_tag(self, current_index=""):
        return "{}</{}>\n".format(current_index, self.tag)
    
    def render(self, out_file, current_index=""):
        out_file.write(self.open_tag(current_index) + ">\n")
        for content in self.contents:
            try:
                content.render(out_file, current_index + self.indent)
            except:
                out_file.write(current_index + self.indent + content)
                out_file.write("\n")
        out_file.write(self.close_tag(current_index))

class HTML(Element):
    tag = "html"

    def render(self, out_file, current_index=""):
        out_file.write("<!DOCTYPE HTML>\n")
        super().render(out_file, current_index)
    
class Body(Element):
    tag= "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag= "head"

class OneLineTag(Element):
    def render(self, out_file, current_index=""):
        out_file.write(current_index + self.indent + self._opn_tag() + ">")
        out_file.write(self.contents[0])
        out_file.write(self.close_tag())
    
class Title(OneLineTag):
    tag = "title"

class A(OneLineTag):
    tag = "a"

    def __init__(self, link ,content=None, **kwargs):
        kwargs["href"] = link
        super().__init__(content, **kwargs)

    
class SelfClosingTag(Element):
    def render(self, outfile, current_index=""):
        tag=current_index + self.indent + self.open_tag + " />\n"
        outfile.write(tag)

    def append(self, *args):
        raise TypeError("Content cannot be added to a self closing tag.")
    
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("Content cannot be added to a self closing tag.")
        super().__init__(content=content, **kwargs)
    

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        self.tag = "h{}".format(level)
        super().__init__(content=content, **kwargs)


class Meta(SelfClosingTag):
    tag = "meta"
