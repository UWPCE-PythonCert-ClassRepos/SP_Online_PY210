"""
test code for html_render.py
"""

import io
import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from html_render import *


# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.
def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = io.StringIO()
    # this so the tests will work before we tackle indentation
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
    So it is also testing that the append method works correctly.

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
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

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



# ########
# # Step 2
# ########

def test_html():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)
    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<!DOCTYPE html>")
    assert "<html>" in file_contents
    assert file_contents.endswith("</html>")


def test_body():
    e = Body("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():
    e = P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<p>" in file_contents
    assert "</p>" in file_contents
    #added: test that the tags are nested in the right order
    assert file_contents.index("<html>") < file_contents.index("<p>") \
     < file_contents.index("</p>") < file_contents.index("</html>")




########
# Step 3
########

# Add your tests here!

def test_head_element():
    page = Html()
    page.append("some plain text.")
    page.append(Head("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<head>" in file_contents
    assert "</head>" in file_contents
    assert file_contents.index("<head>") < file_contents.index("</head>")

def test_title_element():
    page = Html()
    page.append(Title("PythonClass - Session 6 example"))

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    assert "<title>PythonClass - Session 6 example</title>" in file_contents

#Step 4

def test_attributes():
    page = Html()
    page.append(P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough  to show that we can do some text",
              style="text-align: center; font-style: oblique;"))

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    assert '<p style="text-align: center; font-style: oblique;">' in file_contents
    assert "Here is a paragraph of text -- there could be more of them, " in file_contents
    assert "</p>" in file_contents
    assert file_contents.index("<p style") < file_contents.index("Here is a paragraph") \
           < file_contents.index("</p>")

#Step 5

def test_selfclosingtag():
    page = Html()
    page.append("some plain text.")
    page.append(Hr())
    page.append(Br())

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    assert "<hr />" in file_contents
    assert "<br />" in file_contents
    #Test that a TypeError is raised when self closing tag is given content
    with pytest.raises(TypeError):
        badhr = Hr(content="some content")

#Step 6

def test_link():
    page = Html()
    page.append("some plain text.")
    page.append(A("http://www.google.com", "link to Google"))

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    assert '<a href="http://www.google.com">link to Google</a>' in file_contents

#Step 7

def test_lists():
    page = Html()

    mylist = Ul()
    mylist.append(Li("Item one"))
    mylist.append(Li("Item two"))
    page.append(mylist)

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    assert "<ul>" in file_contents
    assert "</ul>" in file_contents
    assert "<li>" in file_contents
    assert "</li>" in file_contents
    assert "Item one" in file_contents
    assert "Item two" in file_contents
    assert file_contents.index("<ul>") < file_contents.index("<li>") \
           < file_contents.index("</li>") < file_contents.index("</ul>")

def test_headers():
    page = Html()
    page.append(H(1, "header one"))
    page.append(H(2, "header two"))

    file_contents = render_result(page)
    print(file_contents)

    assert "<h1>header one</h1>" in file_contents
    assert "<h2>header two</h2>" in file_contents

#Step 8

def test_meta():
    page = Html()
    head = Head()
    head.append(Meta(charset="UTF-8"))
    page.append(head)

    file_contents = render_result(page)
    print(file_contents)

    assert '<meta charset="UTF-8" />' in file_contents




#####################
# indentation testing
#  Uncomment for Step 9 -- adding indentation
#####################


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    html = Html("some content")
    file_contents = render_result(html, ind="   ").rstrip()  #remove the end newline

    print(file_contents)
    lines = file_contents.split("\n")
    #below changed from lines[0] to lines[1] because the first line has the doctype tag
    assert lines[1].startswith("   <")
    print(repr(lines[-1]))
    assert lines[-1].startswith("   <")


def test_indent_contents():
    """
    The contents in an element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = Element("some content")
    file_contents = render_result(html, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(Element.indent)


def test_multiple_indent():
    """
    make sure multiple levels get indented fully
    """
    body = Body()
    body.append(P("some text"))
    html = Html(body)

    file_contents = render_result(html)

    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
        assert lines[i + 1].startswith(i * Element.indent + "<")

    assert lines[4].startswith(3 * Element.indent + "some")


def test_element_indent1():
    """
    Tests whether the Element indents at least simple content

    we are expecting to to look like this:

    <html>
        this is some text
    </html>

    More complex indentation should be tested later.
    """
    e = Element("this is some text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # break into lines to check indentation
    lines = file_contents.split('\n')
    # making sure the opening and closing tags are right.
    assert lines[0] == "<html>"
    # this line should be indented by the amount specified
    # by the class attribute: "indent"
    assert lines[1].startswith(Element.indent + "thi")
    assert lines[2] == "</html>"
    assert file_contents.endswith("</html>")
