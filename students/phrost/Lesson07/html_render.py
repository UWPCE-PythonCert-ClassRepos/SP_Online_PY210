#!/usr/bin/env python3
### Lesson_7 - Mailroom Part 3
import copy
"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "   "

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attrb = copy.deepcopy(kwargs)


    def _create_open_tag(self,out_file,cur_ind=""):
        open_tag = ["{}<{}".format(cur_ind + self.indent,self.tag)]
        for key, value in self.attrb.items():
            open_tag.append(" " + key + "=" + value)
        open_tag.append(">\n")
        out_file.write("".join(open_tag))


    def append(self, new_content):
        self.content.append(new_content)


    def render(self, out_file,cur_ind=""):
        #out_file.write("<{}>\n".format(self.tag))
        self._create_open_tag(out_file,cur_ind)
        for content in self.content:
            try:
                content.render(out_file,cur_ind + self.indent)
            except AttributeError:
                out_file.write("{}".format(cur_ind + self.indent))
                out_file.write(content)
            out_file.write("\n")
        out_file.write("{}</{}>\n".format(cur_ind + self.indent,self.tag))


class OneLineTag(Element):
    def render(self, out_file,cur_ind=""):
        #self._create_open_tag(out_file)
         out_file.write("{}<{}>".format(self.indent + cur_ind,self.tag))
         out_file.write(self.content[0])
         out_file.write("</{}>\n".format(self.tag))


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("not allowed content")
        super().__init__(content=content,**kwargs)


    def render(self,out_file,cur_ind=""):
        open_tag = ["{}<{}".format(self.indent + cur_ind,self.tag)]
        for key, value in self.attrb.items():
            open_tag.append(" " + key + "=" + value)
        open_tag.append(" />\n")
        out_file.write("".join(open_tag))


class A(Element):
    tag = "a"
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = "h" + str(level)
        super().__init__(content, **kwargs)


class Html(Element):
    tag = "html"
    def render(self, out_file,cur_ind=""):
        out_file.write("<!DOCTYPE {}>\n".format(self.tag))
        super().render(out_file, cur_ind + self.indent)



class Body(Element):
    tag = "body"

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class Title(OneLineTag):
    tag = "title"


class title(OneLineTag):
    tag = "title"


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"

class Meta(SelfClosingTag):
    tag = "meta"
