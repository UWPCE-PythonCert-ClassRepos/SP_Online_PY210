#!/usr/bin/env python3
"""
test code for ultimate_circle.py

"""

import pytest
from ultimate_circle import *

def test_init_circle():
    c = Circle(7)
    assert c.radius == 7


def test_init_no_radius():
    with pytest.raises(TypeError):
        c = Circle()


def test_diameter():
    c = Circle(7)
    assert c.diameter  == 14


def test_set_diameter():
    c =Circle(7)
    c.diameter = 20
    assert c.diameter == 20
    assert c.radius == 10


def test_area():
    c =Circle(7)
    with pytest.raises(AttributeError):
        c.area = 34
    assert round(c.area, 2)== 153.94

def test_from_diameter():
    c = Circle.from_diameter(30)


def test_print_string():
    c =Circle(7)
    d = eval(repr(c))
    assert 'Circle(7)' == d

def test_add_circle():
    c = Circle(7)
    c2 = Circle(7)
    csum = c + c2
    assert csum.radius == 14

def test_mulitply_circle():
    c = Circle(7)
    c2 = Circle(7)
    cvalue = c * c2
    c2value = 2 * c2
    assert c2value.radius == 14
    assert cvalue.radius == 49









