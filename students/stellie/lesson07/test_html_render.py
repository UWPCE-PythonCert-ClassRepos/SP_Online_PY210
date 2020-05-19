"""
Test code for html_render.py
"""

import io
import pytest
from html_render import *


# Utility function for testing render methods
def render_result(element, ind=''):
    """Calls element's render method, and returns what rendered as a string"""
    # StringIO object provides methods of a file, but keeps everything in memory
    outfile = io.StringIO()
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    return outfile.getvalue()

########
# Step 1
########


# def test_init():
#     """Tests that program can be initialized with and without some content"""
#     e = Element()
#     e = Element('this is some text')


# def test_append():
#     """Tests whether or not you can append text"""
#     e = Element('this is some text')
#     e.append('some more text')


# def test_render_element():
#     """Tests whether Element can render two pieces of text"""
#     e = Element('this is some text')
#     e.append('and this is some more text')

#     # This uses render_results utility above
#     file_contents = render_result(e).strip()
#     print(file_contents)

#     # Make sure the content got in there
#     assert('this is some text') in file_contents
#     assert('and this is some more text') in file_contents

#     # Make sure order is correct
#     assert file_contents.index('this is') < file_contents.index('and this')

#     # Make sure the opening and closing tags are correct
#     assert file_contents.startswith('<html>')
#     assert file_contents.endswith('</html>')
#     assert file_contents.count('<html>') == 1
#     assert file_contents.count('</html>') == 1


# def test_render_element2():
#     """Tests whether Element can render two pieces of text"""
#     e = Element()
#     e.append('this is some text')
#     e.append('and this is some more text')

#     # This uses render_results utility above
#     file_contents = render_result(e).strip()
#     print(file_contents)

#     # Make sure the content got in there
#     assert('this is some text') in file_contents
#     assert('and this is some more text') in file_contents

#     # Make sure order is correct
#     assert file_contents.index('this is') < file_contents.index('and this')

#     # Make sure the opening and closing tags are correct
#     assert file_contents.startswith('<html>')
#     assert file_contents.endswith('</html>')
#     assert file_contents.count('<html>') == 1
#     assert file_contents.count('</html>') == 1

########
# Step 2
########


# Tests for new tags
def test_html():
    e = Html('this is some text')
    e.append('and this is some more text')

    file_contents = render_result(e).strip()

    assert('this is some text') in file_contents
    assert('and this is some more text') in file_contents
    print(file_contents)
    assert file_contents.endswith('</html>')


def test_body():
    e = Body('this is some text')
    e.append('and this is some more text')

    file_contents = render_result(e).strip()

    assert('this is some text') in file_contents
    assert('and this is some more text') in file_contents

    assert file_contents.startswith('<body>')
    assert file_contents.endswith('</body>')


def test_p():
    e = P('this is some text')
    e.append('and this is some more text')

    file_contents = render_result(e).strip()

    assert('this is some text') in file_contents
    assert('and this is some more text') in file_contents

    assert file_contents.startswith('<p>')
    assert file_contents.endswith('</p>')


def test_sub_element():
    """Tests that adding another element will still render properly"""
    page = Html()
    page.append('some plain text.')
    page.append(P('A simple paragraph of text'))
    page.append('Some more plain text.')

    file_contents = render_result(page)
    print(file_contents)

    assert 'some plain text' in file_contents
    assert 'A simple paragraph of text' in file_contents
    assert 'Some more plain text.' in file_contents
    assert 'some plain text' in file_contents
    assert '<p>' in file_contents  # check embedded element's tags are rendered
    assert '</p>' in file_contents


########
# Step 3
########


def test_head():
    e = Head('this is some text')
    e.append('and this is some more text')

    file_contents = render_result(e).strip()
    print(file_contents)

    assert('this is some text') in file_contents
    assert('and this is some more text') in file_contents
    assert file_contents.index('this is') < file_contents.index('and this')

    assert file_contents.startswith('<head>')
    assert file_contents.endswith('</head>')


def test_title():
    e = Title('This is a Title')

    file_contents = render_result(e).strip()

    assert('This is a Title') in file_contents
    print(file_contents)
    assert '\n' not in file_contents
    assert file_contents.startswith('<title>')
    assert file_contents.endswith('</title>')


