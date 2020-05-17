import pytest
from circle import Sphere
from pytest import approx


def test_init():
    s = Sphere(4)
    assert s.radius == 4


def test_diameter():
    s = Sphere(4)
    assert s.diameter == 8

    s.diameter = 4
    assert s.radius == 2


def test_area():
    s = Sphere(2)
    assert s.area == approx(50.2654824)

    with pytest.raises(AttributeError):
        s.area = 42


def test_volume():
    s = Sphere(5)
    assert s.volume == approx(523.59877)


def test_from_diameter():
    s = Sphere.from_diameter(4)
    assert s.radius == 2
    assert s.diameter == 4
    assert s.area == approx(50.26548245743669)


def test_print():
    s = Sphere(4)
    assert str(s) == 'Sphere with radius: 4.000000'


def test_repr():
    s = Sphere(4)
    assert repr(s) == 'Sphere(4)'


def test_add():
    s1 = Sphere(2)
    s2 = Sphere(4)
    s3 = s1 + s2
    assert s3.radius == 6

    s1 += s2
    assert s1.radius == 6


def test_subtract():
    s1 = Sphere(2)
    s2 = Sphere(5)
    s3 = s2 - s1
    assert s3.radius == 3

    with pytest.raises(ValueError):
        s1 - s2

    s2 -= s1
    assert s2.radius == 3


def test_multiply():
    s1 = Sphere(2)
    s2 = Sphere(4)
    s3 = s1 * s2
    assert s3.radius == 8

    s3 = s1 * 5
    assert s3.radius == 10

    s3 = 10 * s1
    assert s3.radius == 20

    assert s1 * 4 == 4 * s1

    s1 *= s2
    assert s1.radius == 8


def test_divide():
    s1 = Sphere(8)
    s2 = Sphere(2)
    s3 = s1 / s2
    assert s3.radius == 4

    s3 = s1 / 4
    assert s3.radius == 2

    s4 = Sphere(0)
    with pytest.raises(ValueError):
        s1 / s4

    with pytest.raises(ValueError):
        s1 / 0

    s1 /= s2
    assert s1.radius == 4


def test_ordering():
    s1 = Sphere(2)
    s2 = Sphere(2)
    s3 = Sphere(4)

    assert s1 == s2
    assert s1 < s3
    assert s3 > s2
    assert (s1 == s3) is False
    assert (s3 < s1) is False
    assert (s2 > s3) is False


def test_sort():
    s0 = Sphere(0)
    s1 = Sphere(1)
    s2 = Sphere(2)
    s3 = Sphere(3)
    s4 = Sphere(4)
    s5 = Sphere(5)
    unsorted_list = [s2, s1, s4, s5, s0, s3]
    unsorted_list.sort()
    assert unsorted_list == [s0, s1, s2, s3, s4, s5]







