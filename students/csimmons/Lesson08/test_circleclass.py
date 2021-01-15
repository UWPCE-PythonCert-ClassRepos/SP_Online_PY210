#!/usr/bin/env python3
#Craig Simmons
# Python 210
# Lesson08 Asignment - pytest unit tests
# Created 01/14/2021 - csimmons

import pytest
from math import pi
from circleclass import *

def test_init():
    c = Circle(5)
    assert c.radius == 5
    
def test_diameter_property():
    c = Circle(5)
    assert c.diameter == 10

def test_diameter_setter():
    c = Circle(8)
    assert c.diameter == 16
    assert c.radius == 8
    c.radius = 10
    assert c.diameter == 20 
    assert c.radius == 10
    c.diameter = 10
    assert c.diameter == 10 
    assert c.radius == 5

def test_area_property():
    c = Circle(5)
    assert c.area == (pi * 25)
    try:
        c.area = 100
    except AttributeError as error:
        print('c.area is ' + str(c.area))
    c.radius = 10
    assert c.area == (pi * 100)
    c.diameter = 6
    assert c.area == (pi * 9)

def test_from_diameter():
    c = Circle(5)
    c.diameter = 20
    assert c.radius == 10
    c.radius = 10
    assert c.diameter == 20

def test_dunder_str():
    c = Circle(5)
    print(str(c))
    assert str(c) == 'Circle with radius: 5.00'

def test_dunder_repr():
    c = Circle(5)
    print(str(c))
    assert repr(c) == 'Circle(5)'

def test_dunder_str_sphere():
    s = Sphere(5)
    print(str(s))
    assert str(s) == 'Sphere with radius: 5.00'

def test_dunder_repr_sphere():
    s = Sphere(5)
    print(str(s))
    assert repr(s) == 'Sphere(5)'

def test_dunder_add():
    c = Circle(5)
    c2 = Circle(10)
    assert c.radius + c2.radius == 15

def test_dunder_add_sphere():
    s = Sphere(5)
    s2 = Sphere(10)
    assert s.radius + s2.radius == 15

def test_dunder_mul():
    c = Circle(5)
    assert c.radius * 6 == 30
    assert 6 * c.radius == 30

def test_dunder_mul_sphere():
    s = Sphere(5)
    assert s.radius * 6 == 30
    assert 6 * s.radius == 30

def test_dunder_rmul():
    c = Circle(5)
    assert 6 * c.radius == 30
    assert c.radius * 6 == 30

def test_dunder_rmul_sphere():
    s = Sphere(5)
    assert 6 * s.radius == 30
    assert s.radius * 6 == 30

def test_dunder_comparisons():
    c = Circle(10)
    c2 = Circle(10)
    assert c.radius == c2.radius
    assert c.radius <= c2.radius
    assert c.radius >= c2.radius
    c = Circle(15)
    c2 = Circle(10)
    assert c.radius != c2.radius
    c = Circle(5)
    c2 = Circle(10)
    assert c.radius < c2.radius
    assert not c.radius > c2.radius
    assert c.radius <= c2.radius
    assert not c.radius >= c2.radius
    c = Circle(15)
    c2 = Circle(10)
    assert c.radius > c2.radius
    assert not c.radius < c2.radius

def test_dunder_comps_sphere():
    s = Sphere(10)
    s2 = Sphere(10)
    assert s.radius == s2.radius
    assert s.radius <= s2.radius
    assert s.radius >= s2.radius
    s = Sphere(15)
    s2 = Sphere(10)
    assert s.radius != s2.radius
    s = Sphere(5)
    s2 = Sphere(10)
    assert s.radius < s2.radius
    assert not s.radius > s2.radius
    assert s.radius <= s2.radius
    assert not s.radius >= s2.radius
    s = Sphere(15)
    s2 = Sphere(10)
    assert s.radius > s2.radius
    assert not s.radius < s2.radius

def test_basic_sorting():
    circles = [Circle(2), Circle(4), Circle(3), Circle(8)]
    circles.sort()
    print(circles)
    assert circles == [Circle(2), Circle(3), Circle(4), Circle(8)]

def test_sphere_sorting():
    spheres = [Sphere(2), Sphere(4), Sphere(3), Sphere(8)]
    spheres.sort()
    print(spheres)
    assert spheres == [Sphere(2), Sphere(3), Sphere(4), Sphere(8)]