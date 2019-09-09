#!/usr/bin/env python3

from args_lab import colors, colors2


def test1():
    assert colors() == 'red black blue purple'


def test2():
    color = colors('red', 'blue', 'yellow', 'chartreuse')
    assert color == 'red blue yellow chartreuse'


def test3():
    color = colors(link_color='red', back_color='blue')
    assert color == 'red blue red purple'


def test4():
    color = colors('purple', link_color='red', back_color='blue')
    assert color == 'purple blue red purple'


def test5():
    some_tuple = ('purple', 'burgundy', 'orange')
    assert colors(*some_tuple) == 'purple burgundy orange purple'


def test6():
    some_kwargs = {'visited_color': 'orange', 'back_color': 'rainbow'}
    assert colors(**some_kwargs) == 'red rainbow blue orange'


def test7():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert colors(*regular, **links) == 'red blue chartreuse purple'


def test8():
    test = colors2('crazy', 'tackle', colors='purple')
    assert test == 'crazy tackle purple'

def test9():
    test = colors2('crazy', 'tackle', 'oregon', 'ducks')
    assert test == 'crazy tackle oregon ducks'


def test10():
    last_test = colors2(fifty_cent='beige', tupac='green',
                        happy='yellow', crazy_taxi='purple', elf='black',
                        cindy='tan')
    assert last_test == 'beige green yellow purple black tan'
