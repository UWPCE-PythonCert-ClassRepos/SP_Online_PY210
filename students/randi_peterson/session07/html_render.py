#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag ='html'
    indent = "   "
    def __init__(self, content=None, **kwargs):
        self.kw_dict = kwargs

        if content is None:
            self.contents = []
        elif isinstance(content, list)==False:
            self.contents = [content]
        else:
            self.contents = content
        #print("contents is:",self.contents)

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        assembled_string = "<{}".format(self.tag)
        for key, value in self.kw_dict.items():
            assembled_string += ' ' + key + '=' + '"{}"'.format(value)

        assembled_string += ">\n"
        return assembled_string

    def _close_tag(self):
        assembled_close = "</{}>\n".format(self.tag)
        return assembled_close

    def render(self, out_file,cur_ind=""):
        #loop through list of contents
        out_file.write(cur_ind + self._open_tag())

        for content in self.contents:
            try:
                content.render(out_file,cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
                out_file.write("\n")

        out_file.write(cur_ind + self._close_tag())

class Body(Element):
    tag = 'body'

class Html(Element):
    tag = 'html'
    def render(self, out_file,cur_ind=""):
        doc = "<!DOCTYPE html>\n"
        out_file.write(cur_ind + doc)
        super().render(out_file,cur_ind)

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    pass
    def render(self, out_file,cur_ind=""):
        #loop through list of contents
        out_file.write(cur_ind + self._open_tag()[:-1])
        out_file.write(cur_ind + self.contents[0])
        out_file.write(cur_ind + self._close_tag())

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)


    def _open_tag(self):
        return super()._open_tag()[:-2]

    def _close_tag(self):
        return " />\n".format(self.tag)

    def append(self, *args):
        raise TypeError("SelfClosingTags do not accept content additions")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content=None,**kwargs):
        super().__init__(content, href=link,**kwargs)

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
         self.tag = "h{}".format(level)
         super().__init__(content,**kwargs)

class Meta(SelfClosingTag):
    tag = 'meta'