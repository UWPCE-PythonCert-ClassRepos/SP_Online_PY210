#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.contents = [content]
        self.attributes = {**kwargs}
        print("contents is:", self.contents)

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        open_tag = "".join(open_tag)
        return open_tag

    def _close_tag(self):
        close_tag = "</{}>".format(self.tag)
        return close_tag

    def render(self, out_file, cur_ind=""):

        out_file.write(cur_ind + self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            if content is None:
                pass
            else:
                try:
                    content.render(out_file, cur_ind + self.indent)
                    out_file.write("\n")
                except AttributeError:
                    out_file.write(cur_ind + self.indent + content)
                    out_file.write("\n")
        out_file.write(cur_ind + self._close_tag())



class Html(Element):
    tag = "html"

    def render(self, out_file,cur_ind=""):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Body(Element):
    tag = "body"
    indent = "    "


class P(Element):
    tag = "p"
    indent = "    "


class Head(Element):
    tag = "head"
    indent = "    "


class SelfClosingTag(Element):
    def render(self, outfile,cur_ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        outfile.write(tag)

    def __init__(self, content=None, indent="", **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self):
        if self.contents is not None:
            raise TypeError("You can not add content to a SelfClosingTag")


class Ul(Element):
    tag = "ul"
    indent = "        "


class Li(Element):
    tag = "li"
    indent = "            "


class Hr(SelfClosingTag):
    tag = "hr"
    indent = "        "


class Br(SelfClosingTag):
    tag = "br"
    indent = "        "


class Meta(SelfClosingTag):
    tag = 'meta charset="UTF-8"'
    indent = "        "


class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self._open_tag())
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'
    indent = "        "


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content=content, **kwargs)


class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        super().__init__(content=content, **kwargs)
        self.level = level
        self.tag = "h" + str(level)



