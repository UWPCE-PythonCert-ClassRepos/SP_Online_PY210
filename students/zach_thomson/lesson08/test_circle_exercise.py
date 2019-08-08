import pytest
from circle_exercise import *

def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_init():
    '''test to make sure class Circle requires radius'''
    with pytest.raises(TypeError):
        c = Circle()

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 2
    assert c.radius == 1

def test_area():
    c = Circle(2)
    assert c.area == 12.566370614359172
    with pytest.raises(AttributeError):
        c.area = 42
