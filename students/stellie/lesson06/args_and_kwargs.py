#!/usr/bin/env python3


def fun_colors(fore_color='red', back_color='blue', link_color='yellow',
               visited_color='green'):
    print(fore_color, back_color, link_color, visited_color)


fun_colors()  # default set
fun_colors('pink', 'navy', 'gold', 'lime')  # use just positional arguments
fun_colors(fore_color='magenta', back_color='aquamarine', link_color='mustard',
           visited_color='olive')  # use just keyword arguments
fun_colors('purple', 'cornflower', link_color='lemon',
           visited_color='emerald')  # use combination of pos/kw arguments
pos = ('orange', 'white')
kw = {'link_color': 'black', 'visited_color': 'gray'}
fun_colors(*pos, **kw)  # use tuple or dictionary
