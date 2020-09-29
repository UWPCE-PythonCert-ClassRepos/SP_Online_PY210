#!/usr/bin/env python3

# Russell Felts
# Assignment 8 - Circle Class Unit Tests


import pytest
import math

from circle_class import Circle
from circle_class import Sphere


def test_init_circle():
    """ Test that a circle can be initialized """
    circle = Circle(7)
    assert circle.radius == 7


def test_get_circle_diameter():
    """ Test getting the diameter property """
    circle = Circle(5)
    assert circle.diameter == 5 * 2


def test_set_circle_diameter():
    """ Test the diameter can be set and it updates the radius """
    circle = Circle(2)
    assert circle.radius == 2
    assert circle.diameter == 2 * 2

    circle.diameter = 5
    assert circle.diameter == 5
    assert circle.diameter == circle.radius * 2


def test_get_circle_area():
    """ Test getting the area """
    circle = Circle(6)
    assert circle.area == math.pi * 6 ** 2


def test_set_circle_area():
    """ Verify the area can not be set """
    circle = Circle(3)
    with pytest.raises(AttributeError):
        circle.area = 4


def test_creation_circle_diameter():
    """ Test a Circle can be created using the diameter property """
    circle = Circle.from_diameter(6)
    assert circle.radius == 3


def test_circle_str():
    """ Verify the string printed is correct """
    circle = Circle(8)
    assert str(circle) == "Circle with radius: 8"


def test_circle_repr():
    """ Verify the output from repr is the expected value """
    circle = Circle(2)
    assert repr(circle) == "Circle(2)"


def test_circle_add():
    """ Test adding two circles together """
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = c1 + c2
    assert c3.radius == 5


def test_circle_multiply():
    """ Test a circle can be multiplied by a number """
    c1 = Circle(2)
    c2 = c1 * 2
    assert c2.radius == 4

    c3 = 2 * c1
    assert c3.radius == 4


def test_circle_comparison():
    """ Test greater than, less than, equals """
    c1 = Circle(2)
    c2 = Circle(3)
    assert c2 > c1
    assert c1 < c2
    assert (c1 > c2) is False
    assert c1 < Circle(4)
    assert Circle(5) > Circle(1)
    assert Circle(3) == c2
    assert Circle(5) != c2
    assert (Circle(5) == c2) is False


def test_circle_sort():
    circle_list = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9),
                   Circle(1)]
    print(circle_list)
    circle_list.sort()
    assert circle_list == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7),
                           Circle(8), Circle(9)]


def test_sphere_init():
    """ Test that a sphere can be initialized """
    sphere = Sphere(2)
    assert sphere.radius == 2
    assert sphere.diameter == 2 * 2


def test_sphere_str():
    """ Verify the string printed is correct """
    sphere = Sphere(8)
    assert str(sphere) == "Sphere with radius: 8"


def test_sphere_repr():
    """ Verify the output from repr is the expected value """
    sphere = Sphere(2)
    assert repr(sphere) == "Sphere(2)"


def test_get_sphere_area():
    """ Test getting the area """
    sphere = Sphere(6)
    assert sphere.area == 4 * math.pi * 6 ** 2


def test_set_sphere_area():
    """ Verify the area can not be set """
    sphere = Sphere(3)
    with pytest.raises(AttributeError):
        sphere.area = 4


def test_get_sphere_volume():
    """ Test getting the area """
    sphere = Sphere(6)
    assert sphere.volume == (4/30) * math.pi * 6 ** 3


def test_set_sphere_volume():
    """ Verify the area can not be set """
    sphere = Sphere(3)
    with pytest.raises(AttributeError):
        sphere.volume = 4


def test_creation_sphere_diameter():
    """ Test a Sphere can be created using the diameter property """
    sphere = Sphere.from_diameter(6)
    assert str(sphere) == "Sphere with radius: 3.0"
    assert sphere.radius == 3
    assert sphere.diameter == 6
    assert sphere.volume == (4/30) * math.pi * 3 ** 3
    assert sphere.area == 4 * math.pi * 3 ** 2
