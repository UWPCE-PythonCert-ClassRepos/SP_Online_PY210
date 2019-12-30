#!/usr/bin/env python3

import math
import pytest
from circle import Circle

def test_set_assign():
    c = Circle(1)
    assert c.radius == 1

def test_unhappy_set_zero():
    with pytest.raises(ValueError) as e:
        c = Circle(0)

def test_unhappy_set_neg():
    with pytest.raises(ValueError) as e:
        c = Circle(-1)

def test_set_diameter():
    radius = 1
    c = Circle(radius)
    c.diameter = radius * math.pi
    assert c.diameter == radius * math.pi

def test_get_area():
    radius = 1
    c = Circle(radius)
    assert c.area == pytest.approx (3.14,0.1)

    radius = 2
    c = Circle(radius)
    assert c.area == pytest.approx (12.56,0.1)

def test_unhappy_set_area():
    c = Circle(1)
    with pytest.raises(AttributeError) as e:
        c.area = 1

