#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag_name = 'html'

    def __init__(self, content=None):
        self.content = [content] if content else []

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write('<{}>\n'.format(self.tag_name))
        for line in self.content:
            out_file.write(line + '\n')
        out_file.write('</{}>\n'.format(self.tag_name))
