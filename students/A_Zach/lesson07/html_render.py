#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = "    "
    def __init__(self, content=None, **kwargs):
        
        self.kwg_dict = kwargs
        
        if content is None:
            self.contents = []
        else:           
            self.contents = [content]
        pass

    def append(self, new_content):
        self.contents.append(new_content)
        pass
    
    def _open_tag(self):
        open_string = f"<{self.tag}"
        for key, value in self.kwg_dict.items():
            open_string += ' ' + key + '=' + f'"{value}"'
        open_string += ">"
        return open_string

    def _close_tag(self):
        close_string = f"</{self.tag}>"
        return close_string

    def render(self, out_file, cur_ind=""):
        #loop through list of contents
        out_file.write(cur_ind + self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
            out_file.write("\n")
        out_file.write(cur_ind + self._close_tag())
        out_file.write("\n")

#Create a subclass of Element for <body> and <p>
class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'
    
class Html(Element):
    tag = 'html'
    def render(self, out_file, cur_ind=""):
        doc_type = '<!DOCTYPE html>\n'
        out_file.write(cur_ind + doc_type)
        super().render(out_file, cur_ind)

class Head(Element):
    tag = 'head'

class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):
 
        out_file.write(cur_ind + self._open_tag())
        out_file.write(cur_ind + self.contents[0])
        out_file.write(cur_ind + self._close_tag())
    
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    
    def render(self, out_file, cur_ind=""):
        tag = self._open_tag()[:-1] + " />"
        out_file.write(cur_ind + tag)
    
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")
    
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
        
class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"
    
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        self.tag = f"h{level}"
        super().__init__(content, **kwargs)
    
class Meta(SelfClosingTag):
    tag = 'meta'