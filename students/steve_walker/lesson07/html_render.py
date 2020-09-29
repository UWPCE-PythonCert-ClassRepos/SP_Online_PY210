#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.contents = [content] if content is not None else []
        self.attributes = kwargs

    def _open_tag(self, cur_ind):
        open_tag = [f"{cur_ind}<{self.tag}"]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        open_tag = "".join(open_tag)
        return open_tag

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(self._open_tag(cur_ind))
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
                out_file.write("\n")
        out_file.write(cur_ind + f"</{self.tag}>\n")


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write(f"{cur_ind}<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Head(Element):
    tag = "head"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):
        out_file.write(self._open_tag(cur_ind))
        out_file.write(self.contents[0])
        out_file.write(f"</{self.tag}>\n")

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:  # Check for special SelfClosingTags exception
            raise TypeError("SelfClosingTag cannot contain content")
        super().__init__(content=content, **kwargs)  # Else run like normal

    def render(self, out_file, cur_ind=""):
        # out_file.write(cur_ind)
        out_file.write(self._open_tag(cur_ind)[:-1] + " />\n")

    def append(self, *args):
        raise TypeError("You cannot add content to a SelfClosingTag")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Meta(SelfClosingTag):
    tag = "meta"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):

    def __init__(self, header_level, content=None, **kwargs):
        self.tag = f"h{header_level}"
        super().__init__(content, **kwargs)
