#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class

class Element:
    tag = 'html'
    def __init__(self, content=None, **kwargs):
        self.attr = kwargs
        print (self.attr)
        self.content = []
        if content:
            self.content.append(content)

    def append(self, new_content):
        self.content.append(new_content)

    def attr_maker(self):
        attr_string = " ".join(['{}="{}"'.format(k, v) for k, v in self.attr.items()])
        if attr_string.strip():
            open_tag = "<{} {}>".format(self.tag, attr_string.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self.tag)
        return open_tag, close_tag


    def render(self, out_file):
        open_tag, close_tag = self.attr_maker()
        out_file.write("{}".format(open_tag))
        for item in self.content:
            if hasattr(item, "render"):
                item.render(out_file)
            else:
                out_file.write(item)
                out_file.write("\n")
        out_file.write("{}".format(close_tag))



class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        for item in self.content:
            out_file.write(item)
        out_file.write("</{}>".format(self.tag))

class Title(OneLineTag):
    tag = 'title'

class Head(OneLineTag):
    tag = 'head'


class SelfClosingTag(Element):

    def append(self, new_content):
        raise TypeError("You can not add content to a self closing tag")

    def render(self, out_file):
        open_tag = self.attr_maker()[0]
        out_file.write(open_tag.replace(">", " />"))

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(Element):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = "H"

    def __init__(self, level, content=None, **kwargs):
        self.tag = "h" + str(int(level))
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):

    tag = "meta"

