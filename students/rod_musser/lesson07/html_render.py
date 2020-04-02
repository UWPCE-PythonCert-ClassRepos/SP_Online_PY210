#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag_name = "html"

    def __init__(self, content=None):
        self.content_list = [content]

    def append(self, new_content):
        self.content_list.append(new_content)

    def render(self, out_file):
        out_file.write("<" + Element.tag_name + ">" + "\n")
        for content in self.content_list:
            out_file.write(content + "\n")
        out_file.write("</" + Element.tag_name + ">" + "\n")
