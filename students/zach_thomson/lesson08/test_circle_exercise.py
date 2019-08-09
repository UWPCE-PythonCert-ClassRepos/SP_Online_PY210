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

def test_circle_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_circle(capsys):
    c = Circle(4)
    print(str(c))
    captured = capsys.readouterr()
    assert captured.out == 'Circle with radius: 4.000000\n'
    assert repr(c) == "Circle(4)"
