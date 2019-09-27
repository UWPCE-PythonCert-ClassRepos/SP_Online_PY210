#!/usr/bin/env python3

# Element #
###########

class Element(object):
    tag = "html" # abstract tag

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else: self.content = [content]
        #print("content is: ", self.content)
        self.kwargs = kwargs

    def _open_tag(self):
        open_tag = [f"<{self.tag}"]
        if self.kwargs == {}:
            pass
        else:
            for key, value in self.kwargs.items():
                my_string = (f' {key}="{value}"')
                open_tag.append(my_string)
        open_tag.append(">")
        return ("".join(open_tag))

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.content:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write((f"</{self.tag}>"))

class Html(Element):
    tag = "html"

    def render(self, out_file):
        out_file.write("<!DOCTYPE html>\n")
        Element.render(self, out_file)

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

# OneLineTag #
##############

class OneLineTag(Element):

    def render(self, out_file):
        out_file.write(self._open_tag())
        for content in self.content:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(f"</{self.tag}>")

    def append(self, new_content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class H(OneLineTag):

    def __init__(self, count, content=None, **kwargs):
        self.tag = "h" + str(count)
        super().__init__(content, **kwargs)

# SelfClosingTag #
##################

class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    
    def render(self, outfile):
        tag = self._open_tag()[:-1] + " />"
        outfile.write(tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class Meta(SelfClosingTag):
    tag = "meta"
