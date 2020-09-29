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


### Create Content
## Environment Details
enviro_intro = hr.Li("I started by setting up my environment: ")
enviro_details_list = hr.Ul(id="EnviroDetails", style="line-height:200%")

enviro_detail_1 = hr.Li("For my IDE I've chosen: ")
enviro_detail_1.append(
    hr.A(link="https://code.visualstudio.com/", content="VSCode", target="_blank")
)

enviro_detail_2 = hr.Li("I use ")
enviro_detail_2.append(
    hr.A(link="https://docs.pytest.org/en/stable/", content="PyTest", target="_blank")
)
enviro_detail_2.append("for my testing framework.")

enviro_detail_3 = hr.Li("When I finish a lesson, I commit to this ")
enviro_detail_3.append(
    hr.A(
        link="https://github.com/jacobian91/SP_Online_PY210",
        content="repo.",
        target="_blank",
    )
)

enviro_detail_4 = hr.Li("Then submit pull requests to this ")
enviro_detail_4.append(
    hr.A(
        link="https://github.com/UWPCE-PythonCert-ClassRepos/SP_Online_PY210",
        content="repo.",
        target="_blank",
    )
)

enviro_details_list.append(enviro_detail_1)
enviro_details_list.append(enviro_detail_2)
enviro_details_list.append(enviro_detail_3)
enviro_details_list.append(enviro_detail_4)
enviro_intro.append(enviro_details_list)


## Pull Request History
pr_history_intro = hr.Li("I've had multiple submissions merged already ")
pr_history_list = hr.Ul(id="PRHistoryMerged", style="line-height:200%")
pr_history_1 = hr.Li("I finished Lesson 2: ")

pr_history_1.append(
    hr.A(
        "https://github.com/UWPCE-PythonCert-ClassRepos/SP_Online_PY210/pull/1058",
        "Pull Request 1058",
        target="_blank",
    )
)
pr_history_2 = hr.Li("I finished Lesson 2: ")

pr_history_2.append(
    hr.A(
        "https://github.com/UWPCE-PythonCert-ClassRepos/SP_Online_PY210/pull/1062",
        "Pull Request 1062",
        target="_blank",
    )
)
pr_history_3 = hr.Li("I finished Lesson 3: ")

pr_history_3.append(
    hr.A(
        "https://github.com/UWPCE-PythonCert-ClassRepos/SP_Online_PY210/pull/1069",
        "Pull Request 1069",
        target="_blank",
    )
)

pr_history_list.append(pr_history_1)
pr_history_list.append(pr_history_2)
pr_history_list.append(pr_history_3)
pr_history_intro.append(pr_history_list)

## Assemble Page

page = hr.Html()


head = hr.Head()
head.append(hr.Meta(charset="UTF-8"))
head.append(hr.Title("Jacobian Python"))

page.append(head)

body = hr.Body()

body.append(hr.H(2, "This is what I've done in PY210 so far."))


# body.append(hr.Hr())

_list = hr.Ul(id="TheList", style="line-height:200%")


_list.append(enviro_intro)
_list.append(pr_history_intro)


body.append(_list)
body.append(
    hr.Img(
        src="https://imgs.xkcd.com/comics/python.png",
        title="I wrote 20 short programs in Python yesterday.  It was wonderful.  Perl, I'm leaving you.",
    )
)

page.append(body)

render_page(page, "test_jacobian.html")
