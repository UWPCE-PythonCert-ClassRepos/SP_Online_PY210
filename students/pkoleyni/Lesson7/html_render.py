#!/usr/bin/env python3


class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for just text

    This allows the Element classes to render either Element objects or
    plain text

    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_indent=""):
        file_out.write(current_indent + self.text)


class Element:
    """
    Main Class, other classes are Subclasses on Element Class
    """
    #Class attributes
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.content = []
        #call append class method if there content list is not empty
        if content:
            self.append(content)

    def append(self, content):
        """
        add a new content another element to this element
        """
        # if content has render method it means that content
        # is an object, subclass of Element class
        # if content is just a test then we create a new class of that content
        # by using TextWrapper(str(content)
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def make_tags(self):
        """
        create the tags, This CLass method returns open_tag an close_tag
        """
        #make a string from a list of key, value pair of the self.attributes
        attrs = " ".join(['{}="{}"'.format(k, v) for k, v in self.attributes.items()])
        if attrs.strip():
            # create open_tag using HTML tag and some HTML tag attributes 
            open_tag = "<{} {}>".format(self.tag, attrs.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self.tag)

        return open_tag, close_tag

    def render(self, out_file, cur_indent=""):
        open_tag, close_tag = self.make_tags()
        out_file.write(cur_indent + open_tag + "\n")
        for item in self.content:
            item.render(out_file, cur_indent + self.indent)
            out_file.write("\n")
        out_file.write(cur_indent + close_tag)


class OneLineTag(Element):
    def render(self, out_file, cur_indent=""):
        open_tag, close_tag = self.make_tags()
        out_file.write(cur_indent + open_tag)
        for item in self.content:
            item.render(out_file)
        out_file.write(close_tag)


class Html(Element):
    tag = 'html'
    def render(self, file_out, cur_indent=""):
        file_out.write(cur_indent + "<!DOCTYPE html>\n")
        super().render(file_out, cur_indent=cur_indent)


class SelfClosingTag(Element):

    def append(self, *args, **kwargs):
        raise TypeError("You can not add content to a self closing tag")

    def render(self, out_file, ind=""):
        open_tag = self.make_tags()[0]
        out_file.write(ind + open_tag.replace(">", " />"))


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class Title(OneLineTag):
    tag = "title"


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, *args, **kwargs):
        kwargs['href'] = link
        super().__init__(*args, **kwargs)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):
    tag = "H"
    def __init__(self, level, *args, **kwargs):
        self.tag = "h" + str(int(level))
        super().__init__(*args, **kwargs)


class Meta(SelfClosingTag):

    tag = "meta"