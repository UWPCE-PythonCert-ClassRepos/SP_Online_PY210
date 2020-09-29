"""
a simple script can run and test your html rendering classes.

Uncomment the steps as you add to your rendering.

"""

import os
from io import StringIO

# importing the html_rendering code with a short name for easy typing.
import html_render as hr


# writing the file out:
def render_page(page, filename, indent=None):  # pylint: disable=redefined-outer-name
    """
    render the tree of elements

    This uses StringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = StringIO()  # pylint: disable=invalid-name
    if indent is None:
        page.render(f)
    else:
        page.render(f, indent)

    print(f.getvalue())
    path = os.path.dirname(os.path.realpath(__file__))
    with open(path + "\\" + filename, "w") as outfile:
        outfile.write(f.getvalue())


# Step 1
#########
print("\n" + "Step 1".center(40, "-"))
page = hr.Element()

page.append(
    "Here is a paragraph of text -- there could be more of them, "
    "but this is enough  to show that we can do some text"
)

page.append("And here is another piece of text -- you should be able to add any number")

render_page(page, "test_html_output1.html")

# The rest of the steps have been commented out.
#  Uncomment them as you move along with the assignment.

## Step 2
##########
print("\n" + "Step 2".center(40, "-"))
page = hr.Html()

body = hr.Body()

body.append(
    hr.P(
        "Here is a paragraph of text -- there could be more of them, "
        "but this is enough  to show that we can do some text"
    )
)

body.append(
    hr.P("And here is another piece of text -- you should be able to add any number")
)

page.append(body)

render_page(page, "test_html_output2.html")

# Step 3
##########
print("\n" + "Step 3".center(40, "-"))

page = hr.Html()

head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(
    hr.P(
        "Here is a paragraph of text -- there could be more of them, "
        "but this is enough  to show that we can do some text"
    )
)
body.append(
    hr.P("And here is another piece of text -- you should be able to add any number")
)

page.append(body)

render_page(page, "test_html_output3.html")

# Step 4
##########
print("\n" + "Step 4".center(40, "-"))

page = hr.Html()

head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(
    hr.P(
        "Here is a paragraph of text -- there could be more of them, "
        "but this is enough  to show that we can do some text",
        style="text-align: center; font-style: oblique;",
    )
)

page.append(body)

render_page(page, "test_html_output4.html")

# Step 5
#########
print("\n" + "Step 5".center(40, "-"))

page = hr.Html()

head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(
    hr.P(
        "Here is a paragraph of text -- there could be more of them, "
        "but this is enough  to show that we can do some text",
        style="text-align: center; font-style: oblique;",
    )
)

body.append(hr.Hr())

page.append(body)

render_page(page, "test_html_output5.html")

# Step 6
#########
print("\n" + "Step 6".center(40, "-"))

page = hr.Html()

head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(
    hr.P(
        "Here is a paragraph of text -- there could be more of them, "
        "but this is enough  to show that we can do some text",
        style="text-align: center; font-style: oblique;",
    )
)

body.append(hr.Hr())

body.append("And this is a ")
body.append(hr.A("http://google.com", "link"))
body.append("to google")

page.append(body)

render_page(page, "test_html_output6.html")

# Step 7
#########
print("\n" + "Step 7".center(40, "-"))

page = hr.Html()

head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(hr.H(2, "PythonClass - Class 6 example"))

body.append(
    hr.P(
        "Here is a paragraph of text -- there could be more of them, "
        "but this is enough  to show that we can do some text",
        style="text-align: center; font-style: oblique;",
    )
)

body.append(hr.Hr())

_list = hr.Ul(id="TheList", style="line-height:200%")

_list.append(hr.Li("The first item in a list"))
_list.append(hr.Li("This is the second item", style="color: red"))

item = hr.Li()
item.append("And this is a ")
item.append(hr.A("http://google.com", "link"))
item.append("to google")

_list.append(item)

body.append(_list)

page.append(body)

render_page(page, "test_html_output7.html")

# Step 8 and 9
##############
print("\n" + "Step 8/9".center(40, "-"))

page = hr.Html()


head = hr.Head()
head.append(hr.Meta(charset="UTF-8"))
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(hr.H(2, "PythonClass - Example"))

body.append(
    hr.P(
        "Here is a paragraph of text -- there could be more of them, "
        "but this is enough  to show that we can do some text",
        style="text-align: center; font-style: oblique;",
    )
)

body.append(hr.Hr())

_list = hr.Ul(id="TheList", style="line-height:200%")

_list.append(hr.Li("The first item in a list"))
_list.append(hr.Li("This is the second item", style="color: red"))

item = hr.Li()
item.append("And this is a ")
item.append(hr.A("http://google.com", "link"))
item.append("to google")

_list.append(item)

body.append(_list)

page.append(body)

render_page(page, "test_html_output8.html")
