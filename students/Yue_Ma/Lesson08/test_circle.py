#!/usr/bin/env python3
import math
import pytest
from circle import *
import unittest


def test_radius():
    test = Circle(4)
    assert test.radius == 4


def test_diameter():
    test = Circle(4)
    assert test.diameter == 8


def test_set_diameter():
    test = Circle(4)
    test.diameter = 2
    assert test.radius == 1
    assert test.diameter == 2


def test_area():
    test = Circle(2)
    test1 = Sphere(2)
    assert test.area == 4 * math.pi
    assert test1.area == 4 * math.pi * 4


def from_diameter():
    test = Circle.from_diameter(8)
    test1 = Sphere.from_diameter(8)
    assert test.diameter == 8
    assert test.radius == 4
    assert test1.diameter == 8
    assert test1.radius == 4


def test__str__():
    test = Circle(4)
    test1 = Sphere(4)
    assert str(test) == 'Circle with radius: 4'
    assert str(test1) == 'Sphere with radius: 4'


def test__repr__():
    test = Circle(4)
    test1 = Sphere(4)
    assert repr(test) == 'Circle(4)'
    assert eval(repr(test)) == Circle(4)
    assert repr(test1) == 'Sphere(4)'
    assert eval(repr(test1)) == Sphere(4)


def test_numeric_protocol():
    test1 = Circle(2)
    test2 = Circle(4)
    print(test1 + test2)
    print(Circle(6))
    assert test1 + test2 == Circle(6)
    assert test2 * 3 == Circle(12)


def test_compare():
    test1 = Circle(2)
    test2 = Circle(3)
    test3 = Circle(3)

    assert (test1 == test2) is False
    assert (test2 == test3) is True
    assert (test1 > test2) is False
    assert (test1 < test2) is True
    assert (test1 != test2) is True
    assert (test1 >= test2) is False
    assert (test1 <= test2) is True
    Circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
               Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    Circles.sort()
    assert Circles == [Circle(0), Circle(1), Circle(2), Circle(3),
                       Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]


def test_volume():
    test = Sphere(2)
    assert test.volume == 2 ** 3 * math.pi * 4 / 3
