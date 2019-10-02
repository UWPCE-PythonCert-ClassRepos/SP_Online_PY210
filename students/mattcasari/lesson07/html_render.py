#!/usr/bin/env python3
""" Lesson 7, Excercise 1

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/html_renderer.html

Description:
    A class-based system for rendering html.
   

"""

# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "  "

    def __init__(self, content=None, **kwargs):
        if content:
            self.contents = [content]
        else:
            self.contents = []
        self.attributes = {}
        self.attributes.update(kwargs)

    def _open_tag(self, ind=""):
        open_tag = [f"{ind}<{self.tag}"]
        print(self.attributes)
        for key, value in self.attributes.items():
            open_tag.append(f' {key}="{value}"')
        open_tag.append(">")
        open_tag = "".join(open_tag)

        return open_tag

    def _close_tag(self, ind=""):
        close_tag = [f"{ind}</{self.tag}>"]
        return "".join(close_tag)

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, ind=""):
        out_file.write(self._open_tag(ind) + "\n")
        for content in self.contents:
            try:
                content.render(out_file, ind + self.indent)
            except AttributeError:
                out_file.write(self.indent + ind + content)
                out_file.write("\n")
        out_file.write(self._close_tag(ind) + "\n")


class Html(Element):
    tag = "html"

    def render(self, out_file, ind=""):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, ind="")


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def append(self, content):
        raise NotImplementedError

    def render(self, out_file, ind=""):
        out_file.write(self._open_tag(ind))
        out_file.write(self.contents[0])
        out_file.write(self._close_tag(ind) + '\n')


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag cannot contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You cannot add content to a SelfClosingTag")

    def render(self, out_file, ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(ind + tag)


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content, **kwargs):
        kwargs["href"] = link
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = f"h{level}"
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    tag = "meta"
