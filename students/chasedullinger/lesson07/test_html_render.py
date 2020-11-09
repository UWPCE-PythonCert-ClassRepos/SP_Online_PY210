"""
test code for html_render.py

This is just a start -- you will need more tests!
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


# def test_render_element():
#     """
#     Tests whether the Element can render two pieces of text
#     So it is also testing that the append method works correctly.
#
#     It is not testing whether indentation or line feeds are correct.
#     """
#     e = Element("this is some text")
#     e.append("and this is some more text")
#
#     # This uses the render_results utility above
#     file_contents = render_result(e).strip()
#
#     # making sure the content got in there.
#     assert("this is some text") in file_contents
#     assert("and this is some more text") in file_contents
#
#     # make sure it's in the right order
#     assert file_contents.index("this is") < file_contents.index("and this")
#
#     # making sure the opening and closing tags are right.
#     assert file_contents.startswith("<html>")
#     assert file_contents.endswith("</html>")

# # Uncomment this one after you get the one above to pass
# # Does it pass right away?
# def test_render_element2():
#     """
#     Tests whether the Element can render two pieces of text
#     So it is also testing that the append method works correctly.
#
#     It is not testing whether indentation or line feeds are correct.
#     """
#     e = Html()
#     e.append("this is some text")
#     e.append("and this is some more text")
#
#     # This uses the render_results utility above
#     file_contents = render_result(e).strip()
#
#     # making sure the content got in there.
#     assert("this is some text") in file_contents
#     assert("and this is some more text") in file_contents
#
#     # make sure it's in the right order
#     assert file_contents.index("this is") < file_contents.index("and this")
#
#     # making sure the opening and closing tags are right.
#     assert file_contents.startswith("<html>")
#     assert file_contents.endswith("</html>")



# # ########
# # # Step 2
# # ########

# tests for the new tags
def test_html():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)
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




########
# Step 3
########

# Add your tests here!
def test_head():
    e = Head("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)
    assert file_contents.endswith("</head>")


def test_title():
    e = Title("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e)
    check_string = "<title>this is some textand this is some more text</title>"

    assert file_contents == check_string


def test_sub_element2():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    header = Head("A header")
    title = Title("A title")
    header.append(title)
    page.append(header)
    body = Body("some body text")
    p1 = P("A simple paragraph of text")
    p2 = P("Some more plain text.")
    body.append(p1)
    body.append(p2)
    page.append(body)


    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "A header" in file_contents
    assert "A title" in file_contents
    assert "some body text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<p>" in file_contents
    assert "</p>" in file_contents


########
# Step 4
########
def test_tag_attributes():
    """
    tests that you can add attributes to a tag
    """
    page = Html()
    header = Head("A header")
    title = Title("A title")
    header.append(title)
    page.append(header)
    body = Body("some body text")
    p1 = P("A simple paragraph of text", style="text-align: center; font-style: oblique;")
    p2 = P("Some more plain text.")
    body.append(p1)
    body.append(p2)
    page.append(body)


    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "A header" in file_contents
    assert "A title" in file_contents
    assert "some body text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    # but make sure the embedded element's tags get rendered!
    assert 'style="text-align: center; font-style: oblique;"' in file_contents
    assert "<p>" in file_contents
    assert "</p>" in file_contents


########
# Step 5
########
def test_hr():
    e = Hr()

    file_contents = render_result(e).strip()

    assert file_contents.startswith("<hr />")

    with pytest.raises(TypeError):
        e = Hr("some content")


def test_br():
    e = Br()

    file_contents = render_result(e).strip()

    assert file_contents.startswith("<br />")

    with pytest.raises(TypeError):
        e = Br("some content")

########
# Step 6
########
def test_a():
    e = A("http://google.com", "link to google")

    file_contents = render_result(e).strip()

    test_string = '<a href="http://google.com">link to google</a>'
    assert file_contents == test_string

########
# Step 7
########
def test_li():
    e = Li("The first item in a list")
    file_contents = render_result(e).strip()

    assert file_contents.startswith("<li>")
    assert "The first item in a list" in file_contents
    assert file_contents.endswith("</li>")


def test_Ul():
    e = Ul("The first item in a list")
    file_contents = render_result(e).strip()

    assert file_contents.startswith("<ul>")
    assert "The first item in a list" in file_contents
    assert file_contents.endswith("</ul>")


def test_h():
    e = H(2, "some content")

    file_contents = render_result(e).strip()

    assert file_contents.startswith("<h2>")
    assert "some content" in file_contents
    assert file_contents.endswith("</h2>")

    with pytest.raises(TypeError):
        e = H("some non-int", "some content")


# check that DOCTYPE is properly written
def test_html2():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)
    assert file_contents.endswith("</html>")
    assert file_contents.startswith("<!DOCTYPE html>")


def test_meta():
    e = Meta(charset="UTF-8")
    file_contents = render_result(e).strip()

    test_string = '<meta charset="UTF-8" />'
    assert test_string in file_contents
# #####################
# # indentation testing
# #  Uncomment for Step 9 -- adding indentation
# #####################



def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    html = Html("some content")
    file_contents = render_result(html, ind="   ").rstrip()  #remove the end newline

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[0] == "<!DOCTYPE html>"
    assert lines[1].startswith("   <")
    print(repr(lines[-1]))
    assert lines[-1].startswith("   <")


def test_indent_contents():
    """
    The contents in a element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = Element("some content")
    file_contents = render_result(html, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[0].startswith(Element.indent)


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
    <\html>

    More complex indentation should be tested later.
    """
    e = Html("this is some text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # break into lines to check indentation
    lines = file_contents.split('\n')
    print(lines)
    # making sure the opening and closing tags are right.
    assert lines[1] == "<html>"
    # this line should be indented by the amount specified
    # by the class attribute: "indent"
    assert lines[2].startswith(Element.indent + "thi")
    assert lines[3] == "</html>"
    assert file_contents.endswith("</html>")
