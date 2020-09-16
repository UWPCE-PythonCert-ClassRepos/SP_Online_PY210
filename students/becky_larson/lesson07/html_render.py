#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        # loop through the list of contents: 
        open_tag = ["<{}".format(self.tag)]
        for k, v in self.attributes.items():
            open_tag.append(' {}="{}"'.format(k,v))
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("</{}>\n".format(self.tag))

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


class Html(Element):

    tag = 'html'

#    def render(self, out_file):
#        out_file.write("<{}>\n".format(self.tag))
#        for content in self.contents:
#            out_file.write(content)
#        out_file.write("</{}>\n".format(self.tag))


class Body(Element):

    tag = 'body'

class P(Element):

    tag = 'p'

class Head(Element):

    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError
    
class Title(OneLineTag):

    tag = 'title'


class SelfClosingTag(Element):
    # belarson -- stopped in step 5. not sure where this goes. 
    #  https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/html_renderer_tutorial.html#html-renderer-tutorial
    
    def render(self, out_file):
        # loop through the list of contents:
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(self._close_tag())
        out_file.write("\n")


class Hr(SelfClosingTag):
    tag = "hr"



