import pytest

from math import pi
from circle import *

def test_init():
    c = Circle(5)
    assert c.radius == 5

def test_diameter():
    c = Circle(7)
    assert c.diameter == 14
    c.diameter = 8
    assert c.radius == 4
    c = Circle.from_diameter(5)
    c.radius = 2.5

def test_area():
    c = Circle(5)
    assert c.area == 25*pi
    with pytest.raises(AttributeError):
        c.area = 20

def test_print():
    c = Circle(4)
    assert str(c) == "A circle of radius 4"