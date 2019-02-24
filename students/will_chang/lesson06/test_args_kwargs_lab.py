#!/usr/bin/env python

"""
Default values for color_fun(fore_color = 'red', back_color = 'blue', link_color = 'yellow', visited_color = 'green')
"""

from args_kwargs_lab import color_fun, color_args_kwargs

def test_1():
    assert color_fun() == "red blue yellow green"


def test_2():
    assert color_fun('red', 'blue', 'yellow', 'chartreuse') == "red blue yellow chartreuse"
    assert color_args_kwargs('red', 'blue', 'yellow', 'chartreuse') == "red blue yellow chartreuse"
    

def test_3():
    assert color_fun(link_color='red', back_color='blue') == "red blue red green"
    assert color_args_kwargs(link_color='red', back_color='blue') == "red blue"

    
def test_4():
    assert color_fun('purple', link_color='red', back_color='blue') == "purple blue red green"
    assert color_args_kwargs('purple', link_color='red', back_color='blue') == "purple red blue"
    

def test_5():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert color_fun(*regular, **links) == "red blue chartreuse green"
    assert color_args_kwargs(*regular, **links) == "red blue chartreuse"