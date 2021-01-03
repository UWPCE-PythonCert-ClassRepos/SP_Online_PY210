from io import StringIO
import sys
import math
from circle_class import *


def test_attr():

    c = Circle(5)

    assert c.radius == 5


def test_diam_attr():

    c = Circle(5)

    assert c.diameter == 10


def test_diam_update():

    c = Circle(10)

    c.diameter = 4
    assert c.radius == 2


def test_alt_construct():

    c = Circle.from_diameter(8)

    assert c.diameter == 8

    assert c.radius == 4


def test_print_circle():
    c = Circle(4)

    assert str(c) == 'Circle with radius: 4'
    assert repr(c) == 'Circle(4)'


def test_add_circles():

    c1 = Circle(2)

    c2 = Circle(4)

    assert c1 + c2 == Circle(6)


def test_mul_circles():
    c1 = Circle(2)

    c2 = Circle(4)

    assert 3 * c2 == Circle(12)


def test_compare_circles():
    c1 = Circle(2)

    c2 = Circle(4)

    c3 = Circle(4)

    assert c1 < c2
    assert c2 > c1
    assert c2 == c3


def test_circle_list():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = Circle(3)
    c4 = Circle(4)

    circle_list = [c2, c4, c3, c1]

    circle_list.sort()

    assert circle_list == [Circle(1), Circle(2), Circle(3), Circle(4)]


def test_sphere():

    s1 = Sphere(4)

    s1.radius == 4
    s1.diameter == 8


def test_sphere_volume():
    s1 = Sphere(10)
    assert int(s1.volume) == int(4188.79)


def test_sphere_sa():
    s1 = Sphere(10)
    assert s1.area == 4 * math.pi * 10 ** 2
