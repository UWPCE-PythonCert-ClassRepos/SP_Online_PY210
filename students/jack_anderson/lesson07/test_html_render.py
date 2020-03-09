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
    print(file_contents)

    # making sure the content got in there.
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.count("<html>") == 1
    assert file_contents.count("</html>") == 1
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
    assert file_contents.count("<html>") == 1
    assert file_contents.count("</html>") == 1
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")



# ########
# # Step 2
# ########

# tests for the new tags
def test_html():
    e = Html("this is some text for html test")
    e.append("and this is some more text for html testing")

    file_contents = render_result(e).strip()
    print(file_contents)

    assert("this is some text for html test") in file_contents
    assert("and this is some more text for html testing") in file_contents
    assert file_contents.index("<html>") < file_contents.index("</html>")
    assert file_contents.endswith("</html>")

    # assert False
    # assert False



def test_body():
    e = Body("this is some body text")
    e.append("and this is some more body text")

    file_contents = render_result(e).strip()
    print(file_contents)

    assert("this is some body text") in file_contents
    assert("and this is some more body text") in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")

    # assert False
    # assert False


def test_p():
    e = P("this is some text for p tag")
    e.append("and this is some more text for P tag")

    file_contents = render_result(e).strip()
    print(file_contents)

    assert("this is some text for p tag") in file_contents
    assert("and this is some more text for P tag") in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")

    # assert False
    # assert False



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

    # assert False
    # assert False




########
# Step 3
########

def test_head():
    e = Head("This is a head test")
    e.append("and this is some more text for head testing")

    file_contents = render_result(e).strip()
    print(file_contents)

    assert("This is a head test") in file_contents
    assert("and this is some more text for head testing") in file_contents

    assert file_contents.endswith("</head>")
    assert file_contents.startswith("<head>")

    # assert False
    # assert False



def test_title():
    e = Title("This is a Title Test")

    file_contents = render_result(e).strip()
    print(file_contents)

    assert("This is a Title Test") in file_contents
    assert("\n") not in file_contents

    assert file_contents.endswith("</title>")
    assert file_contents.startswith("<title>")

    # assert False
    # assert False


def test_hr_again():
    """a simple horizontal rule with no attributes"""
    hr = Hr()
    file_contents = render_result(hr)
    print(file_contents)
    assert file_contents == '<hr />\n'

    # assert False
    # assert False


def test_hr_attr_again():
    """a horizontal rule with an attribute"""
    hr = Hr(width=400)
    file_contents = render_result(hr)
    print(file_contents)
    assert file_contents == '<hr width="400" />\n'
    #
    # assert False
    # assert False



def test_oneline_tag_append():
    e = Title("This is a one line title")

    with pytest.raises(NotImplementedError):
        e.append("This should fail")
    #
    # try:
    #     e.append("This should fail")
    # except NotImplementedError:
    #     pass

########
# Step 4
########

def test_atttributes_element():
    e = P("some text content", id="TheList", style="line-height:200%")
    file_contents = render_result(e).strip()
    print(file_contents)

    assert "some text content" in file_contents

    assert file_contents.endswith("</p>")

    assert file_contents.startswith("<p ")

    assert 'id="TheList"' in file_contents
    assert 'style="line-height:200%"' in file_contents

    # assert False
    # assert False


def test_atttributes_OneLineTag():
    e = Title("a title with attributes", invalid_title_tag="Titles-dont-have-attribs", style="no_style_here")
    file_contents = render_result(e).strip()
    print(file_contents)

    assert 'invalid_title_tag="Titles-dont-have-attribs"' in file_contents
    assert 'style="no_style_here"' in file_contents
    assert "a title with attributes" in file_contents

    assert file_contents.endswith("</title>")
    assert file_contents.startswith("<title ")

    # assert False
    # assert False


########
# Step 5
########

def test_self_closing_tag_hr():
    e = Hr(width=400)

    file_contents = render_result(e).strip()
    print(file_contents)

    assert '<hr width="400" />' in file_contents
    assert ("\n") not in file_contents

    assert file_contents.endswith(">")
    assert file_contents.startswith("<hr ")

    # assert False
    # assert False


def test_self_closing_tag_br():
    e = Br(height=400)

    file_contents = render_result(e).strip()
    print(file_contents)

    assert '<br height="400" />' in file_contents
    assert ("\n") not in file_contents

    assert file_contents.endswith(">")
    assert file_contents.startswith("<br ")

    # assert False
    # assert False


def test_br():
    br = Br()
    file_contents = render_result(br)
    print(file_contents)
    assert file_contents == "<br />\n"

    # assert False
    # assert False


def test_append_content_in_br():
    with pytest.raises(TypeError):
        br = Br()
        br.append("some content")

        # assert False
        # assert False

########
# Step 6
########


def test_anchor():
    e = A("http://google.com", "link")

    file_contents = render_result(e).strip()
    print(file_contents)

    assert ('<a href="http://google.com">link</a>') in file_contents

    assert file_contents.endswith("</a>")
    assert file_contents.startswith("<a href=")

    # assert False
    # assert False


########
# Step 7
########

def test_ul_and_li():
    e = Ul(id="List of Animals", style="line-height:150%")
    e.append(Li("Zebra"))
    e.append(Li("Cougar"))
    e.append(Li("Mole Rat"))

    file_contents = render_result(e)
    print(file_contents)
    assert file_contents.endswith("</ul>\n")
    assert file_contents.startswith('<ul id="List of Animals"')
    assert 'Zebra' in file_contents
    assert file_contents.index("Zebra") < file_contents.index("Cougar") < file_contents.index("Mole Rat")
    assert file_contents.count('<li>') == 3
    assert file_contents.count('</li>') == 3

    # assert False
    # assert False


def test_valid_h():
    e = H(2, "The text of the header")
    file_contents = render_result(e)
    print(file_contents)
    assert file_contents == '<h2>The text of the header</h2>\n'

    # assert False
    # assert False


def test_invalid_h():
    with pytest.raises(ValueError):
        e = H('abc', "The text of the header")
        file_contents = render_result(e)
        print(file_contents)

    # assert False
    # assert False


########
# Step 8
########


def test_doctype_tag():
    e = Html("this is some text for html test")
    file_contents = render_result(e).strip()
    print(file_contents)
    doc_tag = "<!DOCTYPE html>"
    assert doc_tag in file_contents

    assert file_contents.startswith(doc_tag)
    assert file_contents.index(doc_tag) < file_contents.index("<html>") < file_contents.index("</html>")

    # assert False
    # assert False


def test_meta():
    e = Meta(charset="UTF-8")
    file_contents = render_result(e)
    print(file_contents)
    tag = '<meta charset="UTF-8" />'
    assert tag in file_contents

    # assert False
    # assert False




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
    assert lines[1].startswith("   <")
    print(repr(lines[-1]))
    assert lines[-1].startswith("   <")

    # assert False
    # assert False



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

    # assert False
    # assert False


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

    # assert False
    # assert False


def test_element_indent1():
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

    # assert False
    # assert False
