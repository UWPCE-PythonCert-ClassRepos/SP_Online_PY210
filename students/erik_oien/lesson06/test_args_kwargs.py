#!/usr/bin/env python3

from args_kwargs_lab import color_fun

def test1():
    assert color_fun("red", "blue", "yellow", "chartreuse") == ("red", "blue", "yellow", "chartreuse")

def test2():
    assert color_fun(fore_color="red", back_color="blue", link_color="yellow", visited_color="chartreuse") == ("red", "blue", "yellow", "chartreuse")

def test3():
    assert color_fun("purple", link_color="red", back_color="blue") == ("purple", "blue", "red", "orange")

def test4():
    regular = ("red", "blue")
    links = {"link_color": "chartreuse"}
    assert color_fun(*regular, **links) == ("red", "blue", "chartreuse", "orange")

