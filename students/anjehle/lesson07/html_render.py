#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self._open_tag())
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(f'{cur_ind}{self.indent}{content}\n')
        out_file.write(cur_ind + self._close_tag())

    def _open_tag(self):
        open_tag = [f"<{self.tag}"]
        for key, value in self.attributes.items():
            open_tag.append(f' {key}="{value}"')
        open_tag.append(">\n")
        return "".join(open_tag)


    def _close_tag(self):
        return f"</{self.tag}>\n"


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def append(self, content):
        raise NotImplementedError

    def render(self, out_file, cur_ind):
        out_file.write(f'{cur_ind}{self._open_tag()[:-1]}{self.contents[0]}{self._close_tag()}')


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is None:
            super().__init__(content=content, **kwargs)
        else:
            raise TypeError("SelfClosingTag can not contain any content")

    def render(self, outfile, cur_ind=""):
        tag = cur_ind + self._open_tag()[:-2] + " />\n"
        outfile.write(tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


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
    def __init__(self, level: int, content=None, **kwargs):
        self.tag = f'h{level}'
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    tag = 'meta'