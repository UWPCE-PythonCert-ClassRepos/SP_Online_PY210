"""
test code for circle.py
"""


from circle import *
import pytest


def test_init():
    """
    Tests that a circle can be initiated with a radius
    """
    e = Circle(4)
    assert e.radius == 4


def test_diameter():
    """
    Tests that a circle diameter can be returned and set with an updating radius
    """
    e = Circle(5)
    assert e.diameter == 10
    e.diameter = 13
    assert e.radius == 6.5
    assert e.diameter == 13


def test_area():
    """
    Tests that a circle area can be calculated
    """
    e = Circle(2)
    assert round(e.area, 5) == 12.56637
    with pytest.raises(AttributeError):
        e.area = 10


def test_from_diameter():
    """
    Tests that a circle can be set from the diameter
    """
    e = Circle.from_diameter(8)
    assert e.radius == 4
    assert e.diameter == 8
    assert round(e.area, 5) == 50.26548


def test_str():
    """
    Tests that a string of a circle can be printed
    """
    e = Circle(3)
    assert str(e) == "Circle with radius: 3.000000"
    print(e)


def test_repr():
    """
    Tests that a rpr of a circle can be printed
    """
    e = Circle(3)
    assert repr(e) == "Circle(3)"
    print(repr(e))


def test_add():
    """
    Tests that circles can be added together
    """
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert repr(c3) == "Circle(6)"


def test_mul():
    """
    Tests that circles can be multiplied
    """
    c1 = Circle(3)
    c2 = c1 * 3
    assert repr(c2) == "Circle(9)"
    c3 = 3 * c1
    assert repr(c3) == "Circle(9)"


def test_compare():
    """
    Tests that circles can be compared
    """
    c1 = Circle(5)
    c2 = Circle(6)
    c3 = Circle.from_diameter(12)
    c4 = Circle(2)

    assert c1 < c2
    assert not (c1 > c2)
    assert c2 > c1
    assert not (c2 < c1)
    assert c2 == c3
    assert not (c1 == c2)
    assert c1 != c2
    assert not c2 != c3
    circles = [c1, c2, c4]
    circles.sort()
    assert circles == [Circle(2), Circle(5), Circle(6)]


def test_div():
    """
    Tests that circles can be divided
    """
    c1 = Circle(6)
    c2 = c1 / 2
    assert repr(c2) == "Circle(3.0)"
    c3 = 12 / c1
    assert repr(c3) == "Circle(2.0)"
    c4 = c1 // 2
    assert repr(c4) == "Circle(3)"
    c5 = 12 // c1
    assert repr(c5) == "Circle(2)"


def test_augmentation():
    """
    Tests that circles can be augmented
    """
    c1 = Circle(4)
    c2 = Circle(6)
    c2 += c1
    assert repr(c2) == "Circle(10)"
    c1 *= 2
    assert repr(c1) == "Circle(8)"


def test_sphere():
    """
    Tests sphere
    """
    e = Sphere(2)
    assert e.radius == 2
    assert e.diameter == 4
    assert round(e.volume, 2) == 33.51
    assert round(e.area, 2) == 50.27
    assert str(e) == "Sphere with radius: 2.000000"
    assert repr(e) == "Sphere(2)"
    e2 = Sphere.from_diameter(10)
    assert e2.radius == 5
    e3 = Sphere(6)
    assert repr(e + e3) == "Sphere(8)"
    assert repr(e * 2) == "Sphere(4)"
    e4 = Sphere(2)

    assert e < e3
    assert not (e > e3)
    assert e3 > e
    assert not (e3 < e)
    assert e == e4
    assert not (e == e2)
    assert e != e2
    assert not e != e4
    circles = [e3, e, e2]
    circles.sort()
    assert circles == [Sphere(2), Sphere(5), Sphere(6)]