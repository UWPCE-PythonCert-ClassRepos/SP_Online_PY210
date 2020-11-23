#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    """Base Element Object"""
    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.contents = [content] if content else []
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self, cur_ind):
        open_tag = ["{}<{}".format(cur_ind, self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(" {}=\"{}\"".format(key, value))
        open_tag.append(">")
        return "".join(open_tag)

    def _close_tag(self, cur_ind):
        return '{}</{}>\n'.format(cur_ind, self.tag)

    def render(self, out_file, cur_ind=''):
        out_file.write(self._open_tag(cur_ind))
        out_file.write('\n')
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write('{}{}'.format(cur_ind + self.indent ,content))
                out_file.write('\n')
        out_file.write(self._close_tag(cur_ind))

class Html(Element):
    """HTML Object"""
    tag = 'html'

    def _open_tag(self, cur_ind):
        open_tag = ["{}<!DOCTYPE {}>\n<{}".format(cur_ind, self.tag,self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(" {}=\"{}\"".format(key, value))
        open_tag.append(">")
        return "".join(open_tag)

class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class OneLineTag(Element):
    tag = 'head'

    def append(self, content):
        raise NotImplementedError


    def render(self, out_file, cur_ind=''):
        out_file.write(self._open_tag(cur_ind))
        out_file.write(self.contents[0])
        out_file.write(self._close_tag(cur_ind=''))


class Title(OneLineTag):
    tag = 'title'


class A(OneLineTag):

    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h{:d}'.format(level)
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, outfile, cur_ind=''):
        tag = self._open_tag(cur_ind).replace(">", " />")
        outfile.write(tag)
        outfile.write('\n')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class Meta(SelfClosingTag):
    tag = 'meta'


