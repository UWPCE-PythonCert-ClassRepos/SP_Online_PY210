#!/usr/bin/env python3
from circle import Circle, Sphere


def test_radius():
    c = Circle(4)
    assert c.radius == 4


def test_diameter_getter():
    c = Circle(4)
    assert c.diameter == 8


def test_diameter_setter():
    c = Circle(4)
    c.diameter = 10
    assert c.radius == 5


def test_area():
    c = Circle(4)
    assert c.area == 50.26548245743669


def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.radius == 4


def test_str():
    c = Circle(4)
    assert str(c) == "Circle with radius: 4.0"


def test_repr():
    c = Circle(4)
    assert repr(c) == "Circle(4.0)"
    assert eval(repr(c)) == Circle(4)


def test_addition():
    assert Circle(4) + Circle(8) == Circle(12)


def test_multiplication():
    assert Circle(4) * 2 == Circle(8)
    assert 2 * Circle(4) == Circle(8)


def test_comparison():
    assert Circle(4) == Circle(4)
    assert Circle(4) < Circle(8)
    assert Circle(4) <= Circle(8)
    assert Circle(8) > Circle(4)
    assert Circle(8) >= Circle(4)


def test_sort():
    clist = [Circle(8), Circle(4)]
    assert sorted(clist) == [Circle(4), Circle(8)]


def test_volume():
    s = Sphere(4)
    assert s.volume == 268.082573106329


def test_sphere_area():
    s = Sphere(4)
    assert s.area == 201.06192982974676
