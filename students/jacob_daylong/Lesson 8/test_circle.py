from circle import *
import pytest

def test_radius():
    #  Test Radius
    c = Circle(5)
    assert c.radius == 5
    c.radius = 5
    assert c.radius == 5

def test_diameter():
    # Test diameter
    c = Circle(5)
    assert c.diameter == 10
    c.diameter = 20
    assert c.radius == 10
    assert c.diameter == 20

def test_area():
    # Test Area
    c = Circle(5)
    assert c.area == 78.539816339744830961566084581988
    
def test_str():
    c = Circle(5)
    assert str(c) == "Circle with a radius of 5.00"

def test_repr():
    c = Circle(4)
    assert repr(c) == "Circle(4)"