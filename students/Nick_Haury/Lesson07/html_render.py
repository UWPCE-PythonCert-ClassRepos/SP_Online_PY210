#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

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

    def render(self, out_file):
        # Loop through list of contents, having tags on front and back
        self.render_open_tag(out_file)
        out_file.write(">\n")
        for content in self.contents:
            # out_file.write(content)
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(f"</{self.tag}>\n")

    def render_open_tag(self, out_file):
        out_file.write(f"<{self.tag}")
        for key in self.class_dict:
                out_file.write(f' {key}="{self.class_dict[key]}"')


class Body(Element):

    tag = "body"

class P(Element):

    tag = "p"

class Html(Element):

    tag = "html"

class Head(Element):

    tag = "head"

class OneLineTag(Element):

    def render(self, out_file):
        self.render_open_tag(out_file)
        out_file.write(">")
        out_file.write(self.contents[0])
        out_file.write(f"</{self.tag}>\n")
    
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):

    tag = "title"

if __name__ == "__main__":
    pass