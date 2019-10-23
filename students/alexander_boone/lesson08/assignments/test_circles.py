#!/usr/bin/env python

import pytest
from circles import Circle, Sphere
import math


def test_radius():

    c = Circle(5)
    assert c.radius == 5


def test_diameter():

    c = Circle(5)
    assert c.diameter == 10


def test_diameter_setter():

    c = Circle(5)
    c.diameter = 20
    assert c.radius == 10
    assert c.diameter == 20


def test_area_getter():

    c = Circle(5)
    assert c.area == math.pi * (c.radius ** 2)


def test_circle_from_diameter():

    c = Circle.from_diameter(10)
    assert c.radius == 5
    assert c.diameter == 10


def test_print():

    c = Circle(4)
    print_output = str(c)
    assert print_output.startswith('Circle with radius:') is True
    assert "4" in print_output


def test_numerical_protocol():

    c1 = Circle(2)
    c2 = Circle(6)
    assert print(c1 + c2) == print(Circle(8))
    assert print(c2 * 3) == print(Circle(18))
    assert print(3 * c2) == print(Circle(18))


def test_comparisons():

    c1 = Circle(2)
    c2 = Circle(6)

    assert (c1 < c2) is True
    assert (c1 <= c2) is True
    assert (c1 == c2) is False
    assert (c1 != c2) is True
    assert (c1 > c2) is False
    assert (c1 >= c2) is False


def test_sorting():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
               Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]

    circles.sort()

    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3),
                       Circle(4), Circle(5), Circle(6), Circle(7),
                       Circle(8), Circle(9)]


def test_augmented():
    c1 = Circle(2)
    c1 += 5

    assert print(c1) == print(Circle(7))

    c1 += Circle(12)

    assert print(c1) == print(Circle(19))


def test_sphere_creation():

    s1 = Sphere(4)
    assert s1.radius == 4
    assert s1.diameter == 8
    assert s1.volume == (4/3) * math.pi * (4**3)

    s2 = Sphere.from_diameter(8)
    assert s2.radius == 4
    assert s2.diameter == 8
    assert s2.volume == (4/3) * math.pi * (4**3)


def test_sphere_print():
    s1 = Sphere(4)
    print_output = str(s1)
    assert print_output.startswith('Sphere with radius:') is True
    assert "4" in print_output


def test_sphere_area_call():
    s1 = Sphere(4)
    with pytest.raises(NotImplementedError):
        s1.area
