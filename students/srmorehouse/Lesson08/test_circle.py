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

