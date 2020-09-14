#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""
# This is the framework for the base class


class Element(object):

    tag = "html"
    indent = " "

    def __init__(self, content=None, **kwargs):
        self.contents = [content]
        self.attributes = (kwargs)

        print("contents is:", self.contents)

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):

        open_tag = [cur_ind + "<{}".format(self.tag)]

        for key, value in self.attributes.items():
            open_tag.append(" " + key + "=\"" + str(value) + "\"")
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        for content in self.contents:
            if content is not None:
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(Element.indent)
                    out_file.write(content)
                out_file.write("\n")                          
        out_file.write(cur_ind + "</{}>\n".format(self.tag))


# Don't know how to make "doctype" appear before Element
# Can figure out how to finish 'def test_multiple_indent():'
class Doctype(Element):
    tag = "DOCTYPE"
    
    def render(self, out_file, cur_ind=""):
        
        html_tag = (cur_ind + self.tag+" "+Element().tag)
        out_file.write("<!{}>\n".format(html_tag))


class Body(Element):
    tag = 'body'
    
class P(Element):
    tag = "p"

class Html(Element):
    tag = "html"
    
class Head(Element):
    tag = "head"

class OneLineTag(Element):
    
    def render(self, out_file, cur_ind=""):
        
        out_file.write(SelfClosingTag()._open_tag())
        out_file.write("{}".format(self.tag))
        for key, value in self.attributes.items():
            out_file.write(" "+key+"=\""+str(value)+"\"")

        out_file.write(SelfClosingTag()._close_tag())
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
        print(out_file)

class Title(OneLineTag):
    
    tag = "title"

    def render(self, out_file, cur_ind=""):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("</{}>\n".format(self.tag))

class SelfClosingTag(Element):   

    def render(self, out_file, cur_ind=""):
        try:
            out_file.write(self._open_tag()+"{} ".format(self.tag))
            for key, value in self.attributes.items():
                out_file.write(key+"=\""+str(value)+"\""+" ")
        except AttributeError:
            out_file.write("\n")
        out_file.write("/"+self._close_tag())
        out_file.write("\n")

    def _open_tag(self):
#        return "<{} ".format(self.tag)
        return ("<")

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def _close_tag(self):
        return (">")

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

# Don't know how to program "meta" to appear above title
class Meta(SelfClosingTag):
    tag = "meta"

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

class Li(Ul):
    tag = "li"

class H(OneLineTag):
    tag = "h"


    def __init__(self, index, content=None, **kwargs):

        self.tag = self.tag + str(index)
        
        super().__init__(content)
















