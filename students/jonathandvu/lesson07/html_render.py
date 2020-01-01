#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = '    '

    def __init__(self, content=None, **kwargs):
        if content:
            self.contents = [content]
        else:
            self.contents = []
        self.attributes = kwargs
        pass

    def append(self, new_content):
        self.contents.append(new_content)
        pass

    def render_attribute(self):
        output_text = ''
        for key, value in self.attributes.items():
            output_text += ' {}="{}"'.format(key, value)
        return output_text

    def render(self, out_file, cur_ind=""):
        # loop through the list of contents:
        out_file.write(cur_ind + "<{}".format(self.tag) + self.render_attribute() + ">\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
        out_file.write(cur_ind + "</{}>\n".format(self.tag))


class Body(Element):
    tag = 'body'


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=""):
        # loop through the list of contents:
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)

class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    tag = 'OneLineTag'

    def render(self, out_file, cur_ind=""):
        print(self.contents[0])
        out_file.write(cur_ind + "<{}".format(self.tag) + self.render_attribute() + ">" + self.contents[0] + "</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<{}".format(self.tag) + self.render_attribute() + " />\n")


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class H(OneLineTag):
    def __init__(self, tier, content, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = 'h{}'.format(str(tier))

class Meta(SelfClosingTag):
    tag = 'meta'