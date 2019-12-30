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

