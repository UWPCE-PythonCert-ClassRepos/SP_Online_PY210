#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
#step 1
class Element(object):
    tag = "html"
    #step 9
    indent = "  "

    def __init__(self, content = None, **attrs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = attrs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self._open_tag())
        out_file.write("\n" + self.indent)

        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(cur_ind + content)
                out_file.write("\n")
        out_file.write(cur_ind + self._closed_tag())
        out_file.write("\n")

    def _open_tag(self, selfclose = ""):

        open_string = "<{}".format(self.tag)
        for key, value in self.attributes.items():
            open_string = open_string + " " + ('{}="{}"'.format(key, value))
        open_string = open_string + selfclose + ">"

        return open_string

    def _closed_tag(self):
            return "</{}>".format(self.tag)
#step 2
class Html(Element):
    #step 8
    doctype = '!DOCTYPE html'
    tag = "html"

    def _open_tag(self, cur_ind = ""):
        #step 8 addition
        open_string = cur_ind + "<{}>".format(self.doctype)
        open_string = open_string + ("\n")

        open_string = open_string + cur_ind + "<{}".format(self.tag)


        for key, value in self.attributes.items():
            open_string = open_string + " " + (cur_ind + '{}="{}"'.format(key, value))
        open_string = open_string + ">"

        return open_string

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

#step 3
class Head(Element):
    tag = "head"

class OneLineTag(Element):
    indent = " "
    def append(self, content):
        raise NotImplementedError

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.indent)
        out_file.write(cur_ind + self._open_tag())
        out_file.write(cur_ind + self.contents[0])
        out_file.write(cur_ind + self._closed_tag())
        out_file.write("\n")

class Title(OneLineTag):
    tag = "title"

#step 5
class SelfClosingTag(Element):

    def __init__(self, content=None, **attrs):
        if content is not None:
            raise TypeError("Self closing tags can't have any content")
        super().__init__(content=content, **attrs)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.indent)
        out_file.write(cur_ind + self._open_tag(' /'))
        out_file.write("\n")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

#step 6 - used OneLineTag to get on a single line
class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content = None, **attrs):
        attrs['href'] = link
        super().__init__(content, **attrs)

#step 7
class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):

    def __init__(self, number, content = None, **attrs):
       self.tag = "h" + str(number)
       super().__init__(content, **attrs)

#step 8
class Meta(SelfClosingTag):
    tag = "meta"

    def __init__(self, content=None, **attrs):
        attrs['charset'] = "UTF-8"
        super().__init__(content, **attrs)
