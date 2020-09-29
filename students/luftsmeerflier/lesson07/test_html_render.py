"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io
import pytest

# import * is often bad form, but makes it easier to test everything in a module
from html_render import *

# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.
def render_result(element, ind=""):
	"""
	calls the element's render method, and returns what got renders as a string
	"""
	# the StringIO object is a "file-like" object -- something that
	# provides the mehtods of a file, but keeps everything in memory
	# so it can be used to test code that writes to a file, without
	# having to actually write to disk.
	outfile = io.StringIO()
	# this is so the tests wil work before we tackle indentation
	if ind:
		element.render(outfile, ind)
	else:
		element.render(outfile)
	return outfile.getvalue()

########
# Step 1
########

def test_init():
	"""
	This only tests that it can be initialized with and without
	some content -- but it's a start
	"""
	e = Element()

	e = Element("this is some text")




def test_append():
	"""
	This tests that you can append text

	It doesn't test if it works --
	that will be covered by the render test later
	"""
	e = Element("this is some text")
	e.append("some more text")


def test_render_element():
	"""
	Tests whether the Element can render two pieces of text
	so it is also testing that the append method workds correctly.

	It is not testing whether indentation or line feeds are correct. 
	"""
	e = Element("this is some text")
	e.append("and this is some more text")

	# This uses the render_results utility above
	file_contents = render_result(e).strip()

	# making sure the content got in there. 
	assert("this is some text") in file_contents
	assert("and this is some more text") in file_contents

	# make sure it's in the right order
	assert file_contents.index("this is") < file_contents.index("and this")

	# making sure the opening and closing tags are right.
	assert file_contents.startswith("<html>")
	assert file_contents.endswith("</html>")

 # Uncomment this one after you get the one above to pass
 # Does it pass right away?
def test_render_element2():
	"""
	Tests whether the element can render two pieces of text
	So it is also testing that the append method works correctly/

	It is not testing whether indentation or line feeds are correct.
	"""
	e = Element()
	e.append("this is some text")
	e.append("and this is some more text")

	# This uses the render_results utility above
	file_contents = render_result(e).strip()

	# making sure the content got in there.
	assert("this is some text") in file_contents
	assert("and this is some more text") in file_contents

	# make sure it's in the right order
	assert file_contents.index("this is") < file_contents.index("and this")

	# making sure the opening and closing tags are right.
	assert file_contents.startswith("<html>")
	assert file_contents.endswith("</html>")



# # ########
# # # Step 2
# # ########

# # tests for the new tags
def test_html():
	e = Html("this is some text")
	e.append("and this is some more text")

	file_contents = render_result(e).strip()

	assert("this is some text") in file_contents
	print(file_contents)
	assert("and this is some more text") in file_contents
	assert file_contents.endswith("</html>")


def test_body():
	e = Body("this is some text")
	e.append("and this is some more text")

	file_contents = render_result(e).strip()

	assert("this is some text") in file_contents
	assert("and this is some more text") in file_contents

	assert file_contents.startswith("<body>")
	assert file_contents.endswith("</body>")


# def test_p():
# 	e = P("this is some text")
# 	e.append("and this is some more text")

# 	file_contents = render_results(e).strip()

# 	assert("this is some text") in file_contents
# 	assert("and this is some more text") in file_contents

# 	assert file_contents.startswith("<p>")
# 	assert file_contents.endswith("</p>")


# def test_sub_element():
#	"""
#	tests that you can add another element and still render properly
#	"""
#	page = Html()
# 	page.append("some plain text.")
# 	page.append(P("A simple paragraph of text"))
#	page.append("Some more plain text.")

#	file_contents = render_result(page)
#	print(file_contents) # so we can see it if the test fails

#	# note: The previous tests should make sure that the tags are getting
#	#	properly rendered, so we don't need to test that here.
#	assert "some plain text" in file_contents
#	assert "A simple paragraph of text" in file_contents
#	assert ""
















