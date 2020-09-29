"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io
import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from html_render import *

indent = Element.indent

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


def test_one_line():
    h = Head()
    h.append(Title("OneLineTitle"))

    file_contents = render_result(h)

    assert "OneLineTitle" in file_contents
    start = file_contents.index("<title")
    end = file_contents.index("</title>")
    assert start < end

    # No newlines between start and end
    try:
        i = file_contents[start:end].index("\n")
        assert False
    except ValueError:
        assert True

    assert file_contents.index("<head") < file_contents.index("</head>")
    assert file_contents.index("<head") < file_contents.index("<title")
    assert file_contents.index("</title>") < file_contents.index("</head>")


def test_attributes():
    h = Head(attr1="attribute 1", attr2="attribute_2")
    h.append(Title("title content", title_attr="attribute for title"))

    file_contents = render_result(h)
    lines = file_contents.split('\n')

    assert lines[0] == '<head attr1="attribute 1" attr2="attribute_2">'
    assert lines[1] == indent + '<title title_attr="attribute for title">title content</title>'
    assert lines[2] == '</head>'


def test_one_line_attributes():
    t = Title("OneLine Title", id='hello', number=45)
    file_contents = render_result(t)

    assert "OneLine Title" in file_contents
    assert file_contents.index("<title") < file_contents.index("</title>")
    assert 'id="hello"' in file_contents
    assert 'number="45' in file_contents
    assert '"hello" number' in file_contents
    assert file_contents.index("<title") < file_contents.index("id=") < file_contents.index("</title>")


def test_self_closing():
    br = Br()
    hr = Hr(id="hrule")

    br_text = render_result(br).strip()
    assert br_text == '<br />'

    hr_text = render_result(hr).strip()
    assert hr_text == '<hr id="hrule" />'


def test_self_closing_in_context():
    """Test self closing tags within other elements"""
    h = Head()
    h.append(Br(attr='attribute'))
    h.append(Hr())

    file_contents = render_result(h)
    lines = file_contents.split('\n')

    assert lines[0] == '<head>'
    assert lines[1] == indent + '<br attr="attribute" />'
    assert lines[2] == indent + '<hr />'
    assert lines[3] == '</head>'


def test_self_closing_content():

    with pytest.raises(TypeError):
        h = Hr(content='content', id=2)

    b = Br()
    with pytest.raises(TypeError):
        b.append(Hr())


def test_a():

    a = A('http://www.google.com', 'This is a link to Google')
    contents = render_result(a)
    assert contents.strip() == '<a href="http://www.google.com">This is a link to Google</a>'


def test_li():

    li = Li("List content", list_attr="list attr")
    content = render_result(li)

    assert content == '<li list_attr="list attr">\n' + indent + 'List content\n</li>\n'


def test_ul_basic():

    ul = Ul()
    ul.append('content 1')
    ul.append(Li('content 2', attr='2nd attribute'))

    contents = render_result(ul)
    lines = contents.split('\n')

    assert lines[0] == '<ul>'
    assert lines[1:4] == [indent + '<li>', 2 * indent + 'content 1', indent + '</li>']
    assert lines[4:7] == [indent + '<li attr="2nd attribute">', 2 * indent + 'content 2',
                          indent + '</li>']


def test_ul_advanced():

    ul = Ul("first entry", ul_attr="test attribute")
    ul.append(Li('content 2'))

    ul2 = Ul(Li("second entry", li_attr="attribute"))

    H = Html()
    H.append(ul)
    H.append(ul2)

    contents = render_result(H)

    list_1 = f'{indent}<ul ul_attr="test attribute">\n{2 * indent}<li>\n{3 * indent}first entry\n' + \
             f'{2 * indent}</li>\n{2 * indent}<li>\n' + \
             f'{3 * indent}content 2\n{2 * indent}</li>\n{indent}</ul>'
    list_2 = f'{indent}<ul>\n{2 * indent}<li li_attr="attribute">\n{3 * indent}second entry\n' + \
             f'{2 * indent}</li>\n{indent}</ul>'

    assert list_1 in contents
    assert list_2 in contents
    assert contents.index(list_1) < contents.index(list_2)


def test_h():

    h1 = H(1)
    h1_1 = H(1, "some content")
    h2 = H(2, "some more content")

    h = Html()
    h.append(h1)
    h.append(h1_1)
    h.append(h2)

    contents = render_result(h)
    lines = contents.split("\n")

    # Remove !DOCTYPE line
    lines = lines[1:]
    assert lines[1].strip() == '<h1></h1>'
    assert lines[2].strip() == '<h1>some content</h1>'
    assert lines[3].strip() == '<h2>some more content</h2>'


def test_html_doctype():
    h = Html()
    lines = render_result(h).split('\n')
    assert lines[0] == '<!DOCTYPE html>'
    assert lines[1] == '<html>'
    assert lines[-2] == '</html>'

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
    <\html>

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


def test_class_indent_attribute():

    Element.indent = ''  # No indentation should occur now

    h = Html()
    b = Body()
    h.append(b)

    content = render_result(h).strip().split('\n')
    for line in content:
        assert not line.startswith(' ')

