#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "
    def __init__(self, content=None, **kwargs):
        self.kw_dict = kwargs

        if content is None:
            self.contents = []
        elif isinstance(content, list) == False:
            self.contents = [content]
        else:
            self.contents = content
        pass

    def append(self, new_content):
        self.contents.append(new_content)
        pass

    def _open_tag(self):
        opening_string = "<{}".format(self.tag)
        for key, value in self.kw_dict.items():
            opening_string += ' ' + key + '="{}"'.format(value)
        opening_string += '>\n'
        return opening_string

    def _close_tag(self):
        closing_string = "</{}>\n".format(self.tag)
        return closing_string

    def render(self, out_file, cur_ind=""):
        # Loop through the list of contents
        out_file.write(cur_ind + self._open_tag())
       # out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
                out_file.write("\n")
            #out_file.write("</{}>\n".format(self.tag))

        out_file.write(cur_ind + self._close_tag())
        #out_file.write("\n")

class Html(Element):
    tag = 'html'
    def render(self, out_file, cur_ind=""):
        doc = '<!DOCTYPE html>\n'
        out_file.write(cur_ind + doc)
        super().render(out_file, cur_ind)

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(self._open_tag()[:-1])
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    def render(self, out_file, cur_ind=""):
        tag = self._open_tag()[:-2] + " />\n"
        out_file.write(tag)
    def append(selfself, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content=content,**kwargs)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = 'a'
    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h{}'.format(level)
        super().__init__(content=content,**kwargs)

class Meta(SelfClosingTag):
    tag = 'meta'