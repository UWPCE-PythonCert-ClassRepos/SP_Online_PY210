import io
from html_render import *

# For testing render methods
def render_result(element, ind=""):
    outfile = io.StringIO()
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    return outfile.getvalue()

# Test render methods
def test_render():
    e = Element()
    e = Element("Hello!")
    e.append("HI")
    e.append(" you are Chelsea")
    file_contents = render_result(e).strip()
    assert "Hello!" in file_contents
    assert " you are Chelsea" in file_contents
    assert file_contents.index("Hello") < file_contents.index(" you are Chelsea")

# ----------------Test elements ---------
def test_unorderedlist():
    e = Ul("What-up")
    e.append("texttexttext")
    file_contents = render_result(e).strip()
    assert "text" in file_contents
    assert file_contents.startswith("<ul>")
    assert file_contents.endswith("</ul>")

def test_listitem():
    e = Li("hey")
    file_contents = render_result(e).strip()
    assert file_contents.startswith("<li>")
    assert "hey" in file_contents
    assert file_contents.endswith("</li>")

def test_HTML():
    e = Html()
    file_contents = render_result(e).strip()
    assert file_contents.startswith("<DOCTYPE html>")
    assert file_contents.endswith("</html>")

def test_body():
    e = Body()
    file_contents = render_result(e).strip()
    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")

# -------------------------------------------

# -------------- Test One Line Tags ------

def test_title():
    e = Title("Super")
    file_contents = render_result(e)
    assert file_contents.startswith('<title>')
    assert file_contents.endswith("/title>\n")

def test_link():
    e = A("http://google.com", "links to Bing")
    file_contents = render_result(e)
    assert file_contents.startswith('<a ')
    assert file_contents.endswith("/a>\n")


def test_header():
    e = H(5,'Header')
    file_contents = render_result(e).strip()
    assert file_contents.startswith('<h5>')
    assert 'Header' in file_contents
    assert file_contents.endswith('</h5>')
# -------------------------------------

#------- Testing Self-Closing Tags-------

def test_break():
    e = Br()
    file_contents = render_result(e)
    assert file_contents == "<br>\n"

def test_meta():
    e = Meta()
    file_contents = render_result(e)
    assert file_contents == "<meta>\n"

def test_horizontalrule():
    e = Hr()
    file_contents = render_result(e)
    assert file_contents == "<hr>\n"
# ----------------------------------
