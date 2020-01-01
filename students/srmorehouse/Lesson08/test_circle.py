#!/usr/bin/env python3

import math
import pytest
from circle import Circle

def test_constructor():
    c = Circle(1)
    assert c.radius == 1

def test_alt_constructor():
    c = Circle.using_diameter (2)
    assert c.radius == 1
    assert c.diameter == 2

def test_unhappy_set_zero():
    with pytest.raises(ValueError) as e:
        c = Circle(0)

def test_unhappy_set_neg():
    with pytest.raises(ValueError) as e:
        c = Circle(-1)

def test_set_diameter():
    radius = 1
    c = Circle(radius)
    c.diameter = radius * 2
    assert c.diameter == radius * 2

def test_get_area():
    c = Circle(1)
    assert c.area == pytest.approx (3.14,0.1)

    c = Circle(2)
    assert c.area == pytest.approx (12.56,0.1)

def test_unhappy_set_area():
    c = Circle(1)
    with pytest.raises(AttributeError) as e:
        c.area = 1

def test_str():
    c = Circle(1)
    assert str(c).startswith('Circle with radius:')
    assert '1.0' in str(c)

def test_repr():
    c = Circle(2)
    d = eval(repr(c))
    assert d.radius == 2

def test_add():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = c1 + c2
    assert c3.radius == 3
    assert c3 == c1 + c2

def test_iadd():
    c1 = Circle(1)
    c2 = Circle(2)
    c2 += c1
    assert c2.radius == 3

def test_radd():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = c1 + c2
    assert c3 == 1 + c2

def test_sub():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = c2 - c1
    assert c3.radius == 1

def test_isub():
    c1 = Circle(1)
    c2 = Circle(2)
    c2 -= c1
    assert c2.radius == 1

def test_msub():
    c1 = Circle(1)
    c2 = Circle(2)
    c2 -= c1
    assert c1 == 2 - c2

def test_mul():
    c1 = Circle(3)
    c2 = Circle(4)
    c3 = c1 * c2
    assert c3.radius == 12
    assert c3 == 3 * c2

def test_imul():
    c1 = Circle(3)
    c1 *= 2
    assert c1.radius == 6

def test_rmul():
    c1 = Circle(3)
    c1 *= 2
    c2 = Circle(18)
    assert c2 == 3 * c1

def test_lt():
    c1 = Circle(1)
    c2 = Circle(2)
    assert c1 < c2

def test_gt():
    c1 = Circle(1)
    c2 = Circle(2)
    assert c2 > c1

def test_eq():
    c1 = Circle(1)
    assert c1 == Circle(1)

def test_neq():
    c1 = Circle(1)
    c2 = Circle(2)
    assert c1 != c2

def test_sort():
    l = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    l.sort(key=Circle.sort_key)
    assert l == [Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

