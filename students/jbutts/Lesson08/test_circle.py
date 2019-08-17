#!/usr/bin/env python3

"""
Test for a class-based circle/sphere maker
"""

from circle import *


def test_str_dunder():
    c = Circle(9.99)
    assert c.__str__() == "Circle with a radius of: 9.99"


def test_repr_dunder():
    c = Circle(9.99)
    assert c.__repr__() == "Circle(9.99)"


def test_area():
    c = Circle(4)
    assert '{0:.2f}'.format(c.area) == '50.27'


def test_radius():
    #  Test radius property and setter
    c = Circle(5.32)
    assert c.radius == 5.32
    c.radius = 5.33
    assert c.radius == 5.33


def test_mult():
    #  Test multiplication dunder
    c1 = Circle(7)
    c2 = Circle(4)
    c3 = c1 * c2
    assert c3.radius == 28


def test_gt():
    #  Greater than
    c1 = Circle(7)
    c2 = Circle(4)
    c3 = Circle(1)
    assert c1 > c2
    assert not c2 < c3


def test_gteq():
    c1 = Circle(7)
    c2 = Circle(4)
    c3 = Circle(4)
    assert c1 >= c2
    assert c2 >= c3
    assert not c2 >= c1


def test_eq():
    c1 = Circle(7)
    c2 = Circle(4)
    c3 = Circle(4)
    assert c2 == c3
    assert not c2 == c1


def test_lt():
    c1 = Circle(7)
    c2 = Circle(4)
    c3 = Circle(4)
    assert not c1 < c2
    assert c2 < c1
    assert not c2 < c3


def test_lteq():
    c1 = Circle(7)
    c2 = Circle(4)
    c3 = Circle(4)
    assert not c1 <= c2
    assert c2 <= c3


def test_truediv():
    c1 = Circle(8)
    c2 = Circle(4)
    c3 = c1/c2
    assert c3.radius == 2


def test_sphere_volume():
    #  Area == 4 * pi * s1._radius ** 2
    s1 = Sphere(9)
    assert '{0:.2f}'.format(s1.volume) == '3053.63'


def test_sphere_area():
    #  Volume == (4/3) * pi * s1._radius ** 3
    s1 = Sphere(9)
    assert '{0:.2f}'.format(s1.area) == '1017.88'

