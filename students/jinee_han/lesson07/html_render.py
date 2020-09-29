#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    '''
    The element base class
    '''

    tag = "html"
    indent = "  "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]


    def append(self, new_content):
        self.contents.append(new_content)


    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        return "".join(open_tag)


    def _close_tag(self):
        return "</{}>".format(self.tag)


    def render(self, out_file, cur_ind=""):
        new_indent = cur_ind + self.indent
        out_file.write(cur_ind+self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind = new_indent)
            except AttributeError:
                out_file.write(new_indent + content)
            out_file.write("\n")
        out_file.write(cur_ind + self._close_tag())


class Body(Element):

    '''
    The body class, extends base element
    '''

    tag = 'body'


class Html(Element):

    '''
    The Html class, extends base element
    '''

    tag = 'html'

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class P(Element):

    '''
    The P class, extends base element
    '''

    tag = 'p'


class Head(Element):

    '''
    The Head class, extends base element
    '''

    tag = 'head'


class OneLineTag(Element):

    '''
    One Line Tag class, extends element base class
    '''

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())


    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):

    '''
    The Title class, extends base OneLineTag
    '''

    tag = "title"


class SelfClosingTag(Element):

    '''
    The self closing tag class, extends base element
    '''

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)


    def render(self, out_file, cur_ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(cur_ind + tag)


    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Hr(SelfClosingTag):

    '''
    The Hr class, extends self closing tag
    '''

    tag = "hr"


class Br(SelfClosingTag):

    '''
    The Br class, extends self closing tag
    '''

    tag = "br"


class A(OneLineTag):

    '''
    The A class, extends one line tag
    '''

    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul(Element):

    '''
    The Ul class, extends element base
    '''

    tag = "ul"


class Li(Element):

    '''
    The Li class, extends element base
    '''

    tag = "li"


class H(OneLineTag):

    '''
    The H class, extends one line tag base
    '''

    tag = 'h'

    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h{}'.format(level)
        super().__init__(content=content,**kwargs)


class Meta(Element):
    '''
    The Meta class, extends element base
    '''
    def __init__(self, charset):
        self.charset = charset


    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + '<meta charset="{}" />\n'.format(self.charset))

