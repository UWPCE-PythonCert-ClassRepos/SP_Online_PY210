#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


class Element(object):
    """
    An Element class used to render different html class types. 
    """
    tag = "html"
    attrs = ""
    indent = 3 * ' '

    def __init__(self, content=None, **kwargs):
        self.content = list()
        if content:
            self.content = [content]

        if kwargs:
            for key,value in kwargs.items():
                self.attrs += f' {key}=\"{value}\"'
        

    def append(self, new_content):
        """
        Adds new content for the html Element
        """
        self.content += [new_content]


    def render(self, out_file, curr_ind=""):
        """
        Renders the the html element so that it 
        has the format <tag>content</tag>
        """
        if self.tag != "html":
            curr_ind = curr_ind + self.indent
        out_file.write(self._open_tag(curr_ind))

        for item in self.content:
            try:
                item.render(out_file, curr_ind)
            except AttributeError:
                out_file.write(curr_ind + self.indent)
                out_file.write(f'{item}'.strip())
            out_file.write('\n')

        out_file.write(self._close_tag(curr_ind))


    def _open_tag(self, open_indent=""):
        """
        Returns the opening tag for an html element as a 
        str. <tag> or <tag attribute="some_attribute">

        :param open_indent: indentation amount for the Element
        :type open_indent: str
        """
        open_tag = f'{open_indent}<{self.tag}'
        # Checks for any attributes in the class
        if self.attrs:
            open_tag += f'{self.attrs}'
        open_tag += f'>\n'
        return open_tag


    def _close_tag(self, close_indent=""):
        """
        Returns a string of the closing tag of the Element with the 
        proper indentation. i.e. </tag>

        :param close_indent: amount to indent the closing tag
        :type close_indent: str
        """
        return f'{close_indent}</{self.tag}>'


class Html(Element):
    """
    A class to render the HTML document header.
    """
    def render(self, out_file, curr_ind=""):
        """
        Overrides the Element class's render method. 
        Creates the DOCTYPE tag at the beginning of the 
        html document.

        :param out_file: out_file object to 
        :type out_file: outFile

        :param curr_ind: Amount to indent element
        :type curr_ind: str
        """
        out_file.write(f'{curr_ind}<!DOCTYPE html>\n')
        super().render(out_file, curr_ind)


class Head(Element):
    """
    A subclass of the Element object with the 
    tag with the value 'head'.
    """
    tag = "head"


class Body(Element):
    """
    A subclass of the Element object with the 
    tag with the value 'body'.
    """
    tag = "body"


class P(Element):
    """
    A subclass of the Element object with the 
    tag with the value 'p'.
    """
    tag = "p"


class Ul(Element):
    """
    A subclass of the Element object with the 
    tag with the value 'ul'.
    """
    tag = "ul"


class Li(Element):
    """
    A subclass of the Element object with the 
    tag with the value 'li'.
    """
    tag = "li"


class OneLineTag(Element):
    """
    A subclass of the Element object that renders the class
    when only one line is required.
    """
    def append(self, content):
        """
        Raises a NotImplementedError if content is attempted to be appended 
        to content class variable.
        """
        raise NotImplementedError

    def render(self, out_file, curr_ind=""):
        """
        Overrides the Element class's render method. 
        Creates the one line with tag <tag> some content </tag>.

        :param out_file: out_file object to 
        :type out_file: outFile

        :param curr_ind: Amount to indent element
        :type curr_ind: str
        """
        out_file.write(curr_ind + self.indent)
        one_line = f'{self._open_tag()}{self.content[0]}{self._close_tag()}'.replace('\n', '')
        out_file.write(one_line)


class H(OneLineTag):
    """
    A subclass of the OneLineTag object with the 
    tag with the value h. This is known as the header class.
    """
    tag = "h"

    def __init__(self, header_level, content=None, **kwargs):
        """
        Initializes the header tag with the header level. i.e. h1
    
        :param header_level: size of header in 
        :type header_level:int

        :param content: set
        :type content: str
        """
        self.tag += str(header_level)
        super().__init__(content, **kwargs)


class Title(OneLineTag):
    """
    A subclass of the OneLineTag object with the 
    tag with the value title.
    """
    tag = "title"


class A(OneLineTag):
    """
    A subclass of the OneLineTag object with the 
    tag with the value 'a'. This is also known as an 
    anchor tag.
    """
    tag = "a"

    def __init__(self, link, content, **kwargs):
        kwargs['href']= f'{link}'
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):
    """
    A subclass of the Element object that creates
    a self closing tag. i.e <tag />
    """

    def __init__(self, content=None, **kwargs):
        """
        Initializes SelfClosingTag class. Provides basic checks
        to ensure not content gets slipped into the tag.
        """
        if content is not None:
            # Raises TypeError if SelfClosingTag contains 
            # content. Should be None always
            raise TypeError("Can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, new_content):
        """
        Raises a TypeError if adding content is attempted
        """
        raise TypeError("Can not contain any content")

    def render(self, out_file, curr_ind=""):
        """
        Overrides the Element class's render method. 
        Renders the self closing tag <tag attribute="some_attribue" />.

        :param out_file: out_file object to 
        :type out_file: outFile

        :param curr_ind: Amount to indent element
        :type curr_ind: str
        """
        out_file.write(curr_ind + self.indent)
        closing_tag = f'<{self.tag} />\n'
        if self.attrs:
            closing_tag = closing_tag.replace(' ', f'{self.attrs} ')
        out_file.write(closing_tag)


class Hr(SelfClosingTag):
    """
    A subclass of the Element object with the 
    tag with the value 'hr'. i.e <hr />
    """
    tag = "hr"


class Br(SelfClosingTag):
    """
    A subclass of the Element object with the 
    tag with the value 'br'. i.e <br />
    """
    tag = "br"


class Meta(SelfClosingTag):
    """
    A subclass of the Element object with the 
    tag with the value 'meta'. i.e <meta />
    """
    tag = "meta"