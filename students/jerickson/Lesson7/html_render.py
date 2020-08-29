"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    """HTML Base Element that has tags & contains other elements inside its content"""

    tag = "html"

    def __init__(self, content=None):
        if content:
            self.content = [content]
        else:
            self.content = []

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
        out_file.write(f"\n<{self.tag}>")
        for sub_content in self.content:
            try:
                sub_content.render(out_file)
            except AttributeError:
                out_file.write("\n")
                out_file.write(sub_content)
        out_file.write(f"\n</{self.tag}>")


class Html(Element):
    """html tagged element"""

    tag = "html"


class Body(Element):
    """body tagged element"""

    tag = "body"


class P(Element):  # pylint: disable=invalid-name
    """p "paragraph" tagged element"""

    tag = "p"
