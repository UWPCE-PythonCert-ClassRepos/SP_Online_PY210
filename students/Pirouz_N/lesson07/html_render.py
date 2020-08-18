#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    """Element is an HTML element that holds a list of contents.

        The list hold information describing the HTML element as well as a class attribute describing the HTML tag
        called tag. It also contains instance attributes such as contents which is a list that contains the contents.
        It is very likely that the contents could include element which would be the sub elements to the current
        element. There are two major methods append and render. Append adds more contents to the contents list. Render
        adds the current element.

        Attributes:
            contents: Is the list of the current elements containing all the sub elements and the additional contents.
            Style: Are additional arguments that define the style of the element.
    """
    tag = 'html'
    indent = "    "

    def __init__(self, content=None, **kwargs):
        """Initialises the Element class.

        Args:
            content: Accepts the first content in its contents list, otherwise it will be empty contents list.
            kwargs: Are additional arguments that define the style of the element.
        """
        if content is not None:
            if hasattr(content, 'render'):
                self.contents = [content]
            else:
                self.contents = [TextWrapper(str(content))]
        else:
            self.contents = []
        self.style = kwargs

    def append(self, new_content):
        """Appends the new_contents to the contents list.

        Args:
            new_content: New content to be added to the contents list.
        """
        if new_content is not None:
            if hasattr(new_content, 'render'):
                self.contents.append(new_content)
            else:
                self.contents.append(TextWrapper(str(new_content)))

    def render_style(self):
        """This method adds the style to the tag. It returns an empty string if there are no styles. """
        if len(self.style) == 0:
            return ""
        return ' ' + ' '.join(['='.join([item,  '\"' + str(self.style[item]) + '\"']) for item in self.style])

    def content_list_render(self, out_file, multiline=True, cur_ind=""):
        """Renders contents of Element.

        Args:
            out_file: Is the stream that that will be added to before returning.
            multiline: It defines if after ever item on the list there needs to be a line break during render.
            cur_ind: The current indentation of element.

        """
        for content in self.contents:
            content.render(out_file, cur_ind=cur_ind)
            if multiline:
                out_file.write('\n')

    def render(self, out_file, cur_ind=""):
        """Renders contents of Element.

        Args:
            out_file: Is the stream that that will be added to before returning.
            cur_ind: The current indentation of element.
        """
        out_file.write(cur_ind + "<{}".format(self.tag) + self.render_style() + ">\n")
        self.content_list_render(out_file, cur_ind=cur_ind + self.indent)
        out_file.write(cur_ind + "</{}>".format(self.tag))


class TextWrapper:
    """A simple wrapper that creates a class with a render method for simple text."""
    def __init__(self, text):
        self.text = text

    def render(self, out_file, cur_ind=""):
        """Renders contents of Element.

        Args:
            out_file: Is the stream that that will be added to before returning.
            cur_ind: The current indentation of element.
        """
        out_file.write(cur_ind + self.text)


class Html(Element):
    """Html is an HTML element that holds a list of contents."""
    tag = 'html'

    def render(self, out_file, cur_ind=""):
        """Renders contents of HTML Element.

        Args:
            out_file: Is the stream that that will be added to before returning.
            cur_ind: The current indentation of element.
        """
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind=cur_ind)


class Body(Element):
    """Body is an HTML element that holds a list of contents."""
    tag = 'body'


class P(Element):
    """P is an HTML element that holds a list of contents."""
    tag = 'p'


class Head(Element):
    """Head is an HTML element that holds a list of contents."""
    tag = 'head'


class OneLineTag(Element):
    """OneLineTag is an HTML element that is a one liner element. For small elements. """

    def render(self, out_file, cur_ind=""):
        """Renders contents of one line tag HTML Element.

        Args:
            out_file: Is the stream that that will be added to before returning.
            cur_ind: The current indentation of element.
        """
        out_file.write(cur_ind + "<{}".format(self.tag) + self.render_style() + ">")
        self.content_list_render(out_file, multiline=False)
        out_file.write("</{}>".format(self.tag))


class Title (OneLineTag):
    """Title is a one line tag HTML element that holds a list of contents."""
    tag = 'title'


class SelfClosingTag(OneLineTag):
    """Self closing tag is an HTML element that is a one liner element. For small elements and self closing. """

    def __init__(self, content=None, **kwargs):
        """Overrides init from Element to raise exception if an element is added to the contents.

            Args:
            content: Accepts the first content in its contents list, otherwise it will be empty contents list.
            kwargs: Are additional arguments that define the style of the element.

            Raises:
                TypeError: If args is not equal to None type error will be raised.
        """
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        """Overrides append from Element to raise exception if an element is added to the contents.

            Args:
                args: That could be added to contents.

            Raises:
                TypeError: If args is not equal to None type error will be raised.
        """
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, out_file, cur_ind=""):
        """Renders contents of one line tag HTML Element.

        Args:
            out_file: Is the stream that that will be added to before returning.
            cur_ind: The current indentation of element.
        """
        out_file.write(cur_ind + "<{}".format(self.tag) + self.render_style())
        self.content_list_render(out_file, multiline=False)
        out_file.write(" />")


class Hr (SelfClosingTag):
    """Hr is a self closing HTML element that holds a list of contents."""
    tag = 'hr'


class Br (SelfClosingTag):
    """Br is a self closing HTML element that holds a list of contents."""
    tag = 'br'


class A (OneLineTag):
    """A is a one line tag HTML element that holds a list of contents."""
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        """Initialises the A class.

        Args:
            Link: Is the URL string for the link.
            content: Accepts the first content in its contents list, otherwise it will be empty contents list.
            kwargs: Are additional arguments that define the style of the element.
        """
        super().__init__(content, **dict({'href': link}, **kwargs))


class Ul (Element):
    """Ul is an HTML element that holds a list of contents. Represents an unordered list."""
    tag = 'ul'


class Li(Element):
    """Li is an HTML element that holds a list of contents. Represents an ordered list."""
    tag = 'li'


class H (OneLineTag):
    """H is a one line tag HTML element that holds a list of contents."""

    def __init__(self, level, content=None, **kwargs):
        """Initialises the A class.

        Args:
            level: Defines what number header is being used.
            content: Accepts the first content in its contents list, otherwise it will be empty contents list.
            kwargs: Are additional arguments that define the style of the element.
        """
        self.tag = 'h' + str(level)
        super().__init__(content, **kwargs)


class Meta (SelfClosingTag):
    """Meta is a self closing HTML element that holds a list of contents."""
    tag = 'meta'

