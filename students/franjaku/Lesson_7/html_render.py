#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'

    def __init__(self, content=None, **kwargs):
        """
        Initialize each instance of element.
        """
        if content:
            self.content_list = [content]
        else:
            self.content_list = []

        self.attributes = kwargs

    def append(self, new_content):
        self.content_list.append(new_content)

    def render_open_tag(self):
        open_tag = []

        for key, value in self.attributes.items():
            open_tag.append(f' {key}')
            open_tag.append(f'="{value}"')
        open_tag = "".join(open_tag)

        return "".join(open_tag)

    def render(self, out_file):
        """
        Render the element content list.

        If an another element is in the content list call the render
        function of the element in the list
        """
        out_file.write(f"<{self.tag}{self.render_open_tag()}>\n")

        for content in self.content_list:
            # type out content if string type
            if type(content) is str:
                out_file.write(f"{content}\n")

            else:
                content.render(out_file)

        out_file.write('</{}>\n'.format(self.tag))


class Html(Element):
    """
    HTML subclass of element.
    """
    tag = 'html'


class Body(Element):
    """
    Body subclass of element
    """
    tag = 'body'


class P(Element):
    """
    Paragraph subclass of element.
    """
    tag = 'p'


class Head(Element):
    """
    Head subclass of element.
    """
    tag = 'head'


class OneLineTag(Element):
    """
    Subclass for one line tags.

    Overide the render function.
    """
    tag = 'OneLineTag'

    def render(self, out_file):
        for content in self.content_list:
            out_file.write(f"<{self.tag}{self.render_open_tag()}>{content}</{self.tag}>\n")


class Title(OneLineTag):
    """
    Title subclass of one line tags.

    """
    tag = 'title'
