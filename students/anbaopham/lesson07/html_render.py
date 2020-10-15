#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = ""
    def __init__(self, content = None, **kwargs):
        if content is not None:
            self.contents = [content]
        else:
            self.contents = []
        self.attributes = kwargs


    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        for content in self.contents:
            out_file.write(cur_ind)
            open_tag = ["<{}".format(self.tag)]

            for k,v in self.attributes.items():
                open_tag.append(f'{k}="{v}"')
            for i in range(len(open_tag)):
                if i < len(open_tag)-1:
                    open_tag[i] = open_tag[i] + " "
            open_tag.append(">\n")

            out_file.write("".join(open_tag))
            # out_file.write((cur_ind+ self.indent))
            try:
                content.render(out_file, (cur_ind + self.indent))
            except AttributeError:
                out_file.write(cur_ind)
                out_file.write(content)


        out_file.write("\n")
        # out_file.write(cur_ind)
        out_file.write("{}</{}>\n".format(cur_ind, self.tag))

class Html(Element):
    indent = "   "
    def render(self, out_file,cur_ind=""):
        cur_ind = self.indent
        tag = "!DOCTYPE html"
        #open_tag = ["{}<{}".format(cur_ind, self.tag)]
        out_file.write("{}<{}>\n".format(cur_ind, tag))

        self.tag = "html"
        super().render(out_file, cur_ind)


class Body(Element):
    tag = "body"
    indent = "   "
class P(Element):
    tag = "p"
    indent = "   "
class Head(Element):
    tag = "head"
    indent = "   "

class OneLineTag(Element):
    indent = ""
    def render(self, out_file,cur_ind=""):
        out_file.write((cur_ind))
        tag = self._open_tag()
        out_file.write(tag)
        out_file.write(self.contents[0])
        # out_file.write((cur_ind))

        out_file.write(self._close_tag())

    def _open_tag(self):
        if self.tag == 'a':
            open_tag = ["<{} ".format(self.tag)]
        else:
            open_tag = ["<{}>".format(self.tag)]
        for k,v in self.attributes.items():
            open_tag.append(f'{k}="{v}"')
        for i in range(len(open_tag)):
            if i < len(open_tag)-1:
                open_tag[i] = open_tag[i] + " "
        str_tag = ""
        for i in open_tag:
            str_tag += i
        return str_tag

    def _close_tag(self):
        return "</{}>\n".format(self.tag)

    def append(self, new_content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"
    indent = "   "

class SelfClosingTag(Element):
    indent = ""
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, new_content):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, out_file,cur_ind=""):
        out_file.write(cur_ind)
        tag = self._open_tag() + " />\n"
        out_file.write(tag)
        # out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, (cur_ind + self.indent))
            except AttributeError:
                # out_file.write((cur_ind + self.indent))
                out_file.write(content)

            # out_file.write("\n")
            out_file.write(cur_ind)
            out_file.write(self._close_tag())
            out_file.write("\n")

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for k,v in self.attributes.items():
            open_tag.append(f'{k}="{v}"')
        for i in range(len(open_tag)):
            if i < len(open_tag)-1:
                open_tag[i] = open_tag[i] + " "
        str_tag = ""
        for i in open_tag:
            str_tag += i
        return str_tag

    def _close_tag(self):
        return "</{}>\n".format(self.tag)

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class Ul(Element):
    tag = "ul"
    indent = "   "

class Li(Element):
    tag = "li"
    indent = "   "

class A(OneLineTag):
    tag = 'a'
    indent = "   "
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):
    tag ="h"

    def __init__(self, level, content = None, **kwargs):
        level = str(level)
        self.tag = self.tag + level
        super().__init__(content, **kwargs)
class D(OneLineTag):
    tag = "!"

class Meta(SelfClosingTag):
    tag = "meta"
    indent = "   "
