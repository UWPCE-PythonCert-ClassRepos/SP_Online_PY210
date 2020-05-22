#!/usr/bin/env python3

import pytest
from circle import *

"""
Test code for circle.py
"""


def test_radius():  # test correct output for radius
    c = Circle(3)
    assert c.radius == 3


def test_diameter():  # test correct output for diameter
    c = Circle(3)
    assert c.diameter == 6


def test_diameter_setter():  # test correct output for radius with new diameter
    c = Circle(3)
    print(f'Old diameter: {c.diameter:.2f}')
    c.diameter = 4
    print(f'New diameter: {c.diameter:.2f}')
    print(f'New radius: {c.radius:.2f}')
    assert c.radius == 2.00


def test_area():  # test correct output for area
    c = Circle(3)
    expected = math.pi * 3 ** 2
    print(expected)
    assert c.area == expected


def test_area_setter():  # assert you cannot set area for circle
    c = Circle(3)
    with pytest.raises(AttributeError):
        c.area = 30


def test_from_diameter():  # test for area given new diameter
    c = Circle.from_diameter(8)
    assert c.radius == 4
    assert c.diameter == 8
    assert c.area == math.pi * 4 ** 2


def test_str():  # test for correct string output
    c = Circle(3)
    assert str(c) == 'Circle with radius: 3.00'


def test_repr():
    c = Circle(3)
    assert repr(c) == 'Circle(3)'


# Test circle numerics
def test_add():
    c1 = Circle(3)
    c2 = Circle(4)
    assert repr(c1 + c2) == 'Circle(7)'
    assert (c1 + c2).radius == 7

    # a_circle += another_circle
    # a_circle *= 2


def test_sub():
    c1 = Circle(3)
    c2 = Circle(4)
    assert repr(c2 - c1) == 'Circle(1)'
    assert (c2 - c1).radius == 1


def test_mul():
    c1 = Circle(3)
    c2 = Circle(4)
    c3 = 6
    assert repr(c1 * c2) == 'Circle(12)'
    assert repr(c1 * c3) == 'Circle(18)'
    assert (c1 * c2).radius == 12
    assert c1.radius * c3 == 18
    assert c3 * c2.radius == 24  # test reflected numerics output correctly


# Test circle comparison operators
def test_comparisons():
    c1 = Circle(3)
    c2 = Circle(4)
    c3 = Circle(3)
    assert (c1 < c2) is True
    assert (c2 <= c1) is False
    assert (c1 == c3) is True
    assert (c2 >= c3) is True
    assert (c3 > c2) is False
    assert (c1 != c2) is True


# Test sorting for a list of circles
def test_circle_sort():
    circles = Circle.circle_list(Circle(3), Circle(4), Circle(2),
                                 Circle(5), Circle(1))
    assert sorted(circles) == [Circle(1), Circle(2), Circle(3),
                               Circle(4), Circle(5)]


# Test correct output for sphere dimensions
def test_sphere_properties():
    s = Sphere(4)
    assert s.radius == 4  # test radius
    assert s.diameter == 8  # test diameter

    print(f'Old diameter: {s.diameter:.2f}')
    s.diameter = 12
    print(f'New diameter: {s.diameter:.2f}')
    print(f'New radius: {s.radius:.2f}')
    assert s.radius == 6.00  # test for new radius value given new diameter

    expected = 4 * math.pi * 6 ** 2  # test surface area of sphere
    print(expected)
    assert s.area == expected

    s = Sphere.from_diameter(8)  # test for new surface area given new diameter
    assert s.radius == 4
    assert s.diameter == 8
    assert s.area == 4 * math.pi * 4 ** 2


# Test string outputs with sphere dimensions
def test_sphere_output():
    s = Sphere(4)
    assert str(s) == 'Sphere with radius: 4.00'
    assert repr(s) == 'Sphere(4)'


# Test sphere numerics
def test_sphere_numerics():
    s1 = Sphere(4)
    s2 = Sphere(6)
    s3 = 8
    assert repr(s1 + s2) == 'Sphere(10)'
    assert (s1 + s2).radius == 10  # add two spheres together
    assert repr(s1 * s2) == 'Sphere(24)'
    assert repr(s1 * s3) == 'Sphere(32)'
    assert (s1 * s2).radius == 24  # multiply two spheres together
    assert s1.radius * s3 == 32
    assert s3 * s2.radius == 48  # test reflected numerics output correctly


# Test sorting for a list of spheres
def test_sphere_sort():
    spheres = Sphere.sphere_list(Sphere(3), Sphere(1), Sphere(2))
    assert sorted(spheres) == [Sphere(1), Sphere(2), Sphere(3)]
