#!/usr/bin/env python3

import pytest

from circle_class import *



def test_radius_float():
    c = Circle(4.342)
    print(c.radius)
    assert c.radius == 4.342

    # assert False
    # assert False

def test_radius_int():
    c = Circle(10)
    print(c.radius)
    assert c.radius == 10

    # assert False
    # assert False

def test_radius_neg_num():
    with pytest.raises(ValueError):
        c = Circle(-5)
        print(c.radius)
        assert c.radius == "Must use a positive interger"

def test_radius_string():
    with pytest.raises(ValueError):
        c = Circle("test")
        print(c.radius)

    # assert False
    # assert False

def test_diameter():
    c = Circle(4)
    print(c.diameter)

    assert c.diameter == 8

    # assert False
    # assert False

def test_diameter_w_float():
    c = Circle(4.935)
    print(c.diameter)

    assert c.diameter == 9.87
