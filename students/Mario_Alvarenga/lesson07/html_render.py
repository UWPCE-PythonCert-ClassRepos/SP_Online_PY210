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
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        #print("contents is:", self.contents)
        

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

    def render(self, out_file):
        
        # loop through the list of contents:
        element_indent = cur_ind + self.indent
        out_file.write(cur_ind + self._open_tag())
        out_file.write("\n")
        
        for content in self.contents:
            try:
                content.render(out_file, element_indent)
            except AttributeError:
                out_file.write(element_indent + content)
            out_file.write("\n")
        
        out_file.write(cur_ind + self._close_tag())
        out_file.write("\n")
        
        
       
#Html subclass
class Html(Element):

    tag = 'html'

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)
           

#Body subclass
class Body(Element):
    
    tag = 'body'
    
#P subclass
class P(Element):

    tag = 'p'

#Head subclass
class Head(Element):

    tag = 'head'

#OneLineTag subclass
class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
        
    def append(self, content):
        raise NotImplementedError
            
        
#Title subclass
class Title(OneLineTag):
    
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

class A(OneLineTag):
    '''
    The A subclass extends OneLineTag class
    '''

    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)
