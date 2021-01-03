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


########
# Step 2
########


# # tests for the new tags
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
    e = Html()
    e.append("some plain text.")
    e.append(P("A simple paragraph of text"))
    e.append("Some more plain text.")

    file_contents = render_result(e)
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
    e = Head("this is some text")
    e.append("and this is some more text")
    file_contents = render_result(e).strip()
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    assert file_contents.startswith("<head>")
    assert file_contents.endswith("</head>")


def test_title():
    e = Title("this is a title")
    file_contents = render_result(e).strip()
    assert("this is a title") in file_contents
    print(file_contents)
    assert file_contents.startswith("<title>")
    assert file_contents.endswith("</title>")
    assert "\n" not in file_contents


def test_one_line_tag_append():
    e = OneLineTag("the initial content")
    with pytest.raises(NotImplementedError):
        e.append("some more content")


########
# Step 4
########


def test_attributes():
    e = P("A paragraph of text", style="text-align: center", id="intro")
    file_contents = render_result(e).strip()
    print(file_contents)
    assert "A paragraph of text" in file_contents
    assert file_contents.endswith("</p>")
    assert file_contents.startswith("<p")
    assert 'style="text-align: center"' in file_contents
    assert 'id="intro"' in file_contents
    assert file_contents[:file_contents.index(">")].count(" ") == 3


########
# Step 5
########


def test_hr():
    e = Hr()
    file_contents = render_result(e)
    print(file_contents)
    assert file_contents == "<hr />\n"


def test_hr_attr():
    e = Hr(width=400)
    file_contents = render_result(e)
    print(file_contents)
    assert file_contents == '<hr width="400" />\n'


def test_br():
    e = Br()
    file_contents = render_result(e)
    print(file_contents)
    assert file_contents == "<br />\n"


def test_content_in_br():
    with pytest.raises(TypeError):
        e = Br("some content")


def test_append_content_in_br():
    with pytest.raises(TypeError):
        e = Br()
        e.append("some content")


########
# Step 6
########


def test_anchor():
        a = A("http://google.com", "link to google")
        file_contents = render_result(a)
        print(file_contents)
        assert file_contents == '<a href="http://google.com">link to google</a>'
        assert file_contents.startswith("<a ")
        assert file_contents.endswith("</a>")


########
# Step 7
########


def test_ul():
    e = Ul(id="TheList", style="line-height:200%")
    file_contents = render_result(e).strip()
    print(file_contents)
    assert file_contents.startswith("<ul ")
    assert file_contents.endswith("</ul>")
    assert 'id="TheList"' in file_contents
    assert 'style="line-height:200%"' in file_contents
    assert file_contents[:file_contents.index(">")].count(' ') == 2


def test_li():
    e = Li("Test item in a list", style="color: red")
    file_contents = render_result(e).strip()
    print(file_contents)
    assert file_contents.startswith("<li ")
    assert file_contents.endswith("</li>")
    assert 'style="color: red"' in file_contents
    assert "Test item in a list" in file_contents


def test_headers():
    e = H(2, "Test Header")
    file_contents = render_result(e).strip()
    print(file_contents)
    assert file_contents == '<h2>Test Header</h2>'


########
# Step 7
########


def test_doctype():
    e = Html("this is some text")
    file_contents = render_result(e)
    assert file_contents.startswith("<!DOCTYPE html>")
    print(file_contents)
    assert file_contents.endswith("</html>")

def test_meta():
    e = Meta(charset="UTF-8")
    file_contents = render_result(e).strip()
    assert file_contents == '<meta charset="UTF-8" />'
    print(file_contents)


#####################
# indentation testing
#  Uncomment for Step 9 -- adding indentation
#####################


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    e = Html("some content")
    file_contents = render_result(e, ind="   ").rstrip()  #remove the end newline

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
    e = Element("some content")
    file_contents = render_result(e, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(Element.indent)


def test_multiple_indent():
    """
    make sure multiple levels get indented fully
    """
    e = Body()
    e.append(P("some text"))
    html = Html(e)

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

def test_onelinetag_indent():
    e = Html()
    head = Head()
    head.append(Title("Test OneLineTag"))
    e.append(head)
    file_contents = render_result(e)
    print(file_contents)
    lines = file_contents.split('\n')
    assert lines[3].startswith("        <title")

def test_selfclosingtag_indent():
    e = Html()
    head = Head()
    head.append(Title("Test Title"))
    e.append(head)
    body = Body()
    body.append(H(2, "Test SelfClosingTag") )
    e.append(body)
    file_contents = render_result(e)
    print(file_contents)
    lines = file_contents.split('\n')
    assert lines[6].startswith("        <h2")
