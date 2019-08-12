#!/usr/bin/env python3

from circle import *

def test_init():
    c = Circle(3)
    assert c.radius == 3

def test_diameter_getter():
    c = Circle(3)
    print(c.diameter)
    assert c.diameter == 6

def test_diameter_setter():
    c = Circle(4)
    c.diameter = 2
    print(c.radius)

def test_area():
    c = Circle(2)
    print(c.area)
    assert c.area == 12.566370614359172

def test_from_diameter():
    c = Circle.from_diameter(8)
    print(c.diameter)
    assert c.diameter == 8
    print(c.radius)
    assert c.radius == 4

def test_str():
    c = Circle(4)
    print(c)
    assert str(c) == "Circle with radius: 4"

def test_repr():
    c = Circle(4)
    repr(c)
    assert repr(c) == "Circle(4)"

def test_add_circles():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(c1 + c2) == "Circle(6)"

def test_multiply_circles():
    assert repr(Circle(4) * 3) == "Circle(12)"
    assert repr(3 * Circle(4)) == "Circle(12)"

def test_compare_circles():
    c1 = Circle(2)
    c2 = Circle(3)
    assert c1 < c2
    assert c2 > c1
    assert c1 != c2
    c2 = Circle(2)
    assert c1 == c2
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

def test_sphere_init():
    s = Sphere(3)
    assert s.radius == 3

def test_sphere_diameter():
    s = Sphere(3)
    print(s.diameter)
    assert s.diameter == 6

def test_sphere_area():
    s = Sphere(3)
    print(round(s.area, 1))
    assert round(s.area, 1) == 113.1

def test_sphere_volume():
    s = Sphere(4)
    print(round(s.volume, 2))
    assert round(s.volume, 2) == 268.08