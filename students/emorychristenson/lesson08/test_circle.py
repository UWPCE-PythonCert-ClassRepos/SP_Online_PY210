#!/usr/bin/env python3

import pytest
from circle import *

def test_init():
    c = Circle(8)
    assert c.radius == 8
    s = Sphere(8)
    assert s.radius == 8

def test_diameter():
    c = Circle(8)
    assert c.diameter == 16
    s = Sphere(8)
    assert s.diameter == 16

def test_diameter_setter():
    c = Circle(8)
    c.diameter = 4
    assert c.radius == 2
    s = Sphere(8)
    s.diameter = 4
    assert s.radius == 2

def test_area():
    c = Circle(4)
    assert c.area == 50.26548245743669
    with pytest.raises(AttributeError):
        c.area = 5
    s = Sphere(4)
    assert s.area == 201.06192982974676
    with pytest.raises(AttributeError):
        s.area = 5

def test_from_diameter():
    c = Circle.from_diameter(6)
    assert c.radius == 3
    s = Sphere.from_diameter(6)
    assert s.radius == 3

def test_str():
    c = Circle(8)
    assert str(c) == "Circle with radius 8.00"
    s = Sphere(8)
    assert str(s) == "Sphere with radius 8.00"

def test_repr():
    c = Circle(8)
    assert repr(c) == "Circle(8)"
    s = Sphere(2)
    assert repr(s) == "Sphere(2)"

def test_add():
    c = Circle(8)
    c2 = Circle(2)
    assert repr(c + c2) == "Circle(10)"

def test_multiply():
    c = Circle(8)
    assert repr(c * 2) == "Circle(16)"

def test_right_multiply():
    c = Circle(8)
    assert repr(2 * c) == "Circle(16)"

def test_lt():
    c = Circle(8)
    c2 = Circle(2)
    assert c2 < c

def test_gt():
    c = Circle(8)
    c2 = Circle(2)
    assert c > c2

def test_eq():
    c = Circle(8)
    c2 = Circle(8)
    assert c == c2

def test_sort():
    circles = [Circle(3),Circle(0),Circle(2),Circle(1)]
    circles.sort()
    assert circles == [Circle(0),Circle(1),Circle(2),Circle(3)]

def test_volume():
    s = Sphere(8)
    assert s.volume == 2144.660584850632


