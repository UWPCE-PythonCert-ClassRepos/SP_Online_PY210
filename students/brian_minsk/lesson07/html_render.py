#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag_name = "html"

    def __init__(self, content=None):
        if content:
            self.content = [content]
        else:
            self.content = []

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        print(self.content)
        opening_tag = self.create_opening_tag(self.tag_name)
        closing_tag = self.create_closing_tag(self.tag_name)
        body = "\n".join([opening_tag, "\n".join(self.content), closing_tag])
        out_file.write(body)

    def create_opening_tag(self, tag_name):
        return "".join(["<", tag_name, ">"])

    def create_closing_tag(self, tag_name):
        return "".join(["</", tag_name, ">"])