def test_one_line_tag_append():
    """Test inability to append content to a OneLineTag"""
    e = OneLineTag('the initial content')
    with pytest.raises(NotImplementedError):
        e.append('some more content')

    file_contents = render_result(e).strip()
    print(file_contents)


########
# Step 4
########


def test_attributes():
    e = P('A paragraph of text', style='text-align: center', id='intro')

    file_contents = render_result(e).strip()
    print(file_contents)

    assert 'A paragraph of text' in file_contents
    assert file_contents.endswith('</p>')
    assert file_contents.startswith('<p ')
    assert 'style="text-align: center"' in file_contents
    assert 'id="intro"' in file_contents
    assert file_contents[:file_contents.index('>')].count(' ') == 3


def test_attributes2():
    e = Body('some text content', id='TheList', style='line-height:200%')

    file_contents = render_result(e).strip()
    print(file_contents)

    assert 'some text content' in file_contents
    assert file_contents.endswith('</body>')
    assert file_contents.startswith('<body ')
    assert 'style="line-height:200%"' in file_contents
    assert 'id="TheList"' in file_contents
    assert file_contents[:file_contents.index('>')].count(' ') == 2


########
# Step 5
########


def test_hr():
    """Test simple horizontal rule with no attributes"""
    hr = Hr()
    file_contents = render_result(hr)
    print(file_contents)
    assert file_contents == '<hr />\n'


def test_hr_attr():
    """Test horizontal rule with an attribute"""
    hr = Hr(width=400)
    file_contents = render_result(hr)
    print(file_contents)
    assert file_contents == '<hr width="400" />\n'


def test_br():
    """Test break in line with no attributes"""
    br = Br()
    file_contents = render_result(br)
    print(file_contents)
    assert file_contents == '<br />\n'


def test_content_in_br():
    with pytest.raises(TypeError):
        br = Br('some content')


def test_append_content_in_br():
    with pytest.raises(TypeError):
        br = Br()
        br.append('some content')


########
# Step 6
########

# #####################
# # indentation testing
# #  Uncomment for Step 9 -- adding indentation
# #####################


# def test_indent():
#     """
#     Tests that the indentation gets passed through to the renderer
#     """
#     html = Html("some content")
#     file_contents = render_result(html, ind="   ").rstrip()  #remove the end newline

#     print(file_contents)
#     lines = file_contents.split("\n")
#     assert lines[0].startswith("   <")
#     print(repr(lines[-1]))
#     assert lines[-1].startswith("   <")


# def test_indent_contents():
#     """
#     The contents in a element should be indented more than the tag
#     by the amount in the indent class attribute
#     """
#     html = Element("some content")
#     file_contents = render_result(html, ind="")

#     print(file_contents)
#     lines = file_contents.split("\n")
#     assert lines[1].startswith(Element.indent)


# def test_multiple_indent():
#     """
#     make sure multiple levels get indented fully
#     """
#     body = Body()
#     body.append(P("some text"))
#     html = Html(body)

#     file_contents = render_result(html)

#     print(file_contents)
#     lines = file_contents.split("\n")
#     for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
#         assert lines[i + 1].startswith(i * Element.indent + "<")

#     assert lines[4].startswith(3 * Element.indent + "some")


# def test_element_indent1():
#     """
#     Tests whether the Element indents at least simple content

#     we are expecting to to look like this:

#     <html>
#         this is some text
#     <\html>

#     More complex indentation should be tested later.
#     """
#     e = Element("this is some text")

#     # This uses the render_results utility above
#     file_contents = render_result(e).strip()

#     # making sure the content got in there.
#     assert("this is some text") in file_contents

#     # break into lines to check indentation
#     lines = file_contents.split('\n')
#     # making sure the opening and closing tags are right.
#     assert lines[0] == "<html>"
#     # this line should be indented by the amount specified
#     # by the class attribute: "indent"
#     assert lines[1].startswith(Element.indent + "thi")
#     assert lines[2] == "</html>"
#     assert file_contents.endswith("</html>")
