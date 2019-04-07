#!/usr/bin/env python3

### Lesson 7 HTML Renderer Unit Test for html_render.py

import io
import pytest

from html_render import *


def render_result(element, ind=""):
    outfile = io.StringIO()
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    return outfile.getvalue()

# Step 1

def test_init():
    e = Element()

    e = Element("this is some text")


def test_append():
    e = Element("this is some text")
    e.append("some more text")


def test_render_element():
    e = Element("this is some text")
    e.append("and this is some more text")


    file_contents = render_result(e).strip()
    print(file_contents)

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents


    assert file_contents.index("this is") < file_contents.index("and this")


    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")

    assert file_contents.count("<html>") == 1
    assert file_contents.count("</html>") == 1


def test_render_element2():

    e = Element()
    e.append("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.index("this is") < file_contents.index("and this")

    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")

# Step 2

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

def test_p_newlines():

    e = P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e)

    print(file_contents)

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<p>\n")
    assert file_contents.endswith("</p>\n")


def test_sub_element():

    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)
    print(file_contents) 

    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents

    assert "<p>" in file_contents
    assert "</p>" in file_contents



# Step 3

def test_head():
    e = Head("This is a Header")

    file_contents = render_result(e).strip()

    assert("This is a Header") in file_contents

    assert file_contents.startswith("<head>")
    assert file_contents.endswith("</head>")


def test_title():
    e = Title("This is a Title")

    file_contents = render_result(e).strip()

    assert("This is a Title") in file_contents
    print(file_contents)
    assert file_contents.startswith("<title>")
    assert file_contents.endswith("</title>")
    assert "\n" not in file_contents


def test_one_line_tag_append():

    e = OneLineTag("the initial content")
    with pytest.raises(TypeError):
        e.append("some more content")


def test_attributes():
    e = P("A paragraph of text", style="text-align: center", id="intro")

    file_contents = render_result(e).strip()
    print(file_contents)  
    assert "A paragraph of text" in file_contents
    assert file_contents.endswith("</p>")

    assert file_contents.startswith("<p ")

    assert 'style="text-align: center"' in file_contents
    assert 'id="intro"' in file_contents

    assert file_contents[:-1].index(">") > file_contents.index('id="intro"')
    assert file_contents[:file_contents.index(">")].count(" ") == 3


# Step 5

def test_hr():
    hr = Hr()
    file_contents = render_result(hr)
    print(file_contents)
    assert file_contents == '<hr />\n'


def test_hr_attr():
    hr = Hr(width=400)
    file_contents = render_result(hr)
    print(file_contents)
    assert file_contents == '<hr width="400" />\n'


def test_br():
    br = Br()
    file_contents = render_result(br)
    print(file_contents)
    assert file_contents == "<br />\n"


def test_content_in_br():
    with pytest.raises(TypeError):
        br = Br("some content")


def test_append_content_in_br():
    with pytest.raises(TypeError):
        br = Br()
        br.append("some content")


def test_anchor():
    a = A("http://google.com", "link to google")
    file_contents = render_result(a)
    print(file_contents)
    assert file_contents.startswith('<a ')
    assert file_contents.endswith('</a>\n')
    assert 'href="http://google.com"' in file_contents
    assert 'link to google' in file_contents

# indentation testing

def test_indent():
    html = Html("some content")
    file_contents = render_result(html, ind="   ").rstrip()

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[0].startswith("   <")
    print(repr(lines[-1]))
    assert lines[-1].startswith("   <")


def test_indent_contents():

    html = Element("some content")
    file_contents = render_result(html, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(Element.indent)


def test_multiple_indent():

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

    e = Element("this is some text")
    file_contents = render_result(e).strip()
    assert("this is some text") in file_contents
    lines = file_contents.split('\n')
    assert lines[0] == "<html>"
    assert lines[1].startswith(Element.indent + "thi")
    assert lines[2] == "</html>"
    assert file_contents.endswith("</html>")