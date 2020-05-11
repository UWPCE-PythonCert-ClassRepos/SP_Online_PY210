#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = '    '
    indlvl = 0

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.kwargs = kwargs
        if content is not None:
            self.content = [content, '\n']

    def append(self, content):
        self.content.append(content)

    def front_tag(self):
        k = ''
        for key in self.kwargs:
            k = k + ' ' + key + "='" + str(self.kwargs[key]) + "'"
        self.content.insert(0, '<' + self.tag + k + '>')

    def back_tag(self):
        self.content.insert(len(self.content), '</' + self.tag + '>')

    def render(self, out_file, cur_ind=''):
        self.cur_ind = cur_ind + (self.indent*self.indlvl)
        self.front_tag()
        self.content.insert(1, '\n')
        self.back_tag()
        self.content.insert(len(self.content), '\n')
        for contentlet in self.content:
            try:
                contentlet.render(out_file)
            except AttributeError:
                if contentlet == '\n':
                    out_file.write(contentlet)
                elif contentlet[0] == '<':
                    out_file.write(self.cur_ind + contentlet)
                else:
                    out_file.write(self.cur_ind + self.indent + contentlet)


# Here are all the subclasses


class Html(Element):
    tag = 'html'
    indlvl = 0

    def render(self, out_file, cur_ind=''):
        self.cur_ind = cur_ind + (self.indent*self.indlvl)
        self.front_tag()
        self.content.insert(1, '\n')
        self.content.insert(0, '<!DOCTYPE html>\n')
        self.back_tag()
        self.content.insert(len(self.content), '\n')
        for contentlet in self.content:
            try:
                contentlet.render(out_file)
            except AttributeError:
                if contentlet == '\n':
                    out_file.write(contentlet)
                elif contentlet[0] == '<':
                    out_file.write(self.cur_ind + contentlet)
                else:
                    out_file.write(self.cur_ind + self.indent + contentlet)


class Body(Element):
    tag = 'body'
    indlvl = 1


class P(Element):
    tag = 'p'
    indlvl = 2


class Head(Element):
    tag = 'head'
    indlvl = 1


class OneLineTag(Element):
    indlvl = 2

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.kwargs = kwargs
        if content is not None:
            self.content = [content]

    def render(self, out_file, cur_ind=''):
        self.cur_ind = cur_ind + (self.indent*self.indlvl)
        self.front_tag()
        self.back_tag()
        self.content.insert(len(self.content), '\n')
        for contentlet in self.content:
            try:
                contentlet.render(out_file)
            except AttributeError:
                if contentlet == '\n':
                    out_file.write(contentlet)
                elif (contentlet[0] is '<') and (contentlet[1] is not '/'):
                    out_file.write(self.cur_ind + contentlet)
                else:
                    out_file.write(contentlet)


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.kwargs = kwargs
        if content is not None:
            raise TypeError

    def render(self, out_file, cur_ind=''):
        self.cur_ind = cur_ind + (self.indent*self.indlvl)
        self.self_closing()
        self.content.insert(len(self.content), '\n')
        for contentlet in self.content:
            try:
                contentlet.render(out_file)
            except AttributeError:
                if contentlet == '\n':
                    out_file.write(contentlet)
                elif contentlet[0] == '<':
                    out_file.write(self.cur_ind + contentlet)
                else:
                    out_file.write(self.cur_ind + self.indent + contentlet)

    def self_closing(self):
        k = ''
        for key in self.kwargs:
            k = k + ' ' + key + "='" + str(self.kwargs[key]) + "'"
        self.content.insert(0, '<' + self.tag + k + ' />')


class Hr(SelfClosingTag):
    tag = 'hr'
    indlvl = 2


class Br(SelfClosingTag):
    tag = 'br'
    indlvl = 2


class Meta(SelfClosingTag):
    tag = 'meta charset="UTF-8"'
    indlvl = 2


class A(Element):
    tag = 'a href'
    indlvl = 4

    def __init__(self, link, content=None):
        self.content = []
        self.link = link
        if content is not None:
            self.web = content

    def render(self, out_file, cur_ind=''):
        self.cur_ind = cur_ind + (self.indent*self.indlvl)
        self.content.insert(0, '\n')
        self.content.insert(1, '<' + self.tag + '="' + self.link + '">' + self.web + '</a>')
        self.content.insert(len(self.content), '\n')
        for contentlet in self.content:
            try:
                contentlet.render(out_file)
            except AttributeError:
                if contentlet == '\n':
                    out_file.write(contentlet)
                elif contentlet[0] == '<':
                    out_file.write(self.cur_ind + contentlet)
                else:
                    out_file.write(self.cur_ind + self.indent + contentlet)


class Ul(Element):
    tag = 'ul'
    indlvl = 2


class Li(Element):
    tag = 'li'
    indlvl = 3


class H(OneLineTag):
    tag = 'h'

    def __init__(self, headno, content=None, **kwargs):
        self.content = []
        self.tag = self.tag + str(headno)
        self.kwargs = kwargs
        if content is not None:
            self.content = [content]
