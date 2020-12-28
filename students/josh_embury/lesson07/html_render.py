#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    indent = '    '
    tag_name = 'html'
    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(self._open_tag(cur_ind))
        #out_file.write(self._close_tag(cur_ind))
        out_file.write('\n')
        for item in self.contents:
            try:
                item.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + item)
                out_file.write('\n')
        out_file.write(self._close_tag(cur_ind))
        #out_file.write('\n')

    def _open_tag(self, cur_ind=''):
        open_tag = [cur_ind + '<' + self.tag_name]
        #for item in self.attributes.keys():
         #   open_tag.append(' ' + str(item) + '=' + '"' + str(self.attributes[item]) + '"')
        for key, value in self.attributes.items():
            open_tag.append(' ' + str(key) + '="' + str(value) + '"')
        open_tag.append('>')
        return "".join(open_tag)

    def _close_tag(self, cur_ind=''):
        return cur_ind + '</' + self.tag_name + '>\n'
# html subclass:
class Html(Element):
    tag_name = 'html'
    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind + '<!DOCTYPE html>\n')
        super().render(out_file, cur_ind)

# body subclass:
class Body(Element):
    tag_name = 'body'

# p subclass:
class P(Element):
    tag_name = 'p'

# Head subclass:
class Head(Element):
    tag_name = 'head'

# OneLineTag subclass:
class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        #out_file.write('<' + self.tag_name + '>')
        out_file.write(self._open_tag(cur_ind))
        out_file.write(self.contents[0])
        out_file.write('</' + self.tag_name + '>\n')
        #out_file.write('</' + self.tag_name + '>\n')
        #
    def append(self, new_content):
        raise NotImplementedError
# title subclass from OneLineTag:
class Title(OneLineTag):
    tag_name = 'title'

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError('SelfClosingTag cannot contain any content')
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=""):
        tag_name = self._open_tag()[:-1] + ' />\n'
        out_file.write(cur_ind)
        out_file.write(tag_name)
        #out_file.write(self._close_tag(cur_ind) + '\n')

    def append(self, *args):
        raise TypeError('You cannot add content to a SelfClosingTag')

class Hr(SelfClosingTag):
    tag_name = 'hr'

class Br(SelfClosingTag):
    tag_name = 'br'

class A(OneLineTag):
    tag_name = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag_name = 'ul'

class Li(Element):
    tag_name = 'li'

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        #self.attributes = kwargs
        self.tag_name = 'h' + str(level)
        #kwargs[self.tag_name] = level
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag_name = 'meta'