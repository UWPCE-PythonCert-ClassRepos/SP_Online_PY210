#!/usr/bin/env python

from args_kwargs_lab import colors, colors_args

# colors function tests
def test_1():
    assert colors() == ['red', 'blue', 'yellow', 'chartreuse']

def test_2():
    assert colors('black', 'blue', 'yellow', 'green') == ['black', 'blue', 'yellow', 'green']

def test_3():
    assert colors('orange', link_color="purple") == ['orange', 'blue', 'purple', 'chartreuse']

# colors_arg function tests
def test_4():
    assert colors_args() == []

def test_5():
    regular = ('black', 'green')
    links = {'link_color': 'pink', 'visited_color': 'teal'}
    assert colors_args(*regular, **links) == ['black', 'green', 'pink', 'teal']

def test_6():
    assert colors_args('red', 'white', link_color = 'orange', visited_color = 'blue') == ['red', 'white', 'orange', 'blue']
