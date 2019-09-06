#!/usr/bin/env python

from collections import OrderedDict

def page_color(fore_color="blue", back_color="red", link_color="purple", visited_color="green"):
    return {'fore_color':fore_color, 
            'back_color':back_color, 
            'link_color':link_color,
            'visited_color':visited_color}


def new_func(*argv, **kwargv):
    print(argv)
    print(kwargv)
    

    colors = {'fore_color':'blue',
                'back_color':'red',
                'link_color':'purple',
                'visited_color':'green'}
    color_dict = {0:'fore_color',
                    1:'back_color',
                    2:'link_color',
                    3:'visited_color'}

    for i, arg in enumerate(argv):
        colors[color_dict[i]] = arg
        # print(color_dict[i])

    for key, value in kwargv.items():
        colors[key] = value
    

    print(colors)
    return colors