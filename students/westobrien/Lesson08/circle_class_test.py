import io
import pytest
import math

from circle_class import *


def test_1():
    c = Circle(5)
    assert c


def test_diameter():
    c = Circle(4)
    assert c.diameter is 8


def test_area():
    c = Circle(4)
    assert c.area == float(c.radius * c.radius * math.pi)


def test_alternate_constructor():
    c = Circle.from_diameter(4)
    assert c
    assert c.radius == 2


def test_str():
    c = Circle(4)
    assert("Circle with radius: 4") in str(c)


def test_repr():
    c = Circle(4)
    d = eval(repr(c))
    assert d.radius == 4


def test_add():
    c = Circle(4)
    d = Circle(6)
    e = c + d
    assert e.radius == 10


def test_multiply():
    c = Circle(4)
    d = c * 3
    assert d.radius == 12


def test_lt():
    c = Circle(5)
    d = Circle(6)
    assert c < d
    e = Circle(5)
    assert c == e


def test_sort():
    a = Circle(1)
    b = Circle(2)
    c = Circle(3)
    d = Circle(4)
    circle_list = [d, b, c, a]
    circle_list.sort()
    assert circle_list == [a, b, c, d]


def test_str_sphere():
    s = Sphere(4)
    assert("Sphere with radius: 4") in str(s)


def test_repr_sphere():
    s = Sphere(4)
    d = eval(repr(s))
    assert d.radius == 4


def test_volume():
    s = Sphere(4)
    assert s.volume == (4 / 3) * math.pi * pow(4,2)

def test_surface_area():
    s = Sphere(4)
    assert s.area == 4 * math.pi * pow(s.radius, 2)

def test_from_diameter_sphere():
    s = Sphere.from_diameter(4)
    assert s.radius == 2
