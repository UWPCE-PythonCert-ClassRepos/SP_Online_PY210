#!/usr/bin/env python

def color_fun(fore_color = 'red', back_color = 'blue', link_color = 'yellow', visited_color = 'green'):
    return "{} {} {} {}".format(fore_color, back_color, link_color, visited_color)
    

def color_args_kwargs(*args, **kwargs):
    color_list = []
    for word in args:
        color_list.append(word)
    for word in kwargs.values():
        color_list.append(word)
    
    return "{}".format(" ".join(color_list))