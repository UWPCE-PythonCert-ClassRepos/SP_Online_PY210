"""
Programming In Python - Lesson 7 Assignment 1: HTML Renderer
Code Poet: Anthony McKeever
Start Date: 08/27/2019
End Date: 08/31/2019
"""

import io
import pytest

# import * is often bad form, but makes it easier to test everything in a module.
# from html_render_old import *
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

    content = render_result(e)
    assert f"{e.indent}this is some text" in content
    assert content.startswith("<html>")
    assert content.endswith("</html>\n")


def test_append():
    """
    This tests that you can append text

    It doesn't test if it works --
    that will be covered by the render test later
    """
    e = Element("this is some text")
    e.append("some more text")
    indent = e.indent

    content = render_result(e)
    assert f"{indent}this is some text" in content
    assert "some more text" in content
    assert f"{indent}this is some text\n{indent}some more text" in content
    assert content.startswith("<html>")
    assert content.endswith("</html>\n")


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
def test_header_elements():
    header = Head()
    header.append(Title("Studio Starchelle"))

    content = render_result(header)
    assert "<title>Studio Starchelle</title>" in content
    assert content.startswith("<head>") and content.endswith("</head>\n")


def test_header_as_child():
    page = Html()
    header = Head()
    title = Title("Studio Starchelle")
    header.append(title)
    page.append(header)

    body = Body()
    body.append(P("The Art of the Starchelle*Project 2019"))
    page.append(body)

    assert len(page.content) == 2
    assert header in page.content
    assert body in page.content
    assert title in page.content[0].content
    assert title not in page.content[1].content


def test_anchor():
    url = "https://ahc.gov/depts/doti"
    link_test = "AHC Department of Temporal Integrity"
    anchor = A(url, link_test)
    contents = render_result(anchor)

    assert contents.startswith(f"<a href=\"{url}\">")
    assert contents.endswith("</a>\n")
    assert contents.count(f">{link_test}<") == 1


def test_h():
    heading_text = "Sophie Loaphie Bakery"
    h_list = []
    for i in range(1, 5):
        h_list.append(H(i, heading_text, id=f"heading_{i}"))

    for i in range(len(h_list)):
        contents = render_result(h_list[i])
        assert contents.startswith(f"<h{i + 1} id=\"heading_{i + 1}\">")
        assert contents.endswith(f"</h{i + 1}>\n")
        assert heading_text in contents


def test_hr():
    hr = Hr()

    try:
        hr.append("Cresenta Starchelle")
    except TypeError as te:
        assert "Hr nodes cannot have innerHTML content." in str(te)

    contents = render_result(hr)
    assert contents == "<hr />\n"


def test_br():
    br = Br()

    try:
        br.append("Cresenta Starchelle")
    except TypeError as te:
        assert "Br nodes cannot have innerHTML content." in str(te)

    contents = render_result(br)
    assert contents == "<br />\n"
    

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
    <\\html>

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


def test_document_indent():
    page = Html()
    indent = page.indent

    title = Title("Sophie Loaphie Bakery")
    head = Head(title)
    page.append(head)

    h = H(1, "Sophie Loaphie Bakery")
    p = P("The Sophiest Bakery with the Loaphiest bread!")
    li = Li(A("https://github.com/snip3rm00n", "Our GitHub"))
    ul = Ul(li, id="our_links")
    ul.append(li)
    body = Body(h)
    body.append(p)
    body.append(ul)
    page.append(body)
    
    doc_type = render_result(DocType()).rstrip()
    file_contents = render_result(page).rstrip()
    total_indent = 0
    file_contents = file_contents.split("\n")
    last_close = False

    for line in file_contents:
        print(line)
        if "!DOC" in line:
            assert line == doc_type
            continue

        if "<html" in line:
            assert line == "<html>"
            continue
        
        single_line = any(elm in line for elm in ["<title", "<h1", "<a"])

        if last_close and not "</" in line:
            last_close = False
        elif single_line:
            total_indent = total_indent + 1
            last_close = True
        elif "</" in line:
            total_indent = total_indent - 1
            last_close = True
        else:
            total_indent = total_indent + 1

        print(single_line, total_indent)

        assert indent * total_indent in line
