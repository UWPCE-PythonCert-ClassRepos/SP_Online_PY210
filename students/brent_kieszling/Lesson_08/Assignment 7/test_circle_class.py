#-------------------------------------------#
#Tittle: test_circle_class, PYTHON210 - Assignment 7
#Desc: Circle class test harness
#Change Log: (Who, When, What)
#Brent Kieszling, 2021-Jan-20, created file
#-------------------------------------------#
import io
import pytest

from circle_class import Circle, Sphere

def test_init():
    f = Circle(10)
    g = Circle(0)
    with pytest.raises(AttributeError):
        h = Circle(-1)


def test_radius():
     c = Circle(4)
     assert c.radius == 4

def test_diameter1():
    c = Circle(4)
    assert c.diameter == 8

def test_diameter2():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

def test_area1():
    c = Circle(2)
    assert round(c.area, 5) == 12.56637

def test_area2():
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 42

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_str():
    c = Circle(4)
    assert str(c) == "Circle with radius: 4.000000"

def test_repr():
    c = Circle(4)
    assert repr(c) == "'Circle(4)'"
    d = eval(repr(c))
    print(d)
    assert d == "Circle(4)"

def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    a = c1 + c2
    print(repr(a))
    assert repr(a) == "'Circle(6)'"

def test_sub():
    c1 = Circle(2)
    c2 = Circle(4)
    with pytest.raises(AttributeError):
        a = c1 - c2
    b = c2 - c1
    assert b == Circle(2)

def test_mult():
    c2 = Circle(4)
    c3 = c2 * 3
    c4 = 3 * c2
    assert c3 == Circle(12)
    assert c4 == Circle(12)
    assert repr(c2 * 3) == "'Circle(12)'"
    assert repr(3 * c2) == "'Circle(12)'"
    assert repr(c2 * 3) == repr(3 * c2)

def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    w = c1 < c2
    assert w == True
    x = c1 > c2
    assert x == False
    y = c1 == c2
    assert y == False
    c3 = c2
    z = c3 == c2
    assert  z == True

def test_sort():
    c0 = Circle(0)
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = Circle(3)
    circles = [c2, c3, c1, c0]
    assert circles[0] == c2
    circles.sort()
    print(circles)
    assert circles[0] == c0
    assert circles[3] == c3

def test_iadd():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(6)
    c1 += c2
    assert c1.radius == 6
    assert repr(c1) == repr(c3)

def test_isub():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(6)
    with pytest.raises(AttributeError):
        c1 -= c2
    c3 -= c2
    assert c3 == Circle(2)

def test_divide():
    c2 = Circle(6)
    c3 = c2 / 3
    c4 = Circle(2)
    c5 = Circle(1)
    print(type(c3))
    assert c3 == c4
    assert c5 == (6 / c2)
    assert repr(c2 / 3) == "'Circle(2)'"
    assert repr(6 / c2) == "'Circle(1)'"

def test_imul():
    c1 = Circle(2)
    c1 *= 2
    assert c1 == Circle(4)

def test_idiv():
    c1 = Circle(6)
    c1 /= 2
    assert c1 == Circle(3)

def test_str_sphere():
    c = Sphere(4)
    assert str(c) == "Sphere with radius: 4.000000"

def test_repr_sphere():
    c = Sphere(4)
    assert repr(c) == "'Sphere(4)'"
    d = eval(repr(c))
    print(d)
    assert d == "Sphere(4)"

def test_volume():
    c = Sphere(4)
    assert round(c.volume, 2) == 268.08

def test_area_sphere():
    c = Sphere(4)
    print(c.area)
    assert round(c.area, 2) == 201.06

def test_from_diameter_sphere():
    c = Sphere.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4






















