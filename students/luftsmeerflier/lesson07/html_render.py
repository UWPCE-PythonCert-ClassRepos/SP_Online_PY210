#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the frmaework for the base class
class Element(object):

	tag = "html"

	def __init__(self, content=None):
		if type(content) is not None:
			self.contents = [content]
		else:
			pass

	def append(self, new_content=None):
		if type(new_content) is str:
			self.contents.append(new_content)
		else:
			pass

	def render(self, out_file):
		out_file.write("<{}>\n".format(self.tag))
		for content in self.contents:
			if type(content) is str:
				out_file.write(content)
				out_file.write("\n")
			else:
				pass
		out_file.write("</{}>\n".format(self.tag))

class Html(Element):
	tag = "html"

class Body(Element):
	tag = "body"
