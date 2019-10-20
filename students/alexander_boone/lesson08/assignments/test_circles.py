#!/usr/bin/env python

import pytest
from circles import Circle
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