#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

class Element(object):
    tag = 'html'

    def __init__(self, content=None):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        print("contents is:", self.contents)

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))
