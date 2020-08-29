"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    """HTML Base Element that has tags & contains other elements inside its content"""

    tag = "html"
    content_join = "\n"

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

    def open_tag(self):
        """Generates the opening tag of the element"""
        attributes_text = [
            f' {attribute}="{value}"' for attribute, value in self.attributes.items()
        ]
        return f"<{self.tag}{''.join(attributes_text)}>"

    def append(self, new_content):
        """
        Appends the new internal content to be contained within this element

        Parameters
        ----------
        new_content : str|list|Element
            Internal content of the self-element
        """
        self.content.append(new_content)

    def render(self, out_file):
        """
        Writes the Element contents to the file

        Parameters
        ----------
        out_file : file-like-object
            The file where the content gets written to.
        """
        out_file.write(self.open_tag())
        out_file.write(self.content_join)
        for sub_content in self.content:
            try:
                sub_content.render(out_file)
            except AttributeError:
                out_file.write(sub_content)
                out_file.write(self.content_join)
        out_file.write(f"</{self.tag}>")
        out_file.write("\n")


class Html(Element):
    """html tagged element"""

    tag = "html"


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

