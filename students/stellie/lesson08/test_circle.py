#!/usr/bin/env python3

import pytest
from circle import *

"""
Test code for circle.py
"""


def test_radius():
    c = Circle(3)
    assert c.radius == 3


def test_diameter():
    c = Circle(3)
    assert c.diameter == 6


def test_diameter_setter():
    c = Circle(3)
    print('Old diameter: {:.2f}'.format(round(c.diameter, 2)))
    c.diameter = 4
    print('New diameter: {:.2f}'.format(round(c.diameter, 2)))
    print('New radius: {:.2f}'.format(round(c.radius, 2)))


def test_area():
    c = Circle(3)
    expected = math.pi * 3 ** 2
    print(expected)
    assert c.area == expected


def test_area_setter():
    c = Circle(3)
    with pytest.raises(AttributeError):
        c.area = 30


def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.radius == 4
    assert c.diameter == 8
    assert c.area == math.pi * 4 ** 2

