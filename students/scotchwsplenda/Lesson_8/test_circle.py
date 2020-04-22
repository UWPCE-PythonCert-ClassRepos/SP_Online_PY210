#!/usr/bin/env python

import pytest
from circle import Circle, Sphere
import math


# step 1
def test_radius():
    c = Circle(5)
    assert c.radius == 5


# step 2
def test_diameter():
    c = Circle(5)
    assert c.diameter == 10


# step 3
def test_diameter_setter():
    c = Circle(5)
    c.diameter = 40
    assert c.radius == 20
    assert c.diameter == 40


# step 4
def test_area():
    c = Circle(8)
    assert c.area == math.pi * (c.radius ** 2)


# step 5
def test_from_diameter():
    c = Circle.from_diameter(10)
    assert c.radius == 5
    assert c.diameter == 10


# step 6
def test_str():
    c = Circle(4)
    print_output = str(c)
    assert print_output.startswith('Circle with radius:') is True


# step 7
def test_numerical_protocol():
    c1 = Circle(2)
    c2 = Circle(6)
    assert print(c1 + c2) == print(Circle(8))
    assert print(c2 * 3) == print(Circle(18))


# step 8
def test_comps():
    c1 = Circle(2)
    c2 = Circle(6)
    assert (c1 < c2) is True
    assert (c1 == c2) is False
    assert (c1 != c2) is True
    assert (c1 > c2) is False


def test_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
               Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]

    circles.sort()

    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3),
                       Circle(4), Circle(5), Circle(6), Circle(7),
                       Circle(8), Circle(9)]


# step 9
def test_sphere():
    s = Sphere(5)
    assert s.radius == 5
    assert s.diameter == 10
    assert s.volume == (4/3) * math.pi * (5**3)
