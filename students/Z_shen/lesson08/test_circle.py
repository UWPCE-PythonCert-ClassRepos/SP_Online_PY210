from circle import *
import pytest


def test_init():

    c = Circle(4)
    assert c.radius == 4


def test_diameter():

    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 2
    assert c.radius == 1
    assert c.diameter == 2


def test_area():
    c = Circle(2)
    assert round(c.area, 5) == 12.566370
    with pytest.raises(AttributeError):
        c.area = 42


def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


def test_str():
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4'


def test_repr():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'
    print(repr(c))


def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert repr(c3) == "Circle(6)"


def test_mul():
    c2 = Circle(4)
    c4 = 3*c2
    assert repr(c4) == 'Circle(12)'


def test_lt():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 > c2) is False
    assert (c1 < c2) is True


def test_eq():
    c1 = Circle(2)
    c3 = Circle(2)
    assert (c1 == c3) is True


def test_sort():
    c1 = Circle(3)
    c2 = Circle(2)
    c3 = Circle(1)
    c = [c1, c2, c3]
    c.sort()
    assert c == [c3, c2, c1]


def test_sphere():

    c = Sphere(3)
    assert c.radius == 3
    assert c.diameter == 6
    assert round(c.volume, 1) == 113.1
    assert round(c.area, 1) == 113.1
    assert str(c) == 'Sphere with radius: 3'
    assert repr(c) == 'Sphere(3)'
    c2 = Sphere.from_diameter(8)
    assert c2.radius == 4