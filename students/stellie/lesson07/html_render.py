#!/usr/bin/env python3

# Stella Kim
# Assignment 5: HTML Renderer Exercise

"""
A class-based system for rendering HTML.
"""


# Base class framework
class Element(object):
    tag_name = 'html'

    def __init__(self, content=None):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag_name))
        for content in self.contents:   # loop through list of contents
            out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag_name))
