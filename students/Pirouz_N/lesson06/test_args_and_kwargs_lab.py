#!/usr/bin/env python

"""
test code for args and kwargs example.

"""


# you can change this import to test different versions
from args_and_kwargs_lab import func, func2, func3, func4
# from walnut_party import walnut_party2 as walnut_party
# from walnut_party import walnut_party3 as walnut_party


def test_1():
    assert func('red', 'blue', 'yellow', 'chartreuse')\
           == "fore_color is red back_color is blue link_color is yellow visited_color is chartreuse"


def test_2():
    assert func(link_color='red', back_color='blue') \
           == "fore_color is black back_color is blue link_color is red visited_color is black"


def test_3():
    assert func('purple', link_color='red', back_color='blue') \
           == "fore_color is purple back_color is blue link_color is red visited_color is black"


def test_4():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert func(*regular, **links)\
           == "fore_color is red back_color is blue link_color is chartreuse visited_color is black"


def test_5():
    regular = ('red', 'blue', 'yellow', 'brown')
    assert func2(*regular)\
           == "fore_color is red back_color is blue link_color is yellow visited_color is brown"


def test_6():
    regular = ['red', 'blue', 'yellow', 'brown']
    assert func2(*regular)\
           == "fore_color is red back_color is blue link_color is yellow visited_color is brown"


def test_7():
    regular = {'fore_color': 'red', 'back_color': 'blue', 'link_color': 'yellow', 'visited_color': 'brown'}
    assert func3(**regular)\
           == "fore_color is red back_color is blue link_color is yellow visited_color is brown"


def test_8():
    one_and_two = ('red', 'blue')
    three_and_four = {'link_color': 'yellow', 'visited_color': 'brown'}
    assert func4(*one_and_two, **three_and_four)\
           == "fore_color is red back_color is blue link_color is yellow visited_color is brown"


def test_9():
    one_and_two = ('red', 'blue', 'grey')
    three_and_four = {'link_color': 'yellow', 'visited_color': 'brown'}
    assert func4(*one_and_two, **three_and_four)\
           == "fore_color is red back_color is blue link_color is yellow visited_color is brown"


def test_10():
    one_and_two = ('red', 'blue', 'grey')
    three_and_four = {'link_color': 'yellow', 'visited_color': 'brown',
                      'useless_color': 'cyan', 'visited_color': 'orange'}
    assert func4(*one_and_two, **three_and_four)\
           == "fore_color is red back_color is blue link_color is yellow visited_color is orange"
