#!/usr/bin/env python3

import pytest
from circle import *

"""
Unit tests for Circle.py
"""

def test_instantiate_circle():
    # test if you can create circle and it saves radius
    circ = Circle(5)
    assert circ.radius == 5

def test_diameter():
    # test you can access diameter and is set correctly
    c = Circle(2)
    assert c.diameter == 4

def test_change_r_d():
    # test if you can change the circle properties
    c = Circle(5)
    c.radius = 10
    print(c.diameter)
    assert c.diameter == 20
    c.diameter = 30
    print(c.radius)
    assert c.radius == 15.0

def test_area():
    """
    test if area is set properly, and test if AttributeError raised when trying
    to set area directly
    """
    c = Circle(5)
    print(c.area)
    assert math.isclose(78.5398, c.area, abs_tol=0.0001)
    with pytest.raises(AttributeError):
        c.area = 100

def test_dia_alternate_constructor():
    c = Circle.from_diameter(10)
    print(c.radius)
    assert c.radius == 5.0
    print(c.diameter)
    assert c.diameter == 10.0

def test_print():
    c = Circle(5)
    print(c)
    print(repr(c))
    assert repr(c) == "Circle(5.000)"
    assert str(c) == "Circle with radius: 5.000"

def test_add():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = c1 + c2
    print(c3)
    # assert c3.radius == 3.0
    assert repr(c3) == 'Circle(3.000)'

def test_mul():
    c1 = Circle(2)
    c2 = c1 * 3
    print(c2)
    assert repr(c2) == 'Circle(6.000)'
    c2 = 3 * c1
    print(c2)
    assert repr(c2) == 'Circle(6.000)'

def test_lt():
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = Circle(2)

    assert c1 < c2
    assert c2 > c3
    assert c1 == c3
    assert c1 >= c3
    assert c1 <= c3
