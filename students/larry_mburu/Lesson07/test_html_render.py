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

def test_head(): 
    """
    tests the head element
    """
    e = Head()
     

    file_contents = render_result(e).strip() 

    assert file_contents.startswith("<head>")
    assert file_contents.endswith("</head>")

def test_OneLineTag(): 
    """
    tests OneLineTag 
    """

    e = OneLineTag()
    e.append("some test text")

    file_contents = render_result(e).strip()

    assert file_contents.startswith("<title>")
    assert file_contents.endswith("</title>")
    assert "some test text" in file_contents
    assert "<title>some test text</title>" in file_contents

def test_title():
    """
    test title tag
    """
    e = Title() 
    e.append("PythonClass - Session 7, very cool")

    file_contents = render_result(e).strip()
    assert file_contents.startswith("<title>")
    assert file_contents.endswith("</title>")
    assert "<title>PythonClass - Session 7, very cool</title>" in file_contents

def test_page_build(): 
    """
    test the complete page build
    """

    html = Html()

    #construct heading page
    head = Head() 
    title = Title()
    title.append("PythonClass - Session 7, very cool") 
    head.append(title)
    
    #construct mid page
    body = Body() 
    paragraph_one = P("Here is a paragraph of text -- there could be more of them, but this is enough to show that we can do some text")
    paragraph_two = P("And here is another piece of text -- you should be able to add any number")
    body.append(paragraph_one)
    body.append(paragraph_two)    

    #construct the whole page
    html.append(head)
    html.append(body)

    file_contents = render_result(html).strip()
    assert "Here is a paragraph" in file_contents
    assert "And here is another" in file_contents

# ########
# STEP 4
# ########

def test_element_attr(): 
    """
    tests the addition of attributes to the element constructor 
    using **kwargs
    """
    element = Element(attr1="attribute1", attr2="attribute2")
    assert 'attr1' and 'attr2' in list( getattr(element, 'attributes') )

def test_render_openning_tag(): 
    """
    tests opening tag rendering function
    """ 
    element = Element(attr1="attribute1", attr2="attribute2")
    attributes = element.render_opening_tag()

    assert '<html attr1="attribute1" attr2="attribute2">' == attributes

def test_p_element_with_attrs(): 
    paragraph = P("This is a test", style="text-align: center; font-style: oblique;")
    file_contents = render_result(paragraph).strip()
    assert "style" in file_contents
    assert 'style="text-align: center; font-style: oblique;"' in file_contents

# ########
# STEP 5
# ########

def test_self_closing_element():
    #self_closing_tag = SelfClosingTag("somecontent", width=400) # with content 
    self_closing_element  = SelfClosingTag(width=400)  #without content
    file_contents = render_result(self_closing_element).strip()
    assert file_contents.startswith("<hr ")
    assert file_contents.endswith("/>")

def test_hr_element(): 
    #self_closing_tag = SelfClosingTag("somecontent", width=400) # with content 
    hr_element  = Hr(width=400)  #without content
    file_contents = render_result(hr_element).strip()
    assert file_contents.startswith("<hr ")
    assert file_contents.endswith("/>")

def test_br_element(): 
    #self_closing_tag = SelfClosingTag("somecontent", width=400) # with content 
    br_element  = Br(width=400)  #without content
    file_contents = render_result(br_element).strip()
    #assert 'width=400' in file_contents
    assert file_contents.startswith("<br ")
    assert file_contents.endswith("/>")

# ########
# STEP 6
# ########

def test_A_element(): 
    a_element = A("http://google.com", "link to google")
    assert 'href' in a_element.attributes
    assert  a_element.attributes['href'] == 'http://google.com'

    file_contents = render_result(a_element).strip() 
    assert file_contents.startswith("<a")

# ########
# STEP 7
# ########

def test_Ul_li_elements(): 

    Ul_element = Ul(id="TheList", style="line-height:200%")
    li_element_one = Li()
    li_element_two = Li() 

    li_element_one.append('the first item')
    li_element_two.append('This is the second item')

    Ul_element.append(li_element_one) 
    Ul_element.append(li_element_two) 

    file_contents = render_result(Ul_element).strip() 
    assert file_contents.startswith("<ul")
    assert file_contents.endswith("</ul>")
    assert file_contents.find('<li>') != -1  #validate <li> in <ul> element

def test_Header_element(): 
    header_element = H(2, "the text header")
    assert header_element.level == 2
    assert "the text header" in header_element.content 

# ########
# STEP 8
# ########

def test_doctype_html_element(): 
    html_element = Html("somecontent")
    file_contents = render_result(html_element).strip()
    
    assert file_contents.startswith('<!DOCTYPE')

def test_meta_element(): 
    head_element = Head()
    meta_element = Meta(charset="UTF-8")
    head_element.append(meta_element) 

    assert meta_element.attributes['charset'] == "UTF-8"

    file_contents = render_result(head_element)
    assert file_contents.find('<meta>') != 1 # confirm meta element in head element

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
     assert lines[1].startswith("   <")
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
#    for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
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
