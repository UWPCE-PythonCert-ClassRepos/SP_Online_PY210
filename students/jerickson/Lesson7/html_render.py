"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    tag = "html"

    def __init__(self, content=None):
        if content:
            self.content = [content]
        else:
            self.content = []

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        output = [f"<{self.tag}>", *self.content, f"</{self.tag}>"]
        print(output)
        out_file.write("\n".join(output))
