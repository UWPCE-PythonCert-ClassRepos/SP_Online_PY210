#!/usr/bin/env python

from circle import *
import math
import pytest

def test_create_obj():
    c1 = Circle(4)
    assert c1.radius == 4

def test_diameter():
    c1 = Circle(4)
    assert c1.diameter == 8

def test_area():
    c1 = Circle(4)
    assert c1.area == ((4**2)*math.pi)

def test_circle_str():
    c1 = Circle(4)
    assert str(c1) == 'Circle with radius: 4.0000'

def test_sphere_repr():
    c1 = Sphere(4)
    assert repr(c1) == 'Circle(4)'

def test_add():
    c1, c2 = Circle(4), Circle(5)
    assert c1 + c2 == Circle(9)

def test_multiply():
    c1, c2 = Circle(2), Circle(3)
    assert repr(c1 * 3) == 'Circle(6)'
    assert repr(3 * c1) == 'Circle(6)'

def test_equal():
    c1, c2, c3 = Circle(4), Circle(5), Circle(4)
    assert c1 == c3
    assert c1 != c2

def test_ln():
    c1, c2, c3 = Circle(10), Circle(8), Circle(15)
    assert c1 < c3
    assert c1 > c2

def test_sort():
    l1 = [Circle(i) for i in range(1,5)]
    l2 = [Circle(3), Circle(1), Circle(4), Circle(2)]
    l2.sort()
    assert l2 == l1

def test_sub():
    c1, c2, c3 = Circle(4), Circle(6), Circle(2)
    assert c1 - c2 == Circle(0)
    assert c2 - c1 == c3

def test_reflection():
    c1, c2 = Circle(3), Circle(3)
    assert c1 * 3 == c2 * 3

def test_sphere():
    s1 = Sphere(5)
    assert s1.radius == 5

def test_sphere_volume():
    s1 = Sphere(4)
    assert s1.volume == (4/3) * (4**3) * math.pi

def test_sphere_area():
    s1 = Sphere(4)
    try:
        s1.area
        assert False
    except NotImplementedError:
        assert True

def test_sphere_str():
    s1 = Sphere(4)
    assert str(s1) == 'Sphere with radius: 4.0000'

def test_sphere_repr():
    s1 = Sphere(4)
    assert repr(s1) == 'Sphere(4)'