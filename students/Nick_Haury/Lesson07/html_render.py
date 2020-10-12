#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "   "

    # **kwargs are keyword value pairs for HTML style attributes
    def __init__(self, content=None, **kwargs):
        self.class_dict = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        if new_content is not None:
            self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        # Loop through list of contents, having tags on front and back
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        self.render_attributes(out_file)
        out_file.write(">\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent)
                out_file.write(content)
                out_file.write("\n")
        out_file.write(cur_ind)
        out_file.write(self._close_tag())

    def render_attributes(self, out_file):
        for key in self.class_dict:
                out_file.write(f' {key}="{self.class_dict[key]}"')

    def _open_tag(self):
        return f"<{self.tag}"

    def _close_tag(self):
        return f"</{self.tag}>\n"


class Body(Element):

    tag = "body"

class P(Element):

    tag = "p"

class Html(Element):

    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file, cur_ind)


class Head(Element):

    tag = "head"

class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        self.render_attributes(out_file)
        out_file.write(">")
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
    
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):

    tag = "title"

class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag cannot containt content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        self.render_attributes(out_file)
        out_file.write(" />\n")

    def append(self, *args):
        raise TypeError("SelfClosingTag cannot have content added")

class Hr(SelfClosingTag):

    tag = "hr"

class Br(SelfClosingTag):

    tag = "br"

class Meta(SelfClosingTag):

    tag = "meta"

class A(OneLineTag):

    tag = "a"

    def __init__(self, link=None, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):

    tag = "ul"

class Li(Element):

    tag = "li"

class H(OneLineTag):

    tag = "h"
    header_level = ""

    def __init__(self, header_level="", content=None, **kwargs):
        try:
            int(header_level)
            self.header_level = header_level
        except ValueError:
            if header_level != "":
                print("header_level must be blank or an integer."
                      " Defaulting to blank.")
                self.header_level = ""
        super().__init__(content, **kwargs)
    
    def _open_tag(self):
        return f"<{self.tag}{self.header_level}"

    def _close_tag(self):
        return f"</{self.tag}{self.header_level}>\n"

if __name__ == "__main__":
    pass