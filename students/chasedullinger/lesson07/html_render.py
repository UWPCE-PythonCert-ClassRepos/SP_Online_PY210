#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    """Basic html element class"""
    tag = ""
    add_new_line = True  # Controls if new line should be added
    indent_spaces = 4
    indent = " " * indent_spaces  # string to pad indentation

    def __init__(self, content=None, **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        self.attributes = kwargs  # store kwargs as dict to unpack later

    def append(self, new_content):
        self.content.append(new_content)

    def get_opening_tag_string(self):
        """Builds the opening tag for an element"""
        opening_tag_string = ""
        opening_tag_string += f"<{self.tag}"
        for k, v in self.attributes.items():
            opening_tag_string += f' {k}="{v}"'
        opening_tag_string += ">"
        if self.add_new_line:
            opening_tag_string += "\n"
        return opening_tag_string

    def render(self, out_file=None, cur_ind=""):
        """Renders the section of html as text"""
        output_string = cur_ind
        if self.tag:
            output_string += self.get_opening_tag_string()
        for line in self.content:
            if not isinstance(line, str):  # Recursively render objects
                output_string += line.render(out_file, cur_ind + self.indent)
            else:  #If it's a string just render it with padding
                output_string += cur_ind + self.indent
                output_string += f"{line}"
            if self.add_new_line:
                output_string += "\n"
        if self.tag:
            output_string += cur_ind
            output_string += f"</{self.tag}>"
        if out_file:
            out_file.write(output_string)
        return output_string


class Html(Element):
    """Sub class for html tag"""
    tag = "html"

    def render(self, out_file=None, cur_ind=""):
        """Html tag render method.  Overrides method in baseclass to add header
        string showing the document type
        """
        header_string = "<!DOCTYPE html>\n"
        output_string = Element.render(self, out_file=None, cur_ind=cur_ind)
        if out_file:
            out_file.write(header_string + output_string)
        return header_string + output_string


class Body(Element):
    """Sub class for body tag"""
    tag = "body"


class P(Element):
    """Sub class for p (paragraph) tag"""
    tag = "p"


class Head(Element):
    """Sub class for head tag"""
    tag = "head"


class Ul(Element):
    """Sub class for ul (unordered list) tag"""
    tag = "ul"


class Li(Element):
    """Sub class for li (list item) tag"""
    tag = "li"


class OneLineTag(Element):
    """Sub class for tag that are all on one line"""
    add_new_line = False

    def render(self, out_file=None, cur_ind=""):
        """Overrides render method in base class to eliminate line breaks"""
        output_string = cur_ind
        if self.tag:
            output_string += self.get_opening_tag_string()
        for line in self.content:
            output_string += f"{line}"
        if self.tag:
            output_string += f"</{self.tag}>"
        if out_file:
            out_file.write(output_string)
        return output_string


class Title(OneLineTag):
    """Sub class for title tag"""
    tag = "title"


class SelfClosingTag(Element):
    """Sub class for tags that contain opening and closing in string"""
    def __init__(self, *args, **kwargs):
        if len(args) > 0:  # Raise error if user tries to pass in content
            raise TypeError("SelfClosingTag can not have content")
        self.content = []
        self.attributes = kwargs

    def get_opening_tag_string(self):
        """Overrides base method to include closing / at the end of the tag"""
        opening_tag_string = ""
        opening_tag_string += f"<{self.tag}"
        for k, v in self.attributes.items():
            opening_tag_string += f' {k}="{v}"'
        opening_tag_string += " />"
        return opening_tag_string

    def render(self, out_file=None, cur_ind=""):
        """Overrides base method to eliminate content"""
        output_string = cur_ind
        if self.tag:
            output_string += self.get_opening_tag_string()
        if out_file:
            out_file.write(output_string)
        return output_string


class Hr(SelfClosingTag):
    """Sub class for hr tag"""
    tag = "hr"


class Br(SelfClosingTag):
    """Sub class for br tag"""
    tag = "br"


class Meta(SelfClosingTag):
    """Sub class for meta tag"""
    tag = "meta"


class A(OneLineTag):  # Want links to be one line
    """Sub class for a (link) tag"""
    tag = "a"
    add_new_line = False

    def __init__(self, link, content, **kwargs):
        """Override base method to pass link as href keyword"""
        Element.__init__(self, content=content, href=link, **kwargs)


class H(OneLineTag):
    """Sub class for h tag"""

    def __init__(self, level, content):
        """Overide base method to include level of h in tag"""
        try:  # Check to make sure valid level is passed (must convert to int)
            int(level)
        except ValueError:
            raise TypeError("Level of H must be convertible to int")
        self.tag = f"h{level}"
        Element.__init__(self, content=content)
