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
    assert file_contents.count("<html>") == 1
    assert file_contents.count("</html>") == 1


# # Uncomment this one after you get the one above to pass
# # Does it pass right away?
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


# # ########
# # # Step 2
# # ########

# # tests for the new tags
def test_html():
    """
    Test the functionality of the Html class

    Expected output is:
    <html>
    this is some text
    and this is some more text
    </html>
    """
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)
    assert file_contents.endswith("</html>")


def test_body():
    """
    Test the functionality of the Body class

    Expected output is:
    <body>
    this is some text
    and this is some more text
    </body>
    """
    e = Body("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():
    """
    Test the functionality of the P class

    Expected output is:
    <p>
    this is some text
    and this is some more text
    </p>
    """
    e = P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    """
    Test the functionality of appending an element to another element.

    Expected output is:
    <html>
    some plain text.
    <p>
    A simple paragraph of text
    </p>
    Some more plain text.
    </html>
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

def test_head():
    """
    Test the functionality of the Head class

    Expected output is:
    <body>
    Here be more tags
    A header with filler
    </body>
    """
    e = Head("Here be more tags")
    e.append("A header with filler")

    file_contents = render_result(e).strip()

    assert "Here be more tags" in file_contents
    assert "A header with filler" in file_contents

    assert file_contents.startswith("<head>")
    assert file_contents.endswith("</head>")


def test_title():
    """
    Test the functionality of the Title class

    Expected output is:
    <title>The title of the page!</title>
    """
    e = Title("The title of the page!")
    with pytest.raises(NotImplementedError):
        e.append("  Possibly a sub-title")

    file_contents = render_result(e).strip()

    assert "The title of the page!" in file_contents
    assert "  Possibly a sub-title" not in file_contents

    assert file_contents.startswith("<title>")
    assert file_contents.endswith("</title>")

    assert file_contents.find("\n") == -1 # the trailing newline will get stripped out so we shouldn't see any additional newlines


def test_head_title():
    """
    Test the functionality of the Head class, with a nested Title class

    Expected output is:
    <head>
    The quick brown fox
    <title>Test Page</title>
    jumped over something or other
    </head>
    """
    head = Head()

    head.append("The quick brown fox")
    head.append(Title("Test Page"))
    head.append("jumped over something or other")

    file_contents = render_result(head)

    assert "<head>" in file_contents
    assert "</head>" in file_contents
    assert "The quick brown fox" in file_contents
    assert "jumped over something or other" in file_contents

    assert "<title>Test Page</title>" in file_contents


########
# Step 4
########

def test_attributes():
    """
    Test the functionality of the classes' ability to add attributes to html tags.

    Expected output is:
    <html>
    <head>
    <title>Test 4 tests</title>
    </head>
    <body>
    <p>
    Paragraph without any extra attributes
    </p>
    <p style="text-align:center;">
    Paragraph 2 should definitely have extra attributes
    </p>
    <p style="text-align:left" class="normalP">
    Paragraph 3 should have multiple extra attributes
    </p>
    </body>
    </html>
    """
    html = Html()

    head = Head()
    head.append(Title("Test 4 tests"))
    html.append(head)

    body = Body()
    body.append(P("Paragraph without any extra attributes"))
    body.append(P("Paragraph 2 should definitely have extra attributes", style="text-align:center;"))
    multiple_attribs = {'style': 'text-align:left', 'class': 'normalP'}
    body.append(P("Paragraph 3 should have multiple extra attributes", **multiple_attribs))
    html.append(body)

    file_contents = render_result(html)

    assert "<html>\n" in file_contents
    assert "</html>\n" in file_contents
    assert "<head>\n" in file_contents
    assert "</head>\n" in file_contents
    assert "<title>Test 4 tests</title>\n" in file_contents
    assert "<body>\n" in file_contents
    assert "</body>\n" in file_contents
    assert "<p>\n" in file_contents
    assert "<p style=\"text-align:center;\">" in file_contents
    assert "<p style=\"text-align:left\" class=\"normalP\">" in file_contents
    assert file_contents.count("</p>\n") == 3


########
# Step 5
########

def test_hr():
    """
    Test the functionality of the Hr class

    Expected output is:
    <hr width="400" />
    """
    e = Hr(width=400)
    with pytest.raises(NotImplementedError):
        e.append("this should fail")

    file_contents = render_result(e).strip()
    print(file_contents)

    assert("width=\"400\"") in file_contents
    assert("this should fail") not in file_contents

    assert file_contents.startswith("<hr")
    assert not file_contents.startswith("<hr>")
    assert file_contents.endswith("/>")
    assert not file_contents.endswith("</hr>")


def test_br():
    """
    Test the functionality of the Br class

    Expected output is:
    <br />
    """
    e = Br()
    with pytest.raises(NotImplementedError):
        e.append("this should fail")

    file_contents = render_result(e).strip()
    print(file_contents)

    assert("this should fail") not in file_contents

    assert file_contents == "<br />"


########
# Step 6
########

def test_a():
    """
    Test the functionality of the A class

    Expected output is:
    <a href="http://www.seattletimes.com">Seattle Times</a>
    """
    e = A("http://www.seattletimes.com", "Seattle Times")
    with pytest.raises(NotImplementedError):
        e.append("this should fail")

    file_contents = render_result(e).strip()
    print(file_contents)

    assert "this should fail" not in file_contents

    assert file_contents == "<a href=\"http://www.seattletimes.com\">Seattle Times</a>"


########
# Step 7
########

def test_ul_li():
    """
    Test the functionality of the Ul and Li classes

    Expected output is:
    <p>
    Paragraph
    <ul id="somelist" style="text-decoration:bold;">
    <li>
    Bullet one
    </li>
    <li style="text-color:red;">
    Bullet two
    </li>
    </ul>
    </p>
    """
    p = P("Paragraph")

    ul = Ul(id="somelist", style="text-decoration:bold;")
    ul.append(Li("Bullet one"))
    ul.append(Li("Bullet two", style="text-color:red;"))

    p.append(ul)

    file_contents = render_result(p).strip()
    print(file_contents)

    assert "<p>" in file_contents
    assert "Paragraph" in file_contents
    assert "<ul id=\"somelist\" style=\"text-decoration:bold;\">" in file_contents
    assert "<li>" in file_contents
    assert "Bullet one" in file_contents
    assert "<li style=\"text-color:red;\">" in file_contents
    assert "Bullet two" in file_contents
    assert file_contents.count("</li>") == 2
    assert "</ul>" in file_contents
    assert "</p>" in file_contents


def test_heading():
    """
    Test the functionality of the H class

    Expected output is:
    <p>
    Paragraph
    <h1>The main title</h1>
    <h2 style="text-decoration:none;">The subtitle</h2>
    </p>
    """
    p = P("Paragraph")

    h1 = H(1, "The main title")
    p.append(h1)

    h2 = H(2, "The subtitle", style="text-decoration:none;")
    p.append(h2)

    file_contents = render_result(p).strip()
    print(file_contents)

    assert "<p>" in file_contents
    assert "Paragraph" in file_contents
    assert "<h1>The main title</h1>" in file_contents
    assert "<h2 style=\"text-decoration:none;\">The subtitle</h2>" in file_contents
    assert "</p> in file_contents"


########
# Step 8
########

def test_doctype():
    """
    Test the addition of the doctype to the Html class

    Expected output is:
    <html>
    <!DOCTYPE html>
    </html>
    """
    e = Html()

    file_contents = render_result(e).strip()
    print(file_contents)

    assert "<html>" in file_contents
    assert file_contents.startswith("<!DOCTYPE html>")
    assert file_contents.endswith("</html>")


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
    assert lines[0].startswith("   <")
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


########################################################################
# Add'l tests (for tags added out of band of the assignment walkthrough)
########################################################################

def test_img():
    """
    Test the functionality of the Img class

    Expected output is (although attributes can be in an arbitrary order):
    <img src="../imgs/test.jpg" alt="Alt text" />
    """
    e = Img("../imgs/test.jpg", alt="Alt text")

    file_contents = render_result(e).strip()

    assert "<img " in file_contents
    assert "src=\"../imgs/test.jpg\"" in file_contents
    assert "alt=\"Alt text\"" in file_contents
    assert file_contents.endswith(" />")
    assert "</img>" not in file_contents

def test_a_with_attribs():
    """
    Test the expanded functionality of the A class

    Expected output is (although attributes can be in an arbitrary order):
    <a href="http://www.seattletimes.com" style="text-decoration:bold;">The Seattle Times</a>
    """
    e = A("http://www.seattletimes.com", "The Seattle Times", style="text-decoration:bold;")

    file_contents = render_result(e).strip()

    assert "<a " in file_contents
    assert "href=\"http://www.seattletimes.com\"" in file_contents
    assert "style=\"text-decoration:bold;\"" in file_contents
    assert file_contents.endswith(">The Seattle Times</a>")
