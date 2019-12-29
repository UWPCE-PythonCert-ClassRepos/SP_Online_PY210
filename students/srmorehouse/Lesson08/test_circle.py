#!/usr/bin/env python3

import pytest
from circle import Circle

def test_happy_assign():
    c = Circle(1)
    assert c.radius == 1

def test_unhappy_assign_zero():
    with pytest.raises(ValueError) as e:
        c = Circle(0)

def test_unhappy_assign_neg():
    with pytest.raises(ValueError) as e:
        c = Circle(-1)

