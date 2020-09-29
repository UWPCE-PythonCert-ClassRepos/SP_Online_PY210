# Chris Dela Pena
# Circle class test_eq

from circle import *
import random

def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_area():
    c = Circle(4)
    assert c.area == 4 * 4 * math.pi

def test_diameter_setter():
    c = Circle(4)
    c.diameter = 2
    assert c.radius == 1

def test_from_diameter():
    c = Circle.from_diameter(8)
    c1 = Circle(4)
    assert c.radius == 4
    assert c.diameter == 8

def test_str():
    c = Circle(4)
    assert str(Circle(4)) == "Circle with radius: 4.000000"

def test__repr():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'

def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c = c1 + c2
    assert c.radius == 6

def test_mult():
    c1 = Circle(4)
    c = c1 * 3
    assert c.radius == 12

def test_greater_than():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c2 > c1) is True

def test_less_than():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 < c2) is True

def test_equals():
    c1 = Circle(2)
    c2 = Circle(2)
    assert Circle(2) == Circle(2)

def test_sort():
    circles = [Circle(2), Circle(4), Circle(1), Circle(5), Circle(3)]
    circles.sort(key=Circle.sort_key)
    assert circles == [Circle(1), Circle(2), Circle(3), Circle(4), Circle(5)]

def test_area_sphere():
    s = Sphere(2)
    assert s.area == math.pi * 2 * 2 * 4

def test_volume_sphere():
    s = Sphere(2)
    assert s.volume == math.pi * 4 / 3 * 2 * 2 * 2
