from circle import *

import math

import pytest

def test_init():
    c = Circle(4)
    assert c.radius == 4

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

def test_area():
    c = Circle(4)
    assert c.area == math.pi * 16
    with pytest.raises(AttributeError):
        c.area = 1

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.radius == 4

def test_str_and_repr():
    c = Circle(4)
    assert str(c) == "A circle with radius: 4"
    assert eval(repr(c)) == Circle(4)

def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)

def test_multiply():
    c1 = Circle(2)
    assert c1 * 3 == Circle(6)
    assert 3 * c1 == Circle (6)

def test_comparisons():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert c1 < c2
    assert c2 > c1
    assert c1 != c2
    assert c2 == c3

def test_reflected():
    c1 = Circle(2)
    assert c1 * 3 == 3 * c1

def test_augmented():
    c1 = Circle(2)
    c2 = Circle(4)
    c1 += c2
    assert c1 == Circle(6)
    c1 *= 2
    assert c1 == Circle(12)

def test_sphere():
    s = Sphere(4)
    assert s.radius == 4
    assert str(s) == "A sphere with radius: 4"
    assert eval(repr(s)) == Sphere(4)
    assert s.volume == 4/3 * math.pi * 64
    assert s.area == 4 * math.pi * 16

    s = Sphere.from_diameter(8)
    assert s.radius == 4
    assert eval(repr(s)) == Sphere(4)