#!/usr/bin/env python

import pytest
from Circle_Class import *
from math import *

def test_radius():
    c = Circle(4)
    assert c.radius == 4


def test_diameter():
    c = Circle(3)
    assert c.diameter == 6


def test_set_diameter():
    c = Circle(8)
    assert c.diameter == 16
    assert c.radius == 8
    c.diameter = 5
    assert c.diameter == 5
    assert c.radius == 2.5


def test_area():
    c = Circle(2.7)
    assert c.area == pi * 2.7**2


def test_alt_constructor():
    c = Circle.from_diameter(9)
    assert c.diameter == 9
    assert c.radius == 4.5


def test_print_str(capsys):
    c = Circle(4)
    print(c)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == 'Circle with radius: 4.000000\n'


def test_repr_c():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'


def test_add():
    c1 = Circle(2)
    c2 = Circle(9)
    assert c1 + c2 == Circle(11)


def test_mult():
    c1 = Circle(2)
    assert c1 * 7 == Circle(14)
    assert 3 * c1 == Circle(6)


def test_lt():
    c1 = Circle(2)
    c2 = Circle(3)
    assert c1 < c2


def test_gt():
    c1 = Circle(4)
    c2 = Circle(3)
    assert c1 > c2


def test_eq():
    c2 = Circle(3)
    c3 = Circle(3)
    assert c2 == c3


def test_ne():
    c2 = Circle(3)
    c3 = Circle(4)
    assert c2 != c3


def test_sort(capsys):
    c1 = Circle(8)
    c2 = Circle(1)
    c3 = Circle(3)
    c4 = Circle(0)
    c5 = Circle(4)
    circles = [c1, c2, c3, c4, c5]
    circles.sort()
    print(circles)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == '[Circle(0), Circle(1), Circle(3), Circle(4), Circle(8)]\n'


def test_plus_up():
    c1 = Circle(2)
    c2 = Circle(3)
    c1 += c2
    assert c1 == Circle(5)


def test_mult_up():
    c1 = Circle(5)
    c1 *= 6
    assert c1 == Circle(30)


def test_sphere_str(capsys):
    s = Sphere(4)
    print(s)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == 'Sphere with radius: 4.000000\n'


def test_repr_s():
    s = Sphere(4)
    assert repr(s) == 'Sphere(4)'


def test_volume():
    s = Sphere(2.7)
    assert s.volume == (4 / 3) * pi * 2.7**3


def test_sphere_area():
    s = Sphere(2.7)
    assert s.area == 4 * pi * 2.7**2


def test_sphere_alt_constructor():
    s = Sphere.from_diameter(9)
    assert s.diameter == 9
    assert s.radius == 4.5