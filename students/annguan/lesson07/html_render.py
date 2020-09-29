#!/usr/bin/env python3

### Lesson 7 HTML Renderer

class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self,content=None,*kwargs):
        self.content = []
        if content:
            self.append(content)
        self.attributes = kwargs

    def append(self,more_content):
        self.content.append(more_content)

    def open__tag(self, cur_ind = ""):
        open_tag = "<{}>".format(self.tag)
        return open_tag
        open_tag = ["{}<{}".format(cur_ind,self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}'.format(key.value))
            open_tag = "".join(open_tag)
            return open_tag

    def close__tag(self, cur_ind = ""):
        return "{}</{}>".format(cur_ind, self.tag)

    def render(self, file_out, cur_ind = ""):
        file_out.write(self.open__tag(cur_ind))
        file_out.write("\n")
        for text in self.content:
            try:
                text.render(file_out, cur_ind + self.indent)
            except AttributeError:
                file_out.write(cur_ind + self.indent + text)
                file_out.write("\n")
        file_out.write(self.close__tag(cur_ind))
        file_out.write("\n")

class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        file_out.write(self.open__tag(cur_ind))
        file_out.write(self.contents[0])
        file_out.write("</{}>\n".format(self.tag))

class Html(Element):
    tag = "html"

    def render(self,file_out,cur_ind = ""):
        file_out.write(cur_ind + "<!DOCTYPE html>\n")
        super().redner(file_out,cur_ind)

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class SelfClosingTag(Element):
    def __init_(self,content=None,*kwargs):
        if content is not None:
            raise TypeError("Content to SelfClosingTag not allowed")
        super().__init__(content=content,*kwargs)

    def render(self,file_out, cur_ind=""):
        tag = self.open__tag()[:-1] + "/>\n"
        file_out.write(cur_ind)
        file_out.write(tag)

    def append(self,*args, **kwargs):
        raise TypeError("Content to SelfClosingTag not allowed")

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class Meta(SelfClosingTag):
    tag = "meta"

class Title(OneLineTag):
    tag = "title"
    
class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, *kwargs):
        kwargs['href'] = link
        Element.__init__(self,content,*kwargs)
        
class H(OneLineTag):
    def __init__(self, level, content=None, *kwargs):
        self.tag = "h{}".format(level)
        super().__init__(content, *kwargs)