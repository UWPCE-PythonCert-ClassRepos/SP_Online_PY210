#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag_name = "html"

    open_tag = {"start": "<", "end": ">"}
    close_tag = {"start": "</", "end": ">"}

    def __init__(self, content=None):
        self.content = content

    def append(self, new_content):
        self.content = " ".join([self.content, (new_content)])

    def render(self, out_file):
        out_file.write("".join([self.open_tag["start"], self.tag_name,
                                self.open_tag["end"], self.content,
                                self.close_tag["start"], self.tag_name,
                                self.close_tag["end"]]))
