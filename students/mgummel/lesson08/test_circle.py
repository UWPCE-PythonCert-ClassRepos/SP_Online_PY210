#!/usr/bin/env python3
import pytest

from circle import *
from math import pi


def test_init():
    c = Circle(12)


def test_radius():
    c = Circle(23)
    d = Circle(3)

    assert c.radius == 23
    assert d.radius == 3

    c.radius = 11

    assert c.radius == 11
    assert d.radius == 3

    d.radius = 50
    assert d.radius == 50


def test_diameter():
    c1 = Circle(10)
    c2 = Circle(4)

    assert c1.diameter == 20
    assert c2.diameter == 8

    c2.radius = 12
    c1.radius = 180
    assert c2.diameter == 24
    assert c1.diameter == 360


def test_set_diameter():
    d1 = Circle(3)
    d2 = Circle(10)

    d1.diameter = 12
    assert d1.diameter == 12
    assert d1.radius == 6

    d2.diameter = 3
    assert d2.diameter == 3
    assert d2.radius == 1.5


def test_area():
    c1 = Circle(1)
    assert round(c1.area, 5) == 3.14159

    c2 = Circle(7)
    assert round(c2.area, 5) == 153.93804


def test_from_diameter():
    d1 = Circle.from_diameter(10)
    d2 = Circle.from_diameter(300)

    assert d1.diameter == 10
    assert d1.radius == 5
    assert d2.diameter == 300
    assert d2.radius == 150


def test__str__():
    c2 = Circle(10)
    assert repr(c2) == "Circle(10)"
    assert c2.__str__() == "Circle with radius: 10.00000"


def test_add():
    c1 = Circle(12)
    c2 = Circle(4)
    c3 = Circle.from_diameter(10)
    c4 = c2 + c1
    c5 = c1 + c2 + c3
    assert repr(c4) == "Circle(16)"
    assert repr(c3 + c2) == "Circle(9)"
    assert repr(c5) == "Circle(21)"

    assert c4.radius == 16
    assert c4.area == pi * 16 ** 2
    assert c4.diameter == 32

    assert c5.radius == 21
    assert c5.area == pi * 21 ** 2
    assert c5.diameter == 42


def test_mul():
    c1 = Circle(7)
    d1 = Circle.from_diameter(4)

    assert repr(d1 * 2) == "Circle(4)"
    assert repr(3 * c1) == "Circle(21)"
    assert c1 * 3 == 3 * c1
    assert d1 * 4 == 4 * d1


def test_lt():
    c1 = Circle(4)
    c2 = Circle(7)
    c3 = Circle(10)
    c4 = Circle(4)

    assert (c2 < c1) == False
    assert (c2 < c3) == True
    assert (c1 > c3) == False
    assert (c1 == c4) == True


def test_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(
        0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]

    sorted_circles = [Circle(0), Circle(1), Circle(2), Circle(3), Circle(
        4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
    circles.sort()

    assert circles == sorted_circles


def test_iadd():
    c1 = Circle(14)
    c2 = Circle(3)
    c3 = Circle.from_diameter(20)

    c1 += c2
    c2 += c3
    assert c1.radius == 17
    assert c2.radius == 13
    
    c1 = Circle(14)
    c1 += c3
    assert c1.radius == 24

    c2 += c2
    assert c2.radius == 26

    c4 = Circle(4)
    c2 += c4
    assert c2.radius == 30


def test_imul():
    c1 = Circle(5)
    c2 = Circle(8)

    c1 *= 4
    c2 *= 1
    assert c1.radius == 20
    assert c2.radius == 8

    c2 *= 7
    assert c2.radius == 56


def test_sphere():
    s1 = Sphere(3)
    s2 = Sphere(4)
    
    assert s1.area == 4 * pi * 3 ** 2