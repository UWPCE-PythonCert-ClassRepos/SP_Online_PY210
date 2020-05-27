#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for keys, values in self.attributes.items():
            open_tag.append(' {}="{}"'.format(keys, values))
        open_tag.append(">")
        return("".join(open_tag))

    def close_tag(self):
        return("</{}>".format(self.tag))

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
                out_file.write("\n")
        out_file.write(cur_ind + self.close_tag())
        out_file.write("\n")

class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + '<!DOCTYPE html>\n')
        super().render(out_file, cur_ind)

class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.open_tag())
        out_file.write(self.contents[0])
        out_file.write(self.close_tag())
        out_file.write('\n')

    def append(self, content):
        raise NotImplementedError

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=""):
        tag = self.open_tag()[:-1] + " />\n"
        out_file.write(tag)

    # Ensure no content will be appended
    def append(self, *args, **kwargs):
        raise TypeError('Cannot append content to SelfClosingTag')

class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = "h{}".format(level)
        super().__init__(content, **kwargs)

#simple subclass
class Head(Element): #3
    tag = "head"

class Title(OneLineTag): #3
    tag = 'title'

class Body(Element): #2-B
    tag = "body"

class P(Element): #2-B
    tag = "p"

class Hr(SelfClosingTag):#5
    tag = "hr"

class Br(SelfClosingTag): #5
    tag = "br"

class Ul(Element): #7
    tag = 'ul'

class Li(Element): #7
    tag = 'li'

class Meta(SelfClosingTag):#8
    tag = "meta"
