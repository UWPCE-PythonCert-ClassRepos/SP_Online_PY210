#!/usr/bin/env python


def colors(fore_color='red', back_color='blue', link_color='yellow',
           visited_color='pink'):
    return [fore_color, back_color, link_color, visited_color]

def colors_2(*args, **kwargs):
    args_colors = list(args)
    kwargs_colors = list()
    for key in kwargs.keys():
        kwargs_colors.append(kwargs[key])
    colors = args_colors + kwargs_colors
    return [colors, args_colors, kwargs_colors]

colors_tuple = ('turquoise', 'brown')
colors_dict = {'Best Color': 'Aggie Maroon', 'Worst Color': 'Burnt Orange'}
colors_2(colors_tuple, colors_dict)
