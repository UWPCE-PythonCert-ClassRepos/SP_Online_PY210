#!/usr/bin/env python3

import math
import pytest
from sphere import Sphere

def test_constructor():
    c = Sphere(1)
    assert c.radius == 1


def test_alt_constructor():
    c = Sphere.using_diameter (2)
    assert c.radius == 1
    assert c.diameter == 2


def test_unhappy_set_zero():
    with pytest.raises(ValueError) as e:
        c = Sphere(0)


def test_unhappy_set_neg():
    with pytest.raises(ValueError) as e:
        c = Sphere(-1)


def test_set_diameter():
    radius = 1
    c = Sphere(radius)
    c.diameter = radius * 2
    assert c.diameter == radius * 2


def test_get_area():
    c = Sphere(1)
    assert c.area == pytest.approx (12.56,0.1)

    c = Sphere(2)
    assert c.area == pytest.approx (50.26,0.1)


def test_volume():
    s = Sphere(1)
    assert s.volume == pytest.approx (4.18,0.1)


def test_unhappy_set_area():
    c = Sphere(1)
    with pytest.raises(AttributeError) as e:
        c.area = 1


def test_str():
    c = Sphere(1)
    assert str(c).startswith('Sphere with radius:')
    assert '1.0' in str(c)


def test_repr():
    c = Sphere(2)
    d = eval(repr(c))
    assert d.radius == 2


def test_add():
    c1 = Sphere(1)
    c2 = Sphere(2)
    c3 = c1 + c2
    assert c3.radius == 3
    assert c3 == c1 + c2


def test_iadd():
    c1 = Sphere(1)
    c2 = Sphere(2)
    c2 += c1
    assert c2.radius == 3


def test_radd():
    c1 = Sphere(1)
    c2 = Sphere(2)
    c3 = c1 + c2
    assert c3 == 1 + c2


def test_sub():
    c1 = Sphere(1)
    c2 = Sphere(2)
    c3 = c2 - c1
    assert c3.radius == 1


def test_isub():
    c1 = Sphere(1)
    c2 = Sphere(2)
    c2 -= c1
    assert c2.radius == 1


def test_msub():
    c1 = Sphere(1)
    c2 = Sphere(2)
    c2 -= c1
    assert c1 == 2 - c2


def test_mul():
    c1 = Sphere(3)
    c2 = Sphere(4)
    c3 = c1 * c2
    assert c3.radius == 12
    assert c3 == 3 * c2


def test_imul():
    c1 = Sphere(3)
    c1 *= 2
    assert c1.radius == 6


def test_rmul():
    c1 = Sphere(3)
    c1 *= 2
    c2 = Sphere(18)
    assert c2 == 3 * c1


def test_lt():
    c1 = Sphere(1)
    c2 = Sphere(2)
    assert c1 < c2


def test_gt():
    c1 = Sphere(1)
    c2 = Sphere(2)
    assert c2 > c1


def test_eq():
    c1 = Sphere(1)
    assert c1 == Sphere(1)


def test_neq():
    c1 = Sphere(1)
    c2 = Sphere(2)
    assert c1 != c2


def test_sort():
    l = [Sphere(6), Sphere(7), Sphere(8), Sphere(4), Sphere(2), Sphere(3), Sphere(5), Sphere(9), Sphere(1)]
    l.sort(key=Sphere.sort_key)
    assert l == [Sphere(1), Sphere(2), Sphere(3), Sphere(4), Sphere(5), Sphere(6), Sphere(7), Sphere(8), Sphere(9)]

