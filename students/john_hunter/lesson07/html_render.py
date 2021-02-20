#!/usr/bin/env python3
"""
A class-based system for rendering html.
John Hunter PY210
"""

# This is the framework for the base class
class Element(object):
    """
    base class for all elements. This class will be subclassed for html element types.
    """
    
    tag = "html"
    indent = "    "
    #contents = []
    
    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            #pass
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
    
    def render(self, out_file, cur_ind=""):#TODO clean up
        """
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        "".join(open_tag)
        """
        element_indent = cur_ind + self.indent
        out_file.write(cur_ind + self._open_tag())
        out_file.write("\n")
        
        for content in self.contents:
            try:
                content.render(out_file, element_indent)#TODO cur_ind = element_indent?
            except AttributeError:
                out_file.write(element_indent + content)
            out_file.write("\n")
        
        out_file.write(cur_ind + self._close_tag())
        out_file.write("\n")
        #"</{}>".format(self.tag)
        
class Html(Element):
    '''
    The Html sub-class extends the element abstract base class
    '''
    tag = 'html'
    
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)
           
class Body(Element):
    '''
    The body sub-class extends the element abstract base class
    '''
    tag = 'body'

class P(Element):
    '''
    The P sub-class extends the element abstract base class
    '''
    tag = 'p'
    
class Head(Element):
    '''
    The Head sub-class extends the element abstract base class
    '''
    tag = 'head'    
    
class OneLineTag(Element):
    '''
    The Head sub-class extends the element abstract base class
    '''
    tag = 'head'
    
    def render(self, out_file, cur_ind=""):
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    '''
    The Title subclass extends subelement class
    '''

    tag = "title"

class SelfClosingTag(Element):
    '''
    The SelfClosingTag subclass extends Element class
    '''

    tag = "title"
    
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    
    def render(self, outfile, cur_ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        outfile.write(tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"
 
class A(OneLineTag):
    '''
    The A subclass extends OneLineTag class
    '''

    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)        
        
class H(OneLineTag):

    '''
    The H subclass extends OneLineTag class
    '''

    tag = 'h'

    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h{}'.format(level)
        super().__init__(content=content,**kwargs)

class Meta(SelfClosingTag):
    tag = "meta"
