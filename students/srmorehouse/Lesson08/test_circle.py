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

def test_multiply():
    c1 = Circle(3)
    c2 = Circle(4)
    c3 = c1 * c2
    assert c3.radius == 12
    with pytest.raises(TypeError) as e:
        c3 = 3 * c2

