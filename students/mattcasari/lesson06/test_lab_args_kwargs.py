#!/usr/bin/env python

from lab_args_kwargs import page_color, new_func


def test_1():
    assert page_color() == {
        "fore_color": "blue",
        "back_color": "red",
        "link_color": "purple",
        "visited_color": "green",
    }


def test_2():
    assert page_color(fore_color="yellow") == {
        "fore_color": "yellow",
        "back_color": "red",
        "link_color": "purple",
        "visited_color": "green",
    }


def test_3():
    assert page_color(back_color="orange") == {
        "fore_color": "blue",
        "back_color": "orange",
        "link_color": "purple",
        "visited_color": "green",
    }


def test_4():
    assert page_color(
        fore_color="yellow", back_color="orange", link_color="tan", visited_color="blue"
    ) == {
        "fore_color": "yellow",
        "back_color": "orange",
        "link_color": "tan",
        "visited_color": "blue",
    }


def test_5():
    assert page_color("red", "orange", "yellow", "green") == {
        "fore_color": "red",
        "back_color": "orange",
        "link_color": "yellow",
        "visited_color": "green",
    }

def test_6():
    assert page_color("purple", link_color="red", back_color="blue") == {
        "fore_color": "purple",
        "back_color": "blue",
        "link_color": "red",
        "visited_color": "green",
    }

def test_7():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert page_color(*regular, **links) == {
        "fore_color": "red",
        "back_color": "blue",
        "link_color": "chartreuse",
        "visited_color": "green",
    }

def test_8():
    
    assert new_func() == {
        "fore_color": "blue",
        "back_color": "red",
        "link_color": "purple",
        "visited_color": "green",
    }

def test_9():
    assert new_func('red', 'blue') == {
        "fore_color": "red",
        "back_color": "blue",
        "link_color": "purple",
        "visited_color": "green",
    }

def test_10():
    assert new_func(fore_color='yellow') == {
        "fore_color": "yellow",
        "back_color": "red",
        "link_color": "purple",
        "visited_color": "green",
    }