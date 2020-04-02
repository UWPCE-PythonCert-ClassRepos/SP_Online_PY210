#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag_name = 'html'

    def __init__(self, content=None, **kwargs):
        if kwargs:
            self.attributes_dict = kwargs
        else:
            self.attributes_dict = {}
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def open_tag(self):
        tag_str = [f'<{self.tag_name}']
        for key, val in self.attributes_dict.items():
            tmp_str = f' {key}="{val}"'
            tag_str.append(tmp_str)
        tag_str.append('>')
        return "".join(tag_str)

    def close_tag(self):
        return f'</{self.tag_name}>\n'

    def render(self, out_file):
        out_file.write(self.open_tag())
        out_file.write('\n')
        for content in self.content:
            if isinstance(content, Element):# string element
                content.render(out_file)
            elif isinstance(content, str):
                out_file.write(content)
                out_file.write('\n')
            else:# unknown objects
                raise(AttributeError, "Unknown object.")
        out_file.write(self.close_tag())

# Define subclasses 'Html', 'Body', 'P'
class Html(Element):
    tag_name = 'html'

    def render(self, out_file):
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file)

class Body(Element):
    tag_name = 'body'

class P(Element):
    tag_name = 'p'

class Head(Element):
    tag_name = 'head'

class OneLineTag(Element):
    tag_name = 'title'

    def append(self, new_content):
        if len(self.content) == 0:
            self.content.append(new_content)
        else:
            raise AttributeError("OneLineTag only has one content.")

    def render(self, out_file):
        out_file.write(self.open_tag())
        # OneLineTag only allow single string content.
        if isinstance(self.content[0], str):# string element
            out_file.write(self.content[0])
            out_file.write(self.close_tag())
        else:
            print(f"content:{self.content}")
            raise AttributeError("OneLineTag doesn't allow Object decalration")


class Title(OneLineTag):
    tag_name = 'title'

class SelfClosingTag(Element):
    tag_name = 'hr'

    def __init__(self, content=None, **kwargs):
        if content is None:
            super().__init__(**kwargs)
        else:
            raise TypeError("SelfClosingTag doesn't allow content paramter.")

    def render(self, out_file):
        #print(f"TT:{self.open_tag()}.")
        out_file.write(self.open_tag()[:-1])
        out_file.write(' />\n')


class Hr(SelfClosingTag):
    tag_name = 'hr'

class Br(SelfClosingTag):
    tag_name = 'br'

class A(Element):
    tag_name = 'a'

    def __init__(self, link=None, content=None, **kwargs):
        if link is None:
            self.link = 'https://www.python.org/'
        else:
            self.link = link
        if content is None:
            self.content = ['link to python']
        else:
            self.content = [content]
        super().__init__(content, **kwargs)

    def render(self, out_file):
        out_file.write(f'<{self.tag_name} href="{self.link}">')
        out_file.write(f'{" ".join(self.content)}')
        out_file.write(f'</a>\n')

class H(OneLineTag):
    tag_name = 'h'

    def __init__(self, Tag_flag=-1, content=None, **kwargs):
        if Tag_flag == -1:
            raise (AttributeError, "H tag needs an integer \
                   argument for the header level.")
        else:
            if str(Tag_flag).isdigit():
                self.tag_name = f'{self.tag_name}{Tag_flag}'
            else:
                raise (ValueError, "H tag needs an integer for header level.")
        super().__init__(content, **kwargs)


class Ul(Element):
    tag_name = 'ul'

class Li(Element):
    tag_name = 'li'

class Meta(SelfClosingTag):
    tag_name = 'meta'
