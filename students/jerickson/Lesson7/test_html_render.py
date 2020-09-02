"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io
import pytest  # pylint: disable=unused-import

import html_render as hr

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
        element.render(outfile, len(ind))
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
    elem = hr.Element()  # pylint: disable=unused-variable

    elem = hr.Element("this is some text")


def test_append():
    """
    This tests that you can append text

    It doesn't test if it works --
    that will be covered by the render test later
    """
    elem = hr.Element("this is some text")
    elem.append("some more text")


def test_render_element():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    elem = hr.Element("this is some text")
    elem.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(elem).strip()

    # making sure the content got in there.
    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")


# Uncomment this one after you get the one above to pass
# Does it pass right away? yes
def test_render_element2():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    elem = hr.Element()
    elem.append("this is some text")
    elem.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(elem).strip()

    # making sure the content got in there.
    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")


# ########
# # Step 2
# ########

# tests for the new tags
def test_html():  # pylint: disable=missing-function-docstring
    elem = hr.Html("this is some text")
    elem.append("and this is some more text")

    file_contents = render_result(elem).strip()

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    print(file_contents)
    assert file_contents.endswith("</html>")


def test_body():  # pylint: disable=missing-function-docstring
    elem = hr.Body("this is some text")
    elem.append("and this is some more text")

    file_contents = render_result(elem).strip()

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():  # pylint: disable=missing-function-docstring
    elem = hr.P("this is some text")
    elem.append("and this is some more text")

    file_contents = render_result(elem).strip()

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    """
    tests that you can add another element and still render properly
    """
    page = hr.Html()
    page.append("some plain text.")
    page.append(hr.P("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)
    print(file_contents)  # so we can see it if the test fails

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


def test_head():  # pylint: disable=missing-function-docstring
    elem = hr.Head("this is some text")
    elem.append("and this is some more text")

    file_contents = render_result(elem).strip()

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    assert file_contents.startswith("<head>")
    assert file_contents.endswith("</head>")


def test_onelinetag():  # pylint: disable=missing-function-docstring
    elem = hr.OneLineTag("this is some text")
    elem.append("and this is some more text")

    file_contents_raw = render_result(elem)
    file_contents = file_contents_raw.strip()
    file_contents_lines = file_contents_raw.split("\n")

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")

    # 1 line with content, 1 line empty (end of line, newline), 2 lines total
    assert len(file_contents_lines) == 2
    assert file_contents_lines[1] == ""


def test_title():  # pylint: disable=missing-function-docstring
    elem = hr.Title("this is some text")
    elem.append("and this is some more text")

    file_contents_raw = render_result(elem)
    file_contents = file_contents_raw.strip()
    file_contents_lines = file_contents_raw.split("\n")

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    assert file_contents.startswith("<title>")
    assert file_contents.endswith("</title>")

    # 1 line with content, 1 line empty (end of line, newline), 2 lines total
    assert len(file_contents_lines) == 2
    assert file_contents_lines[1] == ""


########
# Step 4
########


def get_opening_line(element):
    """Gets only the opening tag of a potentially nested element"""
    return render_result(element).split("\n")[0]


def test_extended_init():
    """Test the extended kwargs functionality of Element"""
    elem = hr.Element("this is some text", id="spam", style="eggs")

    assert get_opening_line(elem) == '<html id="spam" style="eggs">'


def test_class_attributes():
    """Test the ability to assign the html-class using various methods"""

    string_class_dict = {"class": "spam"}
    string_class = hr.Element("this is some text", **string_class_dict)
    assert get_opening_line(string_class) == '<html class="spam">'

    clas = hr.Element("this is some text", clas="spam")  # cspell:disable-line
    assert get_opening_line(clas) == '<html class="spam">'  # cspell:disable-line

    _clas = hr.Element("this is some text", _clas="spam")  # cspell:disable-line
    assert get_opening_line(_clas) == '<html class="spam">'  # cspell:disable-line

    _class = hr.Element("this is some text", _class="spam")  # cspell:disable-line
    assert get_opening_line(_class) == '<html class="spam">'  # cspell:disable-line


def test_set_attribute():
    """Test that attributes can be assigned before and after init"""
    elem = hr.Element("this is some text", id="spam", style="eggs")
    elem.set_attributes(holy="grail", answer=42)

    assert (
        get_opening_line(elem)
        == '<html id="spam" style="eggs" holy="grail" answer="42">'
    )


def test_set_attribute_override():
    """Test that attributes can be overridden after init, including alternate class spellings"""
    elem = hr.Element(
        "this is some text",
        style="cheese",
        answer=1,
        clas="spam",  # cspell:disable-line
    )
    elem.set_attributes(holy="grail", answer=42, _clas="eggs")  # cspell:disable-line

    opening_tag = get_opening_line(elem)
    assert 'style="cheese"' in opening_tag
    assert 'answer="42"' in opening_tag
    assert 'class="eggs"' in opening_tag
    assert 'holy="grail"' in opening_tag


########
# Step 5
########


def test_self_closing():
    """Test the extended kwargs functionality of Element"""
    elem = hr.SelfClosingTag(style="eggs")

    assert get_opening_line(elem) == '<html style="eggs" />'


def test_self_closing_content_errors():
    """Test that self-closing-tags cannot accept content"""
    with pytest.raises(TypeError):
        elem = hr.SelfClosingTag(  # pylint: disable=too-many-function-args
            "spam", style="eggs"
        )
    with pytest.raises(TypeError):
        elem = hr.SelfClosingTag(content="spam", style="eggs")
    with pytest.raises(TypeError):
        elem = hr.SelfClosingTag(style="eggs")
        elem.append("spam")


def test_hr():
    """Test hr element"""
    elem = hr.Hr(style="eggs")
    elem.set_attributes(id="spam")

    assert get_opening_line(elem) == '<hr style="eggs" id="spam" />'


def test_br():
    """Test br element"""
    elem = hr.Br(style="eggs")
    elem.set_attributes(id="spam")

    assert get_opening_line(elem) == '<br style="eggs" id="spam" />'


########
# Step 6
########


def test_anchor():
    """Test a element"""
    elem = hr.A(link="google.com", content="some spam", style="eggs")

    assert get_opening_line(elem) == '<a href="google.com" style="eggs">some spam</a>'


########
# Step 7
########


def test_li():
    """Test li element"""
    elem = hr.Li("some spam", style="eggs")

    assert get_opening_line(elem) == '<li style="eggs">'


def test_ul():
    """Test ul element"""
    elem = hr.Ul("some spam", style="eggs")

    assert get_opening_line(elem) == '<ul style="eggs">'


def test_h():
    """Test h element"""
    for h_number in [1, 2, 3]:
        elem = hr.H(h_number, "some spam", style="eggs")

        assert (
            get_opening_line(elem)
            == f'<h{h_number:d} style="eggs">some spam</h{h_number:d}>'
        )


########
# Step 8
# ########


def test_html_doctype():
    """Test html element adds 'doctype' at the top"""
    elem = hr.Html("some spam", style="eggs")

    assert get_opening_line(elem) == "<!DOCTYPE html>"


def test_meta():
    """Test meta element"""
    elem = hr.Meta(style="eggs")
    elem.set_attributes(id="spam")

    assert get_opening_line(elem) == '<meta style="eggs" id="spam" />'


#####################
# indentation testing
#  Uncomment for Step 9 -- adding indentation
#####################


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    html = hr.Html("some content")
    file_contents = render_result(html, ind="   ").rstrip()  # remove the end newline

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
    html = hr.Element("some content")
    file_contents = render_result(html, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(" " * hr.Element.indent)


def test_multiple_indent():
    """
    make sure multiple levels get indented fully
    """
    body = hr.Body()
    body.append(hr.P("some text"))
    html = hr.Html(body)

    file_contents = render_result(html)

    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
        assert lines[i + 1].startswith(i * (" " * hr.Element.indent) + "<")

    assert lines[4].startswith(3 * (" " * hr.Element.indent) + "some")


def test_element_indent1():
    """
    Tests whether the Element indents at least simple content

    we are expecting to to look like this:

    <html>
        this is some text
    <\html>

    More complex indentation should be tested later.
    """
    elem = hr.Element("this is some text")

    # This uses the render_results utility above
    file_contents = render_result(elem).strip()

    # making sure the content got in there.
    assert "this is some text" in file_contents

    # break into lines to check indentation
    lines = file_contents.split("\n")
    # making sure the opening and closing tags are right.
    assert lines[0] == "<html>"
    # this line should be indented by the amount specified
    # by the class attribute: "indent"
    assert lines[1].startswith((" " * hr.Element.indent) + "thi")
    assert lines[2] == "</html>"
    assert file_contents.endswith("</html>")


def test_adjust_indent():
    """
    make sure multiple levels get indented fully with adjusted indent
    """
    hr.Element.indent = 2

    body = hr.Body()
    body.append(hr.P("some text"))
    html = hr.Html(body)

    file_contents = render_result(html)

    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
        assert lines[i + 1].startswith(i * (" " * hr.Element.indent) + "<")

    assert lines[4].startswith(3 * (" " * hr.Element.indent) + "some")


#####################
# Extra Tags
#####################


def test_img():
    """Test img element"""
    elem = hr.Img(src="eggs")
    elem.set_attributes(alt="spam")

    assert get_opening_line(elem) == '<img src="eggs" alt="spam" />'
