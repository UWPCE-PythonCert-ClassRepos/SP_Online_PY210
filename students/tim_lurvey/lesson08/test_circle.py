#!/usr/bin/env python
__author__ = 'Timothy Lurvey'

from circle import *


def test_Circle_init():
    c = Circle(1)
    assert isinstance(c, Circle)
    assert c.radius == 1


def test_Circle_init2():
    c = Circle()
    assert isinstance(c, Circle)
    assert c.radius == 0.


def test_Circle_radius_set():
    c = Circle(1)
    c.radius = 9
    assert c.radius == 9


def test_Circle_radius_set_error():
    c = Circle(1)
    try:
        c.radius = 'aa'
    except Exception as e:
        err = e
    assert isinstance(err, TypeError)
    assert "{}".format(err) == "radius input must be numeric"


def test_Circle_diameter():
    c = Circle(1)
    assert c.diameter == 2


def test_Circle_diameter_property():
    c = Circle(1)
    try:
        c.diameter = 3
    except Exception as e:
        err = e
    assert isinstance(err, AttributeError)
    assert "{}".format(err) == "can't set attribute"


def test_Circle_from_diameter():
    c = Circle().from_diamter(4)
    assert c.radius == 2


def test_Circle_area():
    c = Circle(2)
    assert c.area == pi * (c.radius ** 2)


def test_Circle_area_property():
    c = Circle(1)
    try:
        c.area = 3
    except Exception as e:
        err = e
    assert isinstance(err, AttributeError)
    assert "{}".format(err) == "can't set attribute"


def test_Circle_from_diamter():
    c = Circle.from_diamter(8)
    assert isinstance(c, Circle)
    assert c.radius == 4


def test_Circle_str():
    c = Circle(1)
    assert c.__str__() == "Circle class with radius of 1.000"


def test_Circle_repr():
    r = 1.000001
    c = Circle(r)
    assert repr(c) == "Circle(1.000001)"
    c2 = eval(repr(c))
    assert isinstance(c2, Circle)
    assert c2.radius == r


def test_Circle_math_add():
    c2 = Circle(2)
    c4 = Circle(4)
    assert (c2 + c4) == Circle(6.0)


def test_Circle_math_iadd():
    c2 = Circle(2)
    c2 += Circle(4)
    assert c2 == Circle(6.0)


def test_Circle_math_radd():
    assert 2 + Circle(2) == Circle(4)
    assert 2 + Circle(2) == Circle(2) + 2


def test_Circle_math_sub():
    c2 = Circle(2)
    c4 = Circle(4)
    assert (c2 - c4) == Circle(-2.0)


def test_Circle_math_isub():
    c2 = Circle(2)
    c2 -= Circle(4)
    assert c2 == Circle(-2.0)


def test_Circle_math_rsub():
    assert 1 - Circle(2.0) == Circle(1)
    assert 2 - Circle(2.0) == Circle(2.0) - 2


def test_Circle_math_mul():
    c2 = Circle(2)
    c4 = Circle(4)
    assert (c2 * c4) == Circle(8.0)


def test_Circle_math_imul():
    c2 = Circle(2)
    c2 *= Circle(4)
    assert c2 == Circle(8.0)


def test_Circle_math_rmul():
    assert 2 * Circle(2) == Circle(4)
    assert 2 * Circle(2) == Circle(2) * 2


def test_Circle_math_div():
    c2 = Circle(2)
    c4 = Circle(4)
    assert (c4 / c2) == Circle(2.0)


def test_Circle_math_idiv():
    c2 = Circle(2)
    c2 /= Circle(4)
    assert c2 == Circle(0.5)


def test_Circle_math_gtr():
    c2 = Circle(2)
    c4 = Circle(4)
    assert c2 < c4
    assert c2 <= 3
    assert c2 <= 2


def test_Circle_math_lth():
    c2 = Circle(2)
    c4 = Circle(4)
    assert c4 > c2
    assert 3 >= c2
    assert 2 >= c2


def test_Circle_math_sort():
    c2 = Circle(2)
    c4 = Circle(4)
    c6 = Circle(6)
    c8 = Circle(8)
    lx = [c6, c2, c8, c4]
    lx.sort()
    assert lx == [c2, c4, c6, c8]


def test_Sphere_init():
    s2 = Sphere(2)
    assert isinstance(s2, Sphere)
    assert isinstance(s2, Circle)


def test_Sphere_init2():
    s2 = Sphere()
    assert isinstance(s2, Sphere)
    assert isinstance(s2, Circle)
    assert s2.radius == 0.


def test_Sphere_radius():
    s2 = Sphere(2)
    assert s2.radius == 2


def test_Sphere_area():
    s2 = Sphere(2)
    assert s2.area == 4 * pi * 2 ** 2


def test_Sphere_volume():
    s2 = Sphere(2)
    assert s2.volume == 4 / 3 * pi * 2 ** 3


def test_Sphere_from_diameter():
    s2 = Sphere().from_diamter(4)
    assert s2.volume == 4 / 3 * pi * 2 ** 3
