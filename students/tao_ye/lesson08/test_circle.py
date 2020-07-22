"""
test code for circle.py
"""

import io
import pytest

from circle import *


def test_init():
    """
    Test class instantiation, and the attribute "radius"
    """
    c = Circle(4)
    assert c.radius == 4


def test_diameter_property():
    c = Circle(4)
    assert c.diameter == 8

    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1


def test_area():
    c = Circle(2)
    assert round(c.area, 6) == 12.566371


def test_diameter_constructor():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


def test_str_repr():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'

    d = eval(repr(c))
    assert isinstance(d, Circle) is True


def test_add_mul_operators():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1+c2

    # __mul__ and __rmul__
    c4 = c2*3
    c5 = 3*c2

    assert isinstance(c3, Circle) is True
    assert c3.radius == 6

    assert isinstance(c4, Circle) is True
    assert c4.radius == 12

    assert isinstance(c5, Circle) is True
    assert c5.radius == 12


def test_comparison_operators():
    c1 = Circle(2)
    c2 = Circle(4)

    assert (c1 > c2) is False
    assert (c1 < c2) is True
    assert (c1 == c2) is False

    c3 = Circle(4)
    assert (c2 == c3) is True


def test_sorting():
    Circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
               Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    Circles.sort(key=Circle.sort_key)

    for i in range(10):
        assert Circles[i] == Circle(i)


def test_sphere_class():
    s1 = Sphere(2)
    assert s1.radius == 2
    assert repr(s1) == 'Sphere(2)'

    assert round(s1.area, 6) == 50.265482
    assert round(s1.volume, 6) == 33.510322

    s2 = Sphere.from_diameter(8)
    assert isinstance(s2, Sphere) is True
    assert s2.diameter == 8
    assert s2.radius == 4

    assert (s1 > s2) is False
