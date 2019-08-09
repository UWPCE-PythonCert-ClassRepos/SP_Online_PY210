#!/usr/bin/env python3

"""
Test script for the html_renderer exercise

"""

from io import StringIO
import pytest

# importing the html_rendering code with a short name for easy typing.
import html_render as hr

def render_result(element, ind=""):
    """
    gives the text string of what's rendered to the file, we'll use this for validation
    """
    outfile = StringIO()
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    return outfile.getvalue()


def test_html():
    page = hr.Html()
    contents = render_result(page)
    assert "<html>" in contents
    assert "</html>" in contents


def test_body():
    page = hr.Body()
    contents = render_result(page)
    assert "<body>" in contents
    assert "</body>" in contents


def test_append():
    page = hr.Html()
    body = hr.Body()
    body.append("this is a test")
    page.append(body)
    contents = render_result(page)
    assert "this is a test" in contents


def test_title():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    contents = render_result(page)
    assert "<title>PythonClass = Revision 1087:</title>" in contents

def test_paragraph():
    page = hr.Html()
    body = hr.Body()
    body.append(hr.P("Paragraph 1"))
    body.append(hr.P("Paragraph 2"))
    page.append(body)
    contents = render_result(page)
    assert "<p>Paragraph 1</p>" in contents
    assert "<p>Paragraph 2</p>" in contents

def test_br():
    br = hr.Br()
    contents = render_result(br)
    assert contents.startswith("<br>")

def test_contents_in_br():
    # Make sure our exception in the self-closing element works
    with pytest.raises(TypeError):
        br = hr.Br("this shouldn't work")
        contents = render_result(br)


def test_append_to_br():
    # Make sure our exception in the self-closing element works
    with pytest.raises(TypeError):
        br = hr.Br()
        br.append("this shouldn't work")
        contents = render_result(br)

def test_meta():
    meta = hr.Meta(charset="UTF-8")
    contents = render_result(meta)
    assert contents.startswith('<meta "charset=UTF-8">')


def test_self_closing_element():
    br = hr.Br()
    contents = render_result(br)
    assert contents.startswith("<br>")
    with pytest.raises(TypeError):
        br = hr.Br("this shouldn't work")
        contents = render_result(br)


def test_one_line_element():
    title = hr.Title("this is the title")
    # test with no attribute
    p = hr.P()
    contents = render_result(title)
    assert contents.startswith("<title>this is the title</title>")
    contents = render_result(p)
    assert contents.startswith("<p></p>")
    print(contents)


def test_style():
    page = hr.Html()
    body = hr.Body()
    body.append(hr.P("Paragraph 1",
                     style="text-align: center; font-style: oblique;"))
    page.append(body)
    contents = render_result(page)
    assert "Paragraph 1" in contents
    assert "<p style=text-align: center; font-style: oblique;>" in contents
    assert "</p>" in contents
    print(contents)


def test_link():
    page = hr.Html()
    body = hr.Body()
    body.append("And this is a ")
    body.append(hr.A("http://google.com", "link"))
    body.append("to google")
    page.append(body)
    contents = render_result(page)
    assert "And this is a" in contents
    assert "<a href=http://google.com>link</a>" in contents
    assert "to google" in contents


def test_heading():
    page = hr.Html()
    head = hr.Head()
    body = hr.Body()
    body.append(hr.H(2, "Heading 2"))
    body.append(hr.H(4, "Heading 4"))
    page.append(body)
    contents = render_result(page)
    assert "<h2>Heading 2</h2>" in contents
    assert "<h4>Heading 4</h4>" in contents


def test_list():
    page = hr.Html()
    body = hr.Body()
    list = hr.Ul(id="TheList", style="line-height:200%")
    list.append(hr.Li("The first item in a list"))
    list.append(hr.Li("This is the second item", style="color: red"))
    item = hr.Li()
    item.append("And this is a ")
    item.append(hr.A("http://google.com", "link"))
    item.append("to google")
    list.append(item)
    body.append(list)
    page.append(body)
    contents = render_result(page)
    assert '<ul "id=TheList" "style=line-height:200%">' in contents
    assert "<li>\nThe first item in a list\n</li>" in contents.replace("  ", "")
    assert '<li "style=color: red">\nThis is the second item\n</li>' in contents.replace("  ", "")
    assert '<li>\nAnd this is a \n<a href=http://google.com>link</a>\nto google\n</li>' in contents.replace("  ", "")
    assert "</li>\n</ul>" in contents.replace("  ", "")


def test_indent():
    # Test that indentation is working as expected
    page = hr.Html()
    body = hr.Body()
    head = hr.Head()
    head.append(hr.Title("Title"))
    body.append(hr.P("Paragraph 1"))
    page.append(head)
    page.append(body)
    contents = render_result(page)
    assert contents.startswith("<html>")
    lines = contents.split("\n")
    assert lines[1] == "    <head>"
    assert lines[2].startswith("        <title>")
    assert lines[3] == "    </head>"
    assert lines[4] == "    <body>"
    assert lines[5].startswith("        <p>")
    assert lines[6] == "    </body>"
    assert lines[7].startswith("</html>")








