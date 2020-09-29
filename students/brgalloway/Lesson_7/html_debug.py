from html_render import *
import io


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

def test_attributes():
    e = Html()
    e.append(P("A paragraph of text", style="text-align: center", id="intro"))
    print(e)
    file_contents = render_result(e).strip()
    print(file_contents)
    assert("A paragraph of text") in file_contents
    assert file_contents.startswith("<p")
    assert file_contents.endswith("</p>")
    assert file_contents[:-1].index(">") > file_contents.index('id="intro"')
    assert file_contents[:file_contents.index(">")].count(" ") == 3
test_attributes()