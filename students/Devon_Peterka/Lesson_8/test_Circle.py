#!/usr/bin/env python3

from Circle import Circle as circle
from Circle import Sphere as sphere
import math

def test_radius():
    c1 = circle(1)
    assert(c1.radius == 1)

def test_diameter():
    c1 = circle(1)
    c1.diameter = 4
    assert (c1.radius == 2)
    assert (c1.diameter == 4)

def test_setdiameter():
    c1 = circle(2)
    c1.diameter = 2
    assert (c1.radius == 1)
    assert (c1.diameter == 2)

def test_area():
    c1 = circle(1)
    assert (c1.area == math.pi)

def test_from_diameter():
    c1 = circle.from_diameter(8)
    assert (c1.radius == 4)
    assert (c1.diameter == 8)

def test_str():
    c1 = circle(4)
    assert (str(c1) == 'Circle with radius: 4')

def test_repr():
    c1 = circle(4)
    assert (repr(c1) == 'Circle(4)')

def test_add():
    c1 = circle(2)
    c2 = circle(4)
    assert ((c1 + c2).radius == circle(6).radius)

def test_mult():
    c1 = circle(2)
    assert ((c1 * 3).radius == circle(6).radius)

def test_compare():
    c1 = circle(2)
    c2 = circle(3)
    c3 = circle(2)
    assert((c1 < c2) is True)
    assert((c1 == c2) is False)
    assert((c3 == c1) is True)
    assert((c2 > c3) is True)
    assert((c1 <= c2) is True)

def test_sort():
    c1 = circle(1)
    c2 = circle(4)
    c3 = circle(2)
    c4 = circle(6)
    circles = [c1, c2, c3, c4]
    circles.sort()
    assert (circles == [circle(1), circle(2), circle(4), circle(6)])

def test_sphere():
    s = sphere(9)
    assert(str(s) == 'Sphere of radius: 9')
    assert(repr(s) == 'Sphere(9)')
