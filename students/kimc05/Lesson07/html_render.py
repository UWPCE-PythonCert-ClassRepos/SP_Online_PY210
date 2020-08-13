#!/usr/bin/env python3

"""
A class-based system for rendering html.
Christine Kim
Lesson 7 HTML Render
"""


# this is the framework for the base class
class Element(object):
    # class attribute
    tag = "html"
    indent = "    "

    #Initialize a new base Element
    def __init__(self, content=None, **kwargs):
        # store content in list, use self for other methods
        self.contents = []
        
        self.attributes = kwargs

        if content is not None:
            self.append(content)


    def append(self, new_content):
        # add new content
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        # start with tag        
        out_file.write(cur_ind + self.open_tag())

        # loop through the list of contents:
        for content in self.contents:
            # recursive if element
            try:
                content.render(out_file, cur_ind + self.indent)
            # print if string
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
            out_file.write("\n")
        
        # finish with tag
        out_file.write(cur_ind + self.close_tag())

    def open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(" {}='{}'".format(key, value))
        return "".join(open_tag) + ">\n"

    def close_tag(self):
        return "</{}>".format(self.tag) + "\n"

# this is the framework for the body class
class Body(Element):
    tag = "body"

# this is the framework for the paragraph class
class P(Element):
    tag = "p"

# this is the framework for the HTML class
class Html(Element):
    
    tag = "html"
    # render the element and write to out file
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)

class Head(Element):
    tag = "head"

class OneLineTag(Element):

    #overwrite render()
    def render(self, out_file, cur_ind=""):
        # start with html tag
        out_file.write(cur_ind + self.open_tag().strip())
        # write title
        out_file.write(self.contents[0])
        # finish with html tag
        out_file.write(self.close_tag())

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    
    # overwrite render
    def render(self,out_file, cur_ind=""):
        tag = self.open_tag()[:-2] + " />\n"
        out_file.write(cur_ind + tag)

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

    def __int__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag cannot contain any content")
        super().__int__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You cannot add content to a SelfClosingTag")

class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs["href"] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class Header(Element):
    tag = "head"

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = f"h{level}"
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"