#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


class Element(object):
    """ This is a base class representing an HTML element.

    Attributes:
    tag_name - the string used for the element's tag. Defaul of "html" is
        just to fill in something.
    tag_attributes - any tag attributes passed in throug kwargs to __init__.
    indent - How many spaces to use for a single indent for 'pretty print'.
        Change this to set the indent level.
    content - the content within a tag, with the exception of the enclosing
        "<>" the tag name and the tag attributes.
    """

    tag_name = "html"
    tag_attributes = {}
    indent = 3

    def __init__(self, content=None, **kwargs):
        """ Initialize the class.

        Keyword arguments:
        content - the content within a tag, with the exception of the
            enclosing "<>" the tag name and the tag attributes.
            Default = None.
        **kwargs - any HTML attributes for the tag.
        """

        self.content = []
        if content:
            self.append(content)

        self.tag_attributes = {}
        self.tag_attributes.update(kwargs)

    def append(self, new_content):
        """ Adds a new element onto this element.

        Keyword arguments:
        new_content - the element to be added. Any content not already defined
            is assumed not to have a render function and is converted to a
            string and made a TextWrapper object.
        """

        if hasattr(new_content, 'render'):
            self.content.append(new_content)
        else:
            self.content.append(TextWrapper(str(new_content)))

    def render(self, out_file, current_indent=0):
        """ Add the current object to a file as text.

        Keyword arguments:
        out_file - file being written to.
        current_indent - how many spaces to add at the start of the text line.
        """

        opening_tag = self.create_opening_tag(self.tag_name)
        closing_tag = self.create_closing_tag(self.tag_name)
        out_file.write(" " * current_indent)
        out_file.write(opening_tag)
        out_file.write("\n")
        for item in self.content:
            item.render(out_file, current_indent + self.indent)
            out_file.write("\n")
        out_file.write(" " * current_indent)
        out_file.write(closing_tag)

    def create_opening_tag(self, tag_name):
        """ Create the opening tag text.

        Keyword arguments:
        tag_name - the text to be used for the tag name.
        """

        attr_part = self.create_attribute_string()
        return "".join(["<", tag_name, attr_part, ">"])

    def create_closing_tag(self, tag_name):
        """ Create the closing tag text.

        Keyword arguments:
        tag_name - the text to be used for the tag name.
        """

        return "".join(["</", tag_name, ">"])

    def create_attribute_string(self):
        """ Create the text for tag attributes.
        """

        attr_list = []
        attr_part = ""
        for key, value in self.tag_attributes.items():
            attr_list.append('{}="{}"'.format(str(key), value))

        if len(attr_list) > 0:
            attr_part = " " + " ".join(attr_list)

        return attr_part


class Html(Element):
    tag_name = "html"

    def render(this, out_file):
        """ Add the current object to a file as text.

        Keyword arguments:
        out_file - file being written to.
        current_indent - how many spaces to add at the start of the text line.
        """

        out_file.write("<!DOCTYPE html>\n")
        # since the html tag is not indented we pass 0 for # of indent spaces
        super().render(out_file, 0)


class Body(Element):
    tag_name = "body"


class P(Element):
    tag_name = "p"


class Head(Element):
    tag_name = "head"


class Ul(Element):
    tag_name = "ul"


class Li(Element):
    tag_name = "li"


class OneLineTag(Element):
    """ A tag that has all of its text, including the opening and closing
    tags, on one line.
    """

    def render(self, out_file, current_indent=0):
        opening_tag = self.create_opening_tag(self.tag_name)
        closing_tag = self.create_closing_tag(self.tag_name)
        out_file.write(" " * current_indent)
        out_file.write(opening_tag)
        for item in self.content:
            item.render(out_file, 0)
        out_file.write(closing_tag)


class Title(OneLineTag):
    tag_name = "title"


class A(OneLineTag):
    tag_name = "a"

    def __init__(self, link, content):
        self.content = []
        if content:
            self.append(content)

        self.tag_attributes = {"href": link}


class H(OneLineTag):
    tag_name = "h"

    def __init__(self, level, content=None, **kwargs):
        # TODO - Check that level is an int
        self.tag_name = "{}{}".format(self.tag_name, str(level))
        super().__init__(content, **kwargs)


class SelfClosingTag(OneLineTag):
    """ A tag that has a opening tag but no closing tag.
    """
    def create_opening_tag(self, tag_name):
        attr_part = self.create_attribute_string()
        return "".join(["<", tag_name, attr_part, " />"])

    def create_closing_tag(self, tag_name):
        return ""


class Hr(SelfClosingTag):
    tag_name = "hr"


class Br(SelfClosingTag):
    tag_name = "br"


class Meta(SelfClosingTag):
    tag_name = "meta"


class TextWrapper():
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_indent=0):
        file_out.write(" " * current_indent)
        file_out.write(self.text)
