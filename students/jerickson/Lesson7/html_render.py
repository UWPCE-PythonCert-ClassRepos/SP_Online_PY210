"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    """HTML Base Element that has tags & contains other elements inside its content"""

    tag = "html"
    content_join = "\n"
    indent = 4

    def __init__(self, content=None, **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        self.attributes = {}
        self.set_attributes(**kwargs)

    def set_attributes(self, **kwargs):
        """Processes HTML attributes and add them to the element"""
        new_attributes = kwargs
        for alternate_class_key in ["clas", "_class", "_clas"]:  # cspell:disable-line
            try:
                new_attributes["class"] = new_attributes.pop(alternate_class_key)
                break
            except KeyError:
                pass
        self.attributes.update(**new_attributes)

    def open_tag(self, cur_ind=0):
        """Generates the opening tag of the element"""
        attributes_text = [
            f' {attribute}="{value}"' for attribute, value in self.attributes.items()
        ]
        return " " * cur_ind + f"<{self.tag}{''.join(attributes_text)}>"

    def close_tag(self, cur_ind=0):
        """Generates the opening tag of the element"""
        closing_indent = cur_ind if self.content_join else 0
        return " " * closing_indent + f"</{self.tag}>"

    def append(self, new_content):
        """
        Appends the new internal content to be contained within this element

        Parameters
        ----------
        new_content : str|list|Element
            Internal content of the self-element
        """
        self.content.append(new_content)

    def render(self, out_file, cur_ind=0):
        """
        Writes the Element contents to the file

        Parameters
        ----------
        out_file : file-like-object
            The file where the content gets written to.
        """
        out_file.write(self.open_tag(cur_ind))
        out_file.write(self.content_join)
        for sub_content in self.content:
            try:
                sub_content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                if self.content_join:
                    out_file.write(" " * (cur_ind + self.indent))
                out_file.write(sub_content)
                out_file.write(self.content_join)
        out_file.write(self.close_tag(cur_ind))
        out_file.write("\n")


class Html(Element):
    """html tagged element"""

    tag = "html"

    def render(self, out_file, cur_ind=0):
        out_file.write(" " * cur_ind)
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Body(Element):
    """body tagged element"""

    tag = "body"


class P(Element):  # pylint: disable=invalid-name
    """p "paragraph" tagged element"""

    tag = "p"


class Head(Element):
    """head tagged element"""

    tag = "head"


class OneLineTag(Element):
    """Element sub-class for elements that should be printed in one line."""

    content_join = ""


class Title(OneLineTag):
    """title tagged element that prints on one line"""

    tag = "title"


class SelfClosingTag(OneLineTag):
    """Element sub-class for elements that self-close. Contains no content."""

    def __init__(self, **kwargs):
        super().__init__(content=None, **kwargs)

    def set_attributes(self, **kwargs):
        """Processes HTML attributes and add them to the element, forces no "content"."""
        if "content" in kwargs:
            raise TypeError
        super().set_attributes(**kwargs)

    def open_tag(self, cur_ind=0):
        """Generates the open/close tag of the element"""
        return super().open_tag(cur_ind).replace(">", " />")

    def close_tag(self, cur_ind=0):
        """No close tag for this element type."""
        return ""

    def append(self, *args, **kwargs):
        """Cannot append in a self-closing-tag"""
        raise TypeError("Cannot append content in a self-closing-tag")


class Hr(SelfClosingTag):
    """Hr "horizontal Line" tagged HTML element"""

    tag = "hr"


class Br(SelfClosingTag):
    """br "Break" tagged HTML element"""

    tag = "br"


class A(OneLineTag):  # pylint: disable=invalid-name
    """a "Anchor" tagged HTML element"""

    tag = "a"

    def __init__(self, link="", content=None, **kwargs):
        super().__init__(content=content, href=link, **kwargs)


class Li(Element):
    """li "list" tagged HTML element"""

    tag = "li"


class Ul(Element):
    """ul "Unordered List" tagged HTML element"""

    tag = "ul"


class H(OneLineTag):  # pylint: disable=invalid-name
    """h# "header" tagged HTML element"""

    def __init__(self, h_number=1, content=None, **kwargs):
        self.tag = f"h{h_number:d}"
        super().__init__(content=content, **kwargs)


class Meta(SelfClosingTag):
    """meta "Metadata" tagged HTML element"""

    tag = "meta"


## EXTRA TAGS ##


class Img(SelfClosingTag):
    """img "Image" tagged HTML element"""

    tag = "img"

    def __init__(self, src="", **kwargs):
        kwargs["src"] = src
        super().__init__(**kwargs)
