#!/usr/bin/env python3

""" Test code for sparse_array.py."""

import pytest
from sparse_array import *

def test_radius():
    c = Circle(4)
    
    print(c.radius)
    assert c.radius == 4

def test_diameter():
    c = Circle(4)
    
    print(c.diameter)
    assert c.diameter == 8

def test_set_diameter():
    c = Circle(4)
    
    c.diameter = 2
    print(c.diameter)
    print(c.radius)
    
    assert c.diameter == 2
    assert c.radius == 1

def test_area():
    c = Circle(4)
    
    print(c.area)
    assert c.area == 50.27

def test_set_area():
    c = Circle(4)
    
    with pytest.raises(AttributeError):
        c.area = 42
    
    print(c.area)

def test_from_diameter():
    c = Circle.from_diameter(8)
    
    print(c.diameter)
    print(c.radius)
    
    assert c.diameter == 8
    assert c.radius == 4

def test_print():
    c = Circle(4)
    d = eval(repr(c))
    
    print(c)
    print(repr(c))
    print(d)
    
    assert c == 'Circle with radius: 4.000000'
    assert repr(c) == "'Circle(4)'"
    assert d == 'Circle(4)'

def test_math():
    c1 = Circle(2)
    c2 = Circle(4)
    
    print(c1 + c2)
    print(c2 * 3)
    print(3 * c2)
    
    assert c1 + c2 == Circle(6)
    assert c2 * 3 == Circle(12)
    #add assert to deal with 3 * c2

def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    
    assert c1 > c2 is False
    assert c1 < c2 is True
    assert c1 == c2 is False
    assert c2 == c3 is True

def test_sort():
    circles = [Circle(2), Circle(4), Circle(4), Circle(3), Circle(8), Circle(6)]
    circles.sort()
    print(circles)
    
    assert circles == [Circle(2), Circle(3), Circle(4), Circle(4), Circle(6), Circle(8)]

#def test_sphere_subclass():
    #add tests for sphere subclass