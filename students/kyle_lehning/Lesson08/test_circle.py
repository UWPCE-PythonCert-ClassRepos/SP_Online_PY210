"""
test code for circle.py
"""

import io
import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from circle import *


def test_init():
    """
    Tests that a circle can be initiated with a radius
    """
    e = Circle(4)
    assert e.radius == 4


def test_diameter():
    """
    Tests that a circle diameter can be returned and set with an updating radius
    """
    e = Circle(5)
    assert e.diameter == 10
    e.diameter = 13
    assert e.radius == 6.5
    assert e.diameter == 13


def test_area():
    """
    Tests that a circle area can be calculated
    """
    e = Circle(2)
    assert round(e.area, 5) == 12.56637
    with pytest.raises(AttributeError):
        e.area = 10


def test_from_diameter():
    """
    Tests that a circle can be set from the diameter
    """
    e = Circle.from_diameter(8)
    assert e.radius == 4
    assert e.diameter == 8
    assert round(e.area, 5) == 50.26548


def test_str():
    """
    Tests that a string of a circle can be printed
    """
    e = Circle(3)
    assert str(e) == "Circle with radius: 3.000000"
    print(e)


def test_repr():
    """
    Tests that a rpr of a circle can be printed
    """
    e = Circle(3)
    assert repr(e) == "Circle(3)"
    print(repr(e))


def test_add():
    """
    Tests that circles can be added together
    """
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert repr(c3) == "Circle(6)"


def test_mul():
    """
    Tests that circles can be multiplied
    """
    c1 = Circle(3)
    c2 = c1 * 3
    assert repr(c2) == "Circle(9)"
    c3 = 3 * c1
    assert repr(c3) == "Circle(9)"
