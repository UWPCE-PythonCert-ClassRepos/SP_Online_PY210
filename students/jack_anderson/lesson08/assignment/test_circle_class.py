#!/usr/bin/env python3

import pytest
import math

from circle_class import *


##########
# STEP 1
##########
def test_radius_float():
    c = Circle(4.34)
    print(c.radius)
    assert c.radius == 4.34

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
    with pytest.raises(TypeError):
        c = Circle("test")
        print(c.radius)

    # assert False
    # assert False

##########
# STEP 2
##########

def test_diameter():
    c = Circle(4)
    print(c.diameter)

    assert c.diameter == 8

    # assert False
    # assert False

def test_diameter_w_float():
    c = Circle(4.93)
    print(c.diameter)

    assert c.diameter == 9.86

##########
# STEP 3
##########

def test_diameter_property():
    c = Circle(8)
    c.diameter = 4
    print(c.diameter , c.radius)
    assert c.diameter == 4
    assert c.radius == 2

    # assert False
    # assert False


##########
# STEP 4
##########

def test_area():
    c = Circle(4)
    print(c.area)
    assert c.area == 50.265

    # assert False
    # assert False

def test_area_pi():
    c = Circle(1)
    print(c.area)
    assert c.area == 3.142

    # assert False
    # assert False

def test_area_edit():
    with pytest.raises(AttributeError):
        c = Circle(1)
        c.area = 20

    # assert False
    # assert False


##########
# STEP 5
##########

def test_alt_contructor():
    c = Circle.from_diameter(8)
    assert c.diameter == 32
    assert c.radius == 16

    # assert False
    # assert False


##########
# STEP 6
##########

def test_str():
    c = Circle(8)
    assert c.__str__() == "Circle with radius: 8"

    # assert False
    # assert False

def test_repr():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'

    # assert False
    # assert False

def test_eval():
    c = Circle(4)
    c2 = eval(repr(c))
    assert c2.radius == 4

    # assert False
    # assert False

##########
# STEP 7
##########

def test_add():
    c = Circle(2)
    c2 = Circle(4)
    x = c + c2
    y = x + c
    assert x.radius == 6
    assert y.radius == 8

    # assert False
    # assert False

def test_multiply():
    c = Circle(4)
    c2 = c * 4
    print(c2)
    assert c2.radius == 16
    c *= 3
    assert c.radius == 12

    # assert False
    # assert False

##########
# STEP 8-1
##########

def test_compare_lt_gt_eq():
    c = Circle(6)
    c2 = Circle(2)
    c3 = Circle(4)
    c4 = c2 + c3
    assert c != c2
    assert c > c3 > c2
    assert c3 < c
    assert c < (c2 + c3 + c4)
    assert c == c4
    assert c4.radius == c.radius

    # assert False
    # assert False

def test_sort():
    circles = [Circle(4), Circle(2), Circle(3), Circle(6), Circle(1), Circle(5)]
    circles.sort()
    print(circles)
    assert circles == [Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6)]

    # assert False
    # assert False



##########
# STEP 8-2
##########

def test_subtract():
    c1 = Circle(10)
    c2 = c1 - 1
    print(c2)

    assert c2.radius == 9

    c1 -= 7
    print(c1)
    assert c1.radius == 3



def test_true_div():
    c1 = Circle(4)
    c2 = Circle(2)
    c3 = c1 / c2
    print(c3)

    assert c3.radius == 2

def test_floor_div():
    c1 = Circle(16)
    c2 = Circle(4)
    c3 = c1 // c2
    print(c3)
    assert c3.radius == 4

    # assert False
    # assert False

def test_reflected_mul():
    c = Circle(2)
    assert c * 3 == 3 * c

    # assert False
    # assert False

def test_reflected_add():
    c1 = Circle(5)
    c2 = Circle(3)
    assert c1 + c2 == c2 + c1


def test_augmented_mul():
    c = Circle(2)
    c2 = Circle(10)
    c *= 20
    assert c.radius == 40


