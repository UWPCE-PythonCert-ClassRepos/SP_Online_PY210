#!/usr/bin/env python3

def colors(fore_color='red', back_color='black', link_color='blue', visited_color='purple'):
    print_string = "{} {} {} {}".format(fore_color, back_color, link_color, visited_color)
    return print_string


def colors2(*args, **kwargs):
    print(args)
    print(kwargs)
    color_length = len(args) + len(kwargs)
    color_string = " ".join(["{}"] * color_length)
    if kwargs:
        values = list()
        for v in kwargs.values():
            values.append(v)
        color_string = color_string.format(*args, *values)
    else:
        color_string = color_string.format(*args)

    return color_string