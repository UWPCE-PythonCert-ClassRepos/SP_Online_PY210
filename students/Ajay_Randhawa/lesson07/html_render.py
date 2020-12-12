#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"

    indent = 4

    def __init__(self, content=None, **kwargs):
        self.contents = [content]
        self.attributes = [kwargs]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=0):
        curr_ind = cur_ind * self.indent
        curr_ind = " " *curr_ind
        out_file.write(curr_ind)
        open_tag = ["<{}".format(self.tag)]
        for dictPair in self.attributes:
            if dictPair:
                for key, value in dictPair.items():
                    open_tag.append(" ")
                    open_tag.append(key)
                    open_tag.append("=")
                    open_tag.append('"{}"'.format(value))
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        for content in self.contents:
            if content is not None:
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(curr_ind + "    ")
                    out_file.write(content)
                out_file.write("\n")
        out_file.write(curr_ind)
        out_file.write("</{}>".format(self.tag))


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=0):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind=0)


class Body(Element):
    tag = "body"

    def render(self, out_file, cur_ind=1):
        super().render(out_file, cur_ind=1)


class P(Element):
    tag = "p"

    def render(self, out_file, cur_ind=2):
        super().render(out_file, cur_ind=2)
    

class Head(Element):
    tag = "head"

    def render(self, out_file, cur_ind=1):
        super().render(out_file, cur_ind=1)

#base class
class OneLineTag(Element):
    tag = "title"

    def render(self, out_file, cur_ind=2):
        curr_ind = cur_ind * self.indent
        curr_ind = " " *curr_ind
        open_tag = ["<{}".format(self.tag)]
        for dictPair in self.attributes:
            if dictPair:
                for key, value in dictPair.items():
                    open_tag.append(" ")
                    open_tag.append(key)
                    open_tag.append("=")
                    open_tag.append('"{}"'.format(value))
        open_tag.append(">")
        out_file.write(curr_ind)
        out_file.write("".join(open_tag))
        for content in self.contents:
            if content is not None:
                out_file.write(content)
        out_file.write("</{}>".format(self.tag))
    #disable append function
    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


#base class 
class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=2):
        curr_ind = cur_ind * self.indent
        curr_ind = " " *curr_ind
        open_tag = ["<{}".format(self.tag)]
        for dictPair in self.attributes:
            if dictPair:
                for key, value in dictPair.items():
                    open_tag.append(" ")
                    open_tag.append(key)
                    open_tag.append("=")
                    open_tag.append('"{}"'.format(value))
        open_tag.append(" />")
        out_file.write(str(curr_ind))
        out_file.write("".join(open_tag))
        

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class A(OneLineTag):

    tag = "a"
    #initialize a custom header for every instance
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

    def render(self, out_file, cur_ind=5):
        super().render(out_file, cur_ind=5)

class Ul(Element):
    tag = "ul"

    def render(self, out_file, cur_ind=3):
        super().render(out_file, cur_ind=3)
    

class Li(Element):
    tag = "li"

    def render(self, out_file, cur_ind=4):
        super().render(out_file, cur_ind=4)

    
        
class H(OneLineTag):
    #iniitialize a custom tag for every instance
    def __init__(self, level, content=None, **kwargs):
        self.tag = "h"+str(level)
        super().__init__(content, **kwargs)



class Meta(SelfClosingTag):
    tag = "meta"