#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    def __init__(self, content=None):
        self.content = '<!DOCTYPE html>\n<html>'
        if content is not None:
            self.content += content

    def append(self, new_content):
        self.content += '\n'+new_content

    def render(self, out_file):
        # out_file.write("just something as a place holder...")
        out_file.write(self.content+'\n</html>')
