#!/usr/bin/env python

import pytest

from circle import *
from math import pi


def test_circle():
    """ Test basic circle intialization"""
    c = Circle(4)
    assert c.radius == 4
    assert c.diameter == 8


def test_circle_diameter_change():
    """Test changing the diameter of circle, updates the radius"""
    c = Circle(4)
    c.diameter = 2

    assert c.radius == 1


def test_circle_area():
    """Test the area calculation of circle"""
    c = Circle(2)
    assert c.area == 4 * pi


def test_circle_area_set():
    """Test that the user cannot set the area of a circle object"""
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 42


def test_circle_from_diameter():
    """Test from_diameter method to create a circle object"""
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


def test_circle_str():
    """Test the circle __str__ method"""
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4.000000'


def test_circle_repr():
    """Test the circle __repr__ method"""
    c = Circle(4)
    assert repr(c) == 'Circle(4)'


def test_add_circle():
    """Test adding a of circle objects"""
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert c3.radius == 6
    # Adding another number
    c4 = c1 + 3
    assert c4.radius == 5
    # Reversing the order
    c5 = 1 + c1
    assert c5.radius == 3
    # adding an non-numeric
    with pytest.raises(TypeError):
        c6 = c1 + '10'


def test_multiple_circle():
    """Test mulitplying of circle objects"""
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 * c2
    assert c3.radius == 8
    # Adding another number
    c4 = c1 * 3
    assert c4.radius == 6
    # Reversing the order
    c5 = 3 * c1
    assert c5.radius == 6
    # adding an non-numeric
    with pytest.raises(TypeError):
        c6 = c1 * '10'


def test_compare_circles():
    """Test the comparison of two circles"""
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)

    assert not c1 > c2
    assert c1 < c2
    assert not c1 == c2
    assert c3 == c2

def test_sort_circles():
    """Test the comparison of two circles"""
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(6)

    l = [c3, c1, c2]
    l.sort()

    assert l == [c1, c2, c3]

def test_subtracting_circle():
    """Test subtracting of circle objects"""
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c2 - c1
    assert c3.radius == 2
    # subtracting another number
    c4 = c2 - 2
    assert c4.radius == 2
    # Reversing the order
    with pytest.raises(TypeError):
        c5 = 6 - c1
    # adding an non-numeric
    with pytest.raises(TypeError):
        c6 = c1 - '10'
    # result is negative number
    with pytest.raises(ValueError):
        c7 = c1 - 3


def test_pow_circle():
    """Test power of circle objects"""
    c1 = Circle(2)
    c2 = c1 ** 3
    assert c2.radius == 8

    c3 = Circle(4)
    c4 = c3 ** c1
    assert c4.radius == 16

def test_augmented_assignment():
    """Test that augmented assignment methods"""
    c = Circle(2)
    c += 4
    assert c.radius == 6

    c *= 2
    assert c.radius == 12

    c **= 2
    assert c.radius == 144

    c -= 6
    assert c.radius == 138

def test_sphere():
    """ Test basic of sphere"""
    s = Sphere(4)
    assert s.radius == 4
    assert s.diameter == 8
    assert s.area == 4 * pi * 16
    assert s.volume == 4/3 * pi * 64
    assert str(s) == 'Sphere with radius: 4.000000'
    assert repr(s) == 'Sphere(4)'