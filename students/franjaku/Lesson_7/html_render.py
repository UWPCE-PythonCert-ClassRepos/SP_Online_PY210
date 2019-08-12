#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    indent = "    "
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
        """
        Render the opening tag that includes all the attributes passed in
        <tag style="text-align: center; font-style: oblique;">
        """
        open_tag = []

        for key, value in self.attributes.items():
            open_tag.append(f' {key}')
            open_tag.append(f'="{value}"')
        open_tag = "".join(open_tag)

        return "".join(open_tag)

    def render(self, out_file, cur_ind=""):
        """
        Render the element content list.

        If an another element is in the content list call the render
        function of the element in the list
        """
        out_file.write(f"{cur_ind}<{self.tag}{self.render_open_tag()}>\n")
        content_ind = "".join([cur_ind,self.indent])

        for content in self.content_list:
            # type out content if string type
            if type(content) is str:
                out_file.write(f"{content_ind}{content}\n")

            else:
                content.render(out_file, content_ind)

        out_file.write(f"{cur_ind}</{self.tag}>\n")


class Html(Element):
    """
    HTML subclass of element.
    """
    tag = 'html'

    def render(self, out_file, cur_ind=""):
        """
        Write out the DOCTYPE tag and then render the rest.
        """
        out_file.write(f"{cur_ind}<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


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

    def render(self, out_file, cur_ind=""):
        for content in self.content_list:
            out_file.write(f"{cur_ind}<{self.tag}{self.render_open_tag()}>{content}</{self.tag}>\n")


class Title(OneLineTag):
    """
    Title subclass of one line tags.

    """
    tag = 'title'


class SelfClosingTag(Element):
    """
    Defines a selfclosing tag class that subclasses from element

    Example: SelfClosingTag(width=400) == <SelfClosingTag width="400" />
    """
    tag = 'SelfClosingTag'

    def render(self, out_file, cur_ind=""):
        """
        Called the reneder_open_tag method from the parent class
        """
        out_file.write(f"{cur_ind}<{self.tag}{self.render_open_tag()} />\n")


class Hr(SelfClosingTag):
    """
    Header break object
    """
    tag = 'Hr'


class Br(SelfClosingTag):
    """
    Line break object
    """
    tag = 'Br'


class Meta(SelfClosingTag):
    """
    Meta element to define encoding.
    """

    tag = 'meta'


class A(OneLineTag):
    """
    Anchor object that currently subclasses from OneLineTag
    """

    tag = 'a'

    def __init__(self, link, content, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul(Element):
    """
    Unordered list element
    """

    tag = 'Ul'


class Li(Element):
    """
    Object in the list
    """

    tag = 'Li'


class H(OneLineTag):
    """
    Header element
    """

    def __init__(self, level, content, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = 'h{}'.format(str(level))
