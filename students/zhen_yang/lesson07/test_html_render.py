"""
test code for html_render.py

This is just a start -- you will need more tests!
"""
import io
import pytest

# import * is often bad form, but makes it easier to test
# everything in a module.
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
"""
def test_init():
    # This only tests that it can be initialized with and without
    # some content -- but it's a start
    e = Element()

    e = Element("this is some text")


def test_append():
    #This tests that you can append text
    #It doesn't test if it works --
    #that will be covered by the render test later

    e = Element("this is some text")
    e.append("some more text")


def test_render_element():
    # Tests whether the Element can render two pieces of text
    # So it is also testing that the append method works correctly.

    # It is not testing whether indentation or line feeds are correct.

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
# # Does it pass right away? yes
def test_render_element2():
     # Tests whether the Element can render two pieces of text
     # So it is also testing that the append method works correctly.
     # It is not testing whether indentation or line feeds are correct.

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
    # tests that you can add another element and still render properly
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
def test_sub_element2():
    # test the 'page', 'tile', 'head', 'body' elements
    page = Html()
    page.append('This is a page.')
    title = Title()
    title.append('This is title 1')
    title.append('This is title 2')
    page.append(title)
    page.append(Head('This is a head.'))
    body = Body('This is a body')
    body.append(P('This is a paragraph.'))
    page.append(body)

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    assert "This is a page" in file_contents
    assert "This is title 1 This is title 2" in file_contents
    assert "This is a head" in file_contents
    assert "This is a body" in file_contents
    assert "This is a paragraph" in file_contents
    assert "<title>" in file_contents
    assert "<head>" in file_contents
    assert "<body>" in file_contents
    assert "<p>" in file_contents

    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>\n")

########
# Step 4
########
def test_set_of_attributes():
    page = Html()
    page.append('This is a page.')
    title = Title('This is tltle 1', id="TheList", style="line-height:200%")
    title.append('This is title 2')
    page.append(title)
    page.append(Head('This is a head.'))
    body = Body('This is a body')
    attrs = {'class': 'intro'}
    p = P('This a paragraph.', style="text-align: center", id="intro", **attrs)
    body.append(p)
    body.append('This is another paragraph.')
    page.append(body)

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails
    print("End of file_contents")
    assert 'style="line-height:200%"' in file_contents
    assert 'class="intro"' in file_contents

########
# Step 5
########
def test_self_closing_tag():
    page = Html()
    page.append('This is a page.')
    title = Title('Testing SelfClosingTag ', id="TheList",
                  style="line-height:200%")
    page.append(title)
    body = Body('This is a body')
    body.append(Hr(width='400'))
    body.append('This is another paragraph.')
    page.append(body)

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails
    assert 'hr' in file_contents
    assert 'width="400"' in file_contents

########
# Step 6
########
def test_webpage_link():
    page = Html()
    page.append('This is a page.')
    title = Title('Testing webpage link')
    page.append(title)
    body = Body('This is a body')
    body.append(Hr(width='400'))
    body.append('This is the web page.')
    a = A('https://www.yahoo.com/', 'link')
    a.append('to yahoo')
    body.append(a)
    page.append(body)

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails
    assert 'yahoo' in file_contents

########
# Step 7
########
def test_Ul_Li_H_classes():
    page = Html()
    head = Head(Title('Testing Ul, Li, H classses'))
    page.append(head)
    body = Body("This is the body")
    # test the H class
    h = H(2, 'Testing Step 7 of lesson07')
    body.append(h)
    body.append(P('This is a paragraph', width='400'))
    body.append(Hr(width='800'))
    # test Ul list with Li objects on the list
    list = Ul(id='TheList', style='line-height:200%')
    li_1 = Li('The first item in a list')
    list.append(li_1)
    li_2 = Li('The second item in a list')
    list.append(li_2)

    item = Li()
    item.append('And this is a')
    item.append(A('http://google.com', 'link'))
    item.append('to google')
    list.append(item)

    body.append(list)
    page.append(body)

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails
    assert 'h2' in file_contents
    assert 'li' in file_contents
    assert 'ul' in file_contents
    assert 'Testing Step 7 of lesson07' in file_contents
    assert 'http://google.com' in file_contents
    assert 'The first item in a list' in file_contents

########
# Step 8
########

def test_Meta():
    page = Html()
    head = Head()
    head.append(Meta(charset="UTF-8"))
    head.append(Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = Body()
    body.append(H(2, "PythonClass - lesson07 example"))
    body.append(P("Here is a paragraph of text ",
                style="text-align: center; font-style: oblique;"))
    body.append(Hr())

    list = Ul(id="TheList", style="line-height:200%")
    list.append(Li("The first item in a list"))
    list.append(Li("This is the second item", style="color: red"))
    item = Li()
    item.append("And this is a")
    item.append(A("http://google.com", "link"))
    item.append("to google")
    list.append(item)
    body.append(list)
    page.append(body)

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails
    assert 'meta' in file_contents
    assert 'DOCTYPE' in file_contents


# #####################
# # indentation testing
# #  Uncomment for Step 9 -- adding indentation
# #####################


def test_indent():
    # Tests that the indentation gets passed through to the renderer

    html = Html("some content")
    #remove the end newline
    file_contents = render_result(html, ind="   ").rstrip()

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[0].startswith("   <")
    print(repr(lines[-1]))
    assert lines[-1].startswith("   <")


def test_indent_contents():
"""
# The contents in a element should be indented more than the tag
# by the amount in the indent class attribute
""""
    html = Element("some content")
    file_contents = render_result(html, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(Element.indent)


def test_multiple_indent():
# make sure multiple levels get indented fully
    body = Body()
    body.append(P("some text"))
    html = Html(body)

    file_contents = render_result(html)

    print(file_contents)
    lines = file_contents.split("\n")
    #for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
    for i in range(4):  # this needed to be adapted to the <DOCTYPE> tag
        assert lines[i].startswith((i + 1) * Element.indent + "<")
    assert lines[4].startswith(5 * Element.indent + "some")

"""

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
    print(file_contents)
    # making sure the content got in there.
    assert("this is some text") in file_contents
    # break into lines to check indentation
    lines = file_contents.split('\n')
    # making sure the opening and closing tags are right.
    assert lines[0] == "<html>"
    # this line should be indented by the amount specified
    # by the class attribute: "indent"
    #assert lines[1].startswith(Element.indent + "thi")
    assert lines[1].startswith(Element.indent * 2 + 'thi')
    assert lines[2] == "    </html>"
    assert file_contents.endswith(Element.indent + "</html>")
