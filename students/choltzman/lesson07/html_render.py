#!/usr/bin/env python3


class Element:
    tag = "html"
    indent = 4

    def __init__(self, content=None, **kwargs):
        self.contents = [content] if content else []
        self.args = kwargs

    def _open_tag(self):
        """Build the opening tag."""
        # initial string variable
        s = f"{self.tag}"

        # loop through args
        for key, val in self.args.items():
            s += f" {key}=\"{val}\""

        return s

    def append(self, new_content):
        """Append a string to the element's content."""
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=0):
        """Build the actual HTML."""
        # add opening tag
        out_file.write(f"{cur_ind * ' '}<{self._open_tag()}>\n")

        # add contents
        for content in self.contents:
            if isinstance(content, Element):
                content.render(out_file, (self.indent + cur_ind))
            else:
                out_file.write(f"{(self.indent + cur_ind) * ' '}{content}\n")

        # add closing tag
        out_file.write(f"{cur_ind * ' '}</{self.tag}>\n")


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=0):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file, cur_ind=0):
        # add opening tag
        out_file.write(f"{cur_ind * ' '}<{self._open_tag()}>")

        # add contents
        for content in self.contents:
            if isinstance(content, Element):
                content.render(out_file)
            else:
                out_file.write(f"{content}")

        # add closing tag
        out_file.write(f"</{self.tag}>\n")


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def render(self, out_file, cur_ind=0):
        out_file.write(f"{cur_ind * ' '}<{self._open_tag()} />\n")


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
    tag = "h"

    def __init__(self, level, content=None, **kwargs):
        self.tag = f"{self.tag}{level}"
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    tag = "meta"
