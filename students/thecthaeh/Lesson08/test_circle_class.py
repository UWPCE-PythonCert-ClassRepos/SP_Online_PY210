#!/usr/bin/env python3

""" Test code for circle_class.py."""

import pytest
from circle_class import *

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
    assert round(c.area, 2) == 50.27

def test_set_area():
    c = Circle(4)
    
    with pytest.raises(AttributeError):
        c.area = 42
    
    print(c.area)

def test_from_diameter():
    c = Circle.from_diameter(8)
    
    print("Circle using diameter: ", c)
    print(c.diameter)
    
    assert c.diameter == 8
    assert c.radius == 4

def test_print():
    c = Circle(4)
    
    print(c)
    print(str(c))
    print(repr(c))
    
    assert str(c) == 'Circle with radius: 4'
    assert repr(c) == 'Circle(4)'

def test_math():
    c1 = Circle(2)
    c2 = Circle(4)
    
    print(repr(c1 + c2))
    print(repr(c2 * 3))
    print(repr(3 * c2))
    
    assert repr(c1 + c2) == repr(Circle(6))
    assert repr(c2 * 3) == repr(Circle(12))
    assert repr(3 * c2) == repr(c2 * 3)

def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    
    print(c1 > c2)
    print(c1 < c2)
    print (c2 == c3)
    
    assert (c1 > c2) == False
    assert c1 < c2
    assert (c1 == c2) == False
    assert c2 == c3

def test_sort_key():
    circles = [Circle(2), Circle(4), Circle(4), Circle(3), Circle(8), Circle(6)]
    print(circles)
    circles.sort(key=Circle.sort_key)
    print(circles)
    
    assert circles == [Circle(2), Circle(3), Circle(4), Circle(4), Circle(6), Circle(8)]

#def test_sphere_subclass():
    #add tests for sphere subclass

def test_sphere_print():
    s = Sphere(4)
    
    print(s)
    print(str(s))
    print(repr(s))
    
    assert str(s) == 'Sphere with radius: 4'
    assert repr(s) == 'Sphere(4)'

def test_sphere_volume():
    s = Sphere(4)
    
    print(s.volume)
    assert round(s.volume, 2) == 268.08

def test_surface_area_sphere():
    s = Sphere(4)
    
    print(s.area)
    assert round(s.area, 2) == 201.06

def test_from_diameter_sphere():
    s = Sphere.from_diameter(8)
    
    print("Sphere using diameter: ", s)
    print(s.diameter)
    
    assert s.diameter == 8
    assert s.radius == 4