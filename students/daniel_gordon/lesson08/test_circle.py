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
        c.area = 30

def test_print():
    c = Circle(4)
    assert str(c) == "A Circle of radius 4"
    assert repr(c) == "Circle(4)"
    
def test_add():
    c = Circle(3) + Circle(2)
    assert c.radius == 5
    c += Circle(5)
    assert c.radius == 10

def test_mult():
    c = Circle(1) * 4
    assert c.radius == 4
    c *= 3
    assert c.radius == 12
    c = 0.5 * c
    assert c.radius == 6