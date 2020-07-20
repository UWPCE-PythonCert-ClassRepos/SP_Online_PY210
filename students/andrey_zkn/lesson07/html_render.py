#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = '    '    

    def __init__(self, content=None, **kwargs):
        self.content = []
        if content: 
            self.append(content)
#        print("contents is:", self.content)
        self.attributes = kwargs

    def append(self, new_content):
        self.content.append(new_content)
		
    def _open_tag(self, cur_ind=''):
        open_tag = ['{}<{}'.format(cur_ind, self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append('>')
        open_tag = "".join(open_tag)
        return open_tag

    def _close_tag(self, cur_ind=''):
        return '{}</{}>'.format(cur_ind, self.tag)

			
    def render(self, out_file, cur_ind = ''):
        out_file.write(self._open_tag(cur_ind))
        out_file.write('\n')
        for content in self.content:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
                out_file.write('\n')
        out_file.write(self._close_tag(cur_ind))
        out_file.write('\n')			

class Html(Element):
    tag = 'html'
	
    def render(self, out_file, cur_ind = ''):
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file, cur_ind='')


class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'
	
	
class OneLineTag(Element):

    def render(self, out_file, cur_ind=''):
#        out_file.write("<{}>".format(self.tag))
        out_file.write(self._open_tag(cur_ind))
        out_file.write(self.content[0])
        out_file.write('</{}>\n'.format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'
	

class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError('SelfClosingTag can not contain any content')
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=''):
        tag = self._open_tag()[:-1] + ' />\n'
        out_file.write(cur_ind)
        out_file.write(tag)

    def append(self, *args):
        raise TypeError('You can not add content to a SelfClosingTag')
	
	
class Hr(SelfClosingTag):
    tag = 'hr'
	

class Br(SelfClosingTag):
    tag = 'br'
	
	
class Meta(SelfClosingTag):
    tag = 'meta'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content,**kwargs)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h{}'.format(level)
        super().__init__(content, **kwargs)