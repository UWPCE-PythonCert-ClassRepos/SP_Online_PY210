#test cases

import pytest


from circle import *

def test_circle_radius():
    c = Circle(4)
    assert c.radius == 4

def test_circle_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_circle_diameter_setter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

def test_circle_area():
    c = Circle(2)
    assert c.area == 12.566370614359172

def test_circle_area_set():
    with pytest.raises(AttributeError):
        c = Circle(2)
        c.area = 42

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

    
def test_rep():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'
    d = eval(repr(c))
    assert d.radius == 4

def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(c1 + c2) == repr(Circle(6))


def test_multiply():
    c1 = Circle(4)
    assert repr(c1 * 3) == repr(Circle(12))

def test_lessthan():
    pass

def test_greaterthan():
    pass

def test_equal():
    pass
