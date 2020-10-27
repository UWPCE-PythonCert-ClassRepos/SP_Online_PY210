#!/usr/bin/env python3

import pytest

from circle import *

# testing circle class

##########
# Step 1 #
##########

def test_radius():
    c = Circle(2)
    assert c.radius == 2

##########
# Step 2 #
##########

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

##########
# Step 3 #
##########

def test_diameter_setter():
    c = Circle(4)
    c.diamter = 2
    assert c.diamter == 2
    assert c.radius == 1

##########
# Step 4 #
##########

def test_area():
    c = Circle(2)
    assert round(c.area, 2) == 12.57

def test_area_attribute_error():
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 2 

##########
# Step 5 #
##########

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

##########
# Step 6 #
##########

def test_str():
    c = Circle(4)
    assert str(c) == 'Circle with a radius of 4'

def test_repr():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'

##########
# Step 7 #
##########

def test__add__():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert repr(c3) == 'Circle(6)'

def test_mul():
    c1 = Circle(4)
    c2 = c1 * 3
    repr(c2)
    assert repr(c2) == 'Circle(12)'

##########
# Step 8 #
##########

def test_comparisons():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(2)

    assert c1 < c2
    assert c1 <= c2
    assert c1 == c3
    assert c2 >= c3
    assert c2 > c3
    assert c2 != c3

##########
# Step 9 #
##########

def test_str_sphere():
    s = Sphere(4)
    assert str(s) == 'Sphere with a radius of 4'

def test_repr_sphere():
    s = Sphere(4)
    assert repr(s) == 'Sphere(4)'

def test_volume_sphere():
    s = Sphere(4)
    assert round(s.volume, 2) == 268.08

def test_area_sphere():
    s = Sphere(4)
    assert round(s.area, 2) == 201.06

