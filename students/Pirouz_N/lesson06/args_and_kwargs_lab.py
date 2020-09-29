#!/usr/bin/env python

"""
Creating a function that returns a set of parameters to check argument passing behavior in python
"""


def func(fore_color='black', back_color='black', link_color='black', visited_color='black'):
    return 'fore_color is {} back_color is {} link_color is {} visited_color is {}'\
        .format(fore_color, back_color, link_color, visited_color)


def func2(*args):
    return 'fore_color is {} back_color is {} link_color is {} visited_color is {}'\
        .format(*args)


def func3(**kwargs):
    return 'fore_color is {fore_color} back_color is {back_color}' \
           ' link_color is {link_color} visited_color is {visited_color}'\
        .format(**kwargs)


def func4(*args, **kwargs):
    return 'fore_color is {} back_color is {}' \
           ' link_color is {link_color} visited_color is {visited_color}'\
        .format(*args, **kwargs)