import pytest
from circle import Circle
from pytest import approx


def test_init():
    c = Circle(4)
    assert c.radius == 4


def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

    c.diameter = 4
    assert c.radius == 2


def test_area():
    c = Circle(2)
    assert c.area == approx(12.566370)

    with pytest.raises(AttributeError):
        c.area = 42


def test_from_diameter():
    c = Circle.from_diameter(4)
    assert c.radius == 2
    assert c.diameter == 4


def test_print():
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4.000000'


def test_repr():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'


def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert c3.radius == 6

    c1 += c2
    assert c1.radius == 6


def test_subtract():
    c1 = Circle(2)
    c2 = Circle(5)
    c3 = c2 - c1
    assert c3.radius == 3

    with pytest.raises(ValueError):
        c1 - c2

    c2 -= c1
    assert c2.radius == 3


def test_multiply():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 * c2
    assert c3.radius == 8

    c3 = c1 * 5
    assert c3.radius == 10

    c3 = 10 * c1
    assert c3.radius == 20

    assert c1 * 4 == 4 * c1

    c1 *= c2
    assert c1.radius == 8


def test_divide():
    c1 = Circle(8)
    c2 = Circle(2)
    c3 = c1 / c2
    assert c3.radius == 4

    c3 = c1 / 4
    assert c3.radius == 2

    c4 = Circle(0)
    with pytest.raises(ValueError):
        c1 / c4

    with pytest.raises(ValueError):
        c1 / 0

    c1 /= c2
    assert c1.radius == 4


def test_ordering():
    c1 = Circle(2)
    c2 = Circle(2)
    c3 = Circle(4)

    assert c1 == c2
    assert c1 < c3
    assert c3 > c2
    assert (c1 == c3) is False
    assert (c3 < c1) is False
    assert (c2 > c3) is False


def test_sort():
    c0 = Circle(0)
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = Circle(3)
    c4 = Circle(4)
    c5 = Circle(5)
    unsorted_list = [c2, c1, c4, c5, c0, c3]
    unsorted_list.sort()
    assert unsorted_list == [c0, c1, c2, c3, c4, c5]







