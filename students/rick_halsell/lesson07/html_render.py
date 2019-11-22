#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"


    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.contents = [content]
        else:
            self.contents = []
        print("contents is:", self.contents)

        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(f' {key}="{value}"')
        open_tag.append(">")
        return ''.join(open_tag)

    def _close_tag(self):
        return '</{}>'.format(self.tag)

    def render(self, out_file):
    # loop through the list of contents:

        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
                out_file.write("</{}>\n".format(self.tag))


class Html(Element):

    tag = 'html'


class Body(Element):

    tag = 'body'


class P(Element):

    tag = 'p'


class Head(Element):

    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=''):
        tag = self._open_tag()[:-1] + ' />\n'
        file_out.write(cur_ind)
        file_out.write(tag)

    def _open_tag(self):
        return super()._open_tag()[:-2]

    def _close_tag(self):
        return " />\n".format(self.tag)
class Hr(SelfClosingTag):

    tag = "hr"
