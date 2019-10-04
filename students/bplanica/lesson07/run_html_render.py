#!/usr/bin/env python3

"""
a simple script can run and test your html rendering classes.

Uncomment the steps as you add to your rendering.

"""

from io import StringIO

# importing the html_rendering code with a short name for easy typing.
import bp_html_render as hr


# writing the file out:
def render_page(page, filename, indent=None):
    """
    render the tree of elements

    This uses StringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = StringIO()
    if indent is None:
        page.render(f)
    else:
        page.render(f, indent)

    print(f.getvalue())
    with open(filename, 'w') as outfile:
        outfile.write(f.getvalue())

# # Step 8 and 9
# ##############

page = hr.Html()


head = hr.Head()
head.append( hr.Meta(charset="UTF-8") )
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append( hr.H(2, "PythonClass - Example") )

body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough to show that we can do some text",
                 style="text-align: center; font-style: oblique;"))

body.append(hr.Hr())

list = hr.Ul(id="TheList", style="line-height:200%")

list.append( hr.Li("The first item in a list") )
list.append( hr.Li("This is the second item", style="color: red") )

item = hr.Li()
item.append("And this is a ")
item.append( hr.A("http://google.com", "link") )
item.append("to google")

list.append(item)

body.append(list)

page.append(body)

render_page(page, "test_html_output8.html")
