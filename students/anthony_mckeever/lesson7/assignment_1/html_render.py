#!/usr/bin/env python3

"""
Programming In Python - Lesson 7 Assignment 1: HTML Renderer
Code Poet: Anthony McKeever
Start Date: 08/27/2019
End Date: 08/31/2019
"""

class Element(object):
    """
    The Base Element Class
    """
    tag = "html"
    indent = "   "

    def __init__(self, content=None, **kwargs):
        """
        Initialize a new Base Element

        :self:      The class
        :content:   The initial innerHTML to append to the element (Default = None)
        :**kwargs:  Additional Element Attrbutes to append to the element.
        """
        self.element_attributes = kwargs
        
        self.content = []  # innerHTML
        if content is not None:
            self.append(content)

    
    def append(self, new_content):
        """
        Append additional innerHTML items to the element.

        :self:          The class
        :new_content:   The additional innerHTML to append.
        """
        self.content.append(new_content)

    
    def get_element_attributes(self):
        """
        Return a string containing the tag and element attributes with their values

        :self:  The class.
        """
        attribs = [self.tag]

        if self.element_attributes is not None:
            attribs.extend([f"{k}=\"{v}\"" for k, v in self.element_attributes.items()])
        
        return " ".join(attribs)


    def get_node_open(self):
        """
        Return the element's opening node as a string.

        :self:  The class.
        """
        return f"<{self.get_element_attributes()}>"


    def get_node_close(self):
        """
        Return the element's closing node as a string.

        :self:  The class.
        """
        return f"</{self.tag}>"


    def render(self, out_file, ind=""):
        """
        Renders the element and write it to the out_file

        :self:      The class.
        :out_file:  The file to write to.
        :ind:       The current level of indentation of the parent element.
        """
        indent_to = f"{ind}{self.indent}"
        
        out_file.write(f"{ind}{self.get_node_open()}\n")

        if self.content is not None:
            for inner in self.content:
                if hasattr(inner, "render"):
                    inner.render(out_file, indent_to)
                else:
                    out_file.write(f"{indent_to}{inner}\n")

        out_file.write(f"{ind}{self.get_node_close()}\n")


class Html(Element):
    """
    The HTML Element.
    """
    def render(self, out_file, ind=""):
        """
        Renders the element and write it to the out_file
        Before rendering it's own content it will also render a DocType() element

        :self:      The class.
        :out_file:  The file to write to.
        :ind:       The current level of indentation of the parent element.
        """
        indent_to = f"{ind}"
        DocType().render(out_file, indent_to)
        super().render(out_file, indent_to)


class Head(Element):
    """
    The Header Element of the entire document.
    """
    tag = "head"


class Body(Element):
    """
    The Body Element.
    """
    tag = "body"


class P(Element):
    """
    The Paragraph Element.
    """
    tag = "p"


class Ul(Element):
    """
    The List Parent Element.
    """
    tag = "ul"


class Li(Element):
    """
    The List Child Element.
    """
    tag = "li"


class OneLineTag(Element):
    """
    The One Line Tag Element.

    An element where all of its content are on a single line.
    """
    def render(self, out_file, ind=""):
        """
        Renders the element and write it to the out_file

        :self:      The class.
        :out_file:  The file to write to.
        :ind:       The current level of indentation of the parent element.
        """
        inner = " ".join(self.content)
        out_file.write(f"{ind}{self.get_node_open()}{inner}{self.get_node_close()}\n")


class Title(OneLineTag):
    """
    The Title Element.
    """
    tag = "title"


class H(OneLineTag):
    """
    The Heading Element.
    Not to be confused with the Header element, this element is for adding
    text to your document for emphasising the headings of new content areas.
    """
    def __init__(self, heading_level, content, **kwargs):
        """
        Initializes a Heading element.

        :self:          The class.
        :heading_level: The level of the heading.  The larger the number the smaller the heading.
        :content:       The innerHTML of the heading.
        :**kwargs:      Any additional element attributes to give the heading element.
        """
        super().__init__(content, **kwargs)
        self.tag = f"h{heading_level}"


class A(OneLineTag):
    """
    The Anchor Element.
    """
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        """
        Initializes an Anchor element.

        :self:      The class.
        :link:      The href value of the anchor.
        :content:   The innerHTML or text of the anchor.
        :**kwargs:  Any additional element attributes to give the anchor element.
        """
        super().__init__(content, **kwargs)
        self.element_attributes.update({"href": link})


class SelfClosingTag(Element):
    """
    The Self Closing Tag Element

    These elements are elements that open and close without any content in the middle.
    You cannot append content to this type of element.
    """
    def __init__(self, **kwargs):
        """
        Initializes a Self Closing Tag element.

        :self:      The class
        :**kwargs:  Any additional attributes to give the Self Closing Tag element.
        """
        super().__init__(None, **kwargs)


    def append(self, content=None):
        """
        Raise a TypeError because you cannot append content to a self closing element.

        :self:      The class.
        :content:   Not used.
        """
        raise TypeError(f"{self.tag.capitalize()} nodes cannot have innerHTML content.")


    def get_node_open(self):
        """
        Return the element's opening node as a string.

        :self:  The class.
        """
        return f"<{self.get_element_attributes()}"


    def get_node_close(self):
        """
        Return the element's closing node as a string.

        :self:  The class.
        """
        return " />"


    def render(self, out_file, ind=""):
        """
        Renders the element and write it to the out_file

        :self:      The class.
        :out_file:  The file to write to.
        :ind:       The current level of indentation of the parent element.
        """
        out_file.write(f"{ind}{self.get_node_open()}{self.get_node_close()}\n")


class DocType(SelfClosingTag):
    """
    The DocType element.
    """

    indent = ""
    tag = "!DOCTYPE"

    def __init__(self, doc_type="html"):
        """
        Initializes a DocType element.

        :self:      The class
        :doc_type:  The document type (Default = HTML)
        """
        self.element_attributes = f"{self.tag} {doc_type}"
        self.content = None


    def get_node_open(self):
        """
        Return the element's opening node as a string.

        :self:  The class.
        """
        return f"<{self.element_attributes}"


    def get_node_close(self):
        """
        Return the element's closing node as a string.

        :self:  The class.
        """
        return ">"


class Meta(SelfClosingTag):
    """
    The Meta Tag element for defining additional parameters in the document's header.
    """
    tag = "meta"


class Hr(SelfClosingTag):
    """
    The Horizontal Rule element.  Creates a break with a visible line.
    """
    tag = "hr"


class Br(SelfClosingTag):
    """
    The Line Break element.  Creates a line break similar to a return.
    """
    tag = "br"
