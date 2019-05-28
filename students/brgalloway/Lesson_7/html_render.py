#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None):
        self.content = content
        self.content = f"<{self.tag}>{self.content}</{self.tag}>"
        if content == None:
            self.content = f"<{self.tag}></{self.tag}>"
    def append(self, new_content):
        self.new_content = new_content
        self.content = self.content.replace("</html>", "")
        self.content = f"{self.content}{new_content}</{self.tag}>"
    def render(self, out_file):
        out_file.write(self.content)



class Html(object):

    def __init__(self, content=None):
        pass

    def append(self, new_content):
        pass


class Body(object):

    def __init__(self, content=None):
        pass

    def append(self, new_content):
        pass

  
class Head(object):

    def __init__(self, content=None):
        pass

    def append(self, new_content):
        pass
