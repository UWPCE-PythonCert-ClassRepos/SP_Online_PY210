#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    
    tag = 'html'
    indent = '  '

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = kwargs

    def append(self, new_content):
        return self.contents.append(new_content)
        

    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        out_file.write('\n')
        ###
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent)
                out_file.write(content)
                out_file.write("\n")
        ###        
        out_file.write(cur_ind)
        out_file.write(self._close_tag())
        out_file.write('\n')
            
    def _open_tag(self):
        open = ['<{}'.format(self.tag)]
        for k, v in self.attributes.items():
            open.append(' {}="{}"'.format(k,v))
        open.append('>')
        open= ''.join(open)
        return open
        
    def _close_tag(self):
        close = '</{}>'.format(self.tag)
        return close

class Body(Element):
    tag = 'body'
    
class Html(Element):
    tag = 'html'
    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind)
        out_file.write('<DOCTYPE html>')
        out_file.write('\n')
        super().render(out_file, cur_ind)
    
class P(Element):
    tag = 'p'
    
class Head(Element):
    tag = 'head'
    
class OneLineTag(Element):
    def render(self, out_file, cur_ind = ''):
        out_file.write(cur_ind + self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
        out_file.write('\n')
        
        
    def append(self, content):
        raise NotImplementedError
        
class Title(OneLineTag):
    tag = 'title'
    
    
class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content,**kwargs)
    
class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can't contain content")
        super().__init__(content=content, **kwargs)
        
    def render(self, out_file, cur_ind=''):
        tag = self._open_tag()[:-1] + " />"
        out_file.write(cur_ind)
        out_file.write(tag)
        out_file.write('\n')
        
    def append(self, *args, **kwargs):
        raise TypeError("Can't append to SelfClosingTag")
    
class Hr(SelfClosingTag):
    tag = 'hr'
    
class Br(SelfClosingTag):
    tag = 'br'
    
        
class Ul(Element):
    tag = 'ul'
    
class Li(Element):
    tag = 'li'

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = ('h{}'.format(level)) # inserts the number - 1,2,etc... - after h
        super().__init__(content,**kwargs)
        
class Meta(SelfClosingTag):
    tag = 'meta'
    
    
    