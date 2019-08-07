# fore_color = 'red'
# back_color = 'green'
# link_color = 'blue'
# visited_color = 'yellow'


def colors(fore_color='red', back_color='green',
           link_color='blue', visited_color='yellow'):
    return (fore_color, back_color, link_color, visited_color)


def colors1(*args, **kwargs):
    print("the positional arguments are: ", args)
    print("the keyword arguments are: ", kwargs)

    arg_tuple = ("fore_color", "back_color", "link_color", "visited_color")

    colors_dict = {}
    # default values
    colors_dict["fore_color"] = "red"
    colors_dict["back_color"] = "green"
    colors_dict["link_color"] = "blue"
    colors_dict["visited_color"] = "yellow"

    for i, color in enumerate(args):
        colors_dict[arg_tuple[i]] = color

    for key, color in kwargs.items():
        colors_dict[key] = color

    return colors_dict["fore_color"], colors_dict["back_color"], colors_dict["link_color"], colors_dict["visited_color"]
    