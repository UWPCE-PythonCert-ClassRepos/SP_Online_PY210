#!/usr/bin/env python3

"""PY210_SP - circle class unit tests
author: Nick Miller"""

import pytest
import math
from circle_class import *


def test_init_circle():
    circle = Circle(10)
    assert circle.radius == 10


def test_str_circle():
    assert str(Circle(10)) == "This circle has a radius of : 10"


def test_get_diameter():
    circle = Circle(5)
    assert circle.diameter == 5 * 2


def test_set_diameter():
    circle = Circle(4)
    assert circle.radius == 4
    assert circle.diameter == 4 * 2

    Circle.diameter = 8
    assert circle.diameter == 8
    assert circle.diameter == circle.radius * 2


def test_area_circle():
    circle = Circle(4)
    assert circle.area == math.pi * 4 ** 2


def test_diameter_creator():
    circle = Circle.from_diameter(12)
    assert circle.radius == 6
    sphere = Sphere.from_diameter(12)
    assert sphere.radius == 6


def test_add_circle():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = c1 + c2
    assert c3 == Circle(3)


def test_sub_circle():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = c2 - c1
    assert c3 == Circle(1)


def test_mul_circle():
    c1 = Circle(2)
    c2 = c1 * 3
    assert c2 == Circle(6)


def test_rmul_circle():
    c1 = Circle(2)
    c2 = 3 * c1
    assert c2 == Circle(6)


def test_lt_circle():
    c1 = Circle(1)
    c2 = Circle(2)
    assert c1 < c2


def test_gt_circle():
    c1 = Circle(5)
    c2 = Circle(2)
    assert c1 > c2


def test_eq_circle():
    c1 = Circle(2)
    c2 = Circle(2)
    assert c1 == c2


def test_circle_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]


def test_init_sphere():
    sphere = Sphere(10)
    assert sphere.radius == 10


def test_str_sphere():
    assert str(Sphere(10)) == "This sphere has a radius of : 10"


def test_volume_sphere():
    sphere = Sphere(4)
    assert sphere.volume == (4/3) * math.pi * 4 ** 3


def test_area_sphere():
    sphere = Sphere(4)
    assert sphere.area == (4 * math.pi) * 4 ** 2


