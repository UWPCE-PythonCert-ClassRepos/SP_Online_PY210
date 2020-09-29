#!/usr/bin/env python3

# Unit tests for Circle class
from circle import *
import math
import pytest


def test_radius():

    c_1 = Circle(4)
    c_2 = Circle(5)

    assert c_1.radius == 4
    assert c_2.radius == 5


def test_diameter():

    c_1 = Circle(4)
    c_2 = Circle(5)

    assert c_1.diameter == 8
    assert c_2.diameter == 10

    # Make sure setter for diameter works
    c_3 = Circle(2)
    c_3.diameter = 10

    assert c_3.diameter == 10
    assert c_3.radius == 5

    c_4 = Circle.from_diameter(8)
    c_5 = Circle.from_diameter(10)

    assert c_4.diameter == 8
    assert c_4.radius == 4
    assert c_5.diameter == 10
    assert c_5.radius == 5


def test_area():

    c_1 = Circle(4)
    c_2 = Circle(5)

    assert c_1.area == 4 ** 2 * pi
    assert c_2.area == 5 ** 2 * pi


def test_str():

    c_1 = Circle(3)
    assert c_1.__str__() == 'Circle with a radius of 3'

    c_2 = Circle(4)
    assert c_2.__str__() == 'Circle with a radius of 4'


def test_repr():

    c_1 = Circle(3)
    c_2 = Circle(4)

    assert c_1.__repr__() == 'Circle(3)'
    assert c_2.__repr__() == 'Circle(4)'


def test_add():

    c_1 = Circle(3)
    c_2 = Circle(4)

    assert print(c_1 + c_2) == print(Circle(7))


def test_sub():

    c_1 = Circle(3)
    c_2 = Circle(5)

    assert print(c_2 - c_1) == print(Circle(2))


def test_mul():

    c_1 = Circle(3)
    c_2 = Circle(4)

    assert print(c_1 * c_2) == print(Circle(12))


def test_compare():

    c_1 = Circle(3)
    c_2 = Circle(4)
    c_3 = Circle(4)
    c_4 = Circle(5)

    assert (c_1 < c_2) is True
    assert (c_2 != c_4) is True
    assert (c_4 > c_1) is True

    circles = [c_4, c_1, c_2]
    circles.sort()
    
    assert circles == [Circle(3), Circle(4), Circle(5)]


# Test for Spheres
def test_sphere_radius():

    s_1 = Sphere(3)
    s_2 = Sphere(4)

    assert s_1.radius == 3
    assert s_2.radius == 4


def test_sphere_diameter():

    s_1 = Sphere(3)
    s_2 = Sphere(4)

    assert s_1.diameter == 6
    assert s_2.diameter == 8

    # Make sure diameter setter works

    s_1.diameter = 10
    assert s_1 == Sphere(5)


def test_sphere_area():

    s_1 = Sphere(3)

    with pytest.raises(NotImplementedError):
        s_1.area