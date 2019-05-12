#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    
    tag = 'html'


    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = kwargs

    def append(self, new_content):
        return self.contents.append(new_content)
        

    def render(self, out_file, cur_ind=''):
        out_file.write(self._open_tag(cur_ind))
        for content in self.contents:
            #out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write(self._close_tag(cur_ind))
            
    def _open_tag(self, cur_ind=""):
        open = ['{}<{}'.format(cur_ind, self.tag)]
        for k, v in self.attributes.items():
            open.append(' {}="{}"'.format(k,v))
        open.append('>')
        open= ''.join(open)
        return open
        
    def _close_tag(self, cur_ind=""):
        close = '</{}>\n'.format(self.tag)
        return close

class Body(Element):
    tag = 'body'
    
class Html(Element):
    tag = 'html'
    
class P(Element):
    tag = 'p'
    
class Head(Element):
    tag = 'head'
    
class OneLineTag(Element):
    def render(self, out_file, cur_ind = ''):
        # open_tag = ["<{}".format(self.tag)]
        # open_tag.append(">")
        # out_file.write("".join(open_tag))
        # out_file.write(self.contents[0])
        # out_file.write("</{}>\n".format(self.tag))
        out_file.write(self._open_tag(cur_ind))
        out_file.write(self.contents[0])
        out_file.write("</{}>".format(self.tag))
        out_file.write('\n')
        
        
    def append(self, content):
        raise NotImplementedError
        
class Title(OneLineTag):
    tag = 'title'
    
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
    
class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content,**kwargs)
        
        
