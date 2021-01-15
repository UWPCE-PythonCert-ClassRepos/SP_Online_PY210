#!/usr/bin/env python3
#Craig Simmons
# Python 210
# Lesson08 Asignment - pytest unit tests
# Created 01/14/2021 - csimmons

import io
import pytest
from math import pi
from circleclass import *

# Tests instantiation -also verifies that radius was passed

def test_init():
    c = Circle(5)
    assert c.radius == 5
    
def test_diameter_property():
    c = Circle(5)
    assert c.diameter == 10

def test_diameter_setter():
    c = Circle(8)
    assert c.diameter == 16
    assert c.radius == 8
    c.radius = 10
    assert c.diameter == 20 
    assert c.radius == 10
    c.diameter = 10
    assert c.diameter == 10 
    assert c.radius == 5

def test_area_property():
    c = Circle(5)
    assert c.area == (pi * 25)
    try:
        c.area = 100
    except AttributeError as error:
        print('c.area is ' + str(c.area))
    c.radius = 10
    assert c.area == (pi * 100)
    c.diameter = 6
    assert c.area == (pi * 9)

def test_from_diameter():
    c = Circle(5)
    c.diameter = 20
    assert c.radius == 10
    c.radius = 10
    assert c.diameter == 20

def test_dunder_str():
    c = Circle(5)
    print(str(c))
    assert str(c) == 'Circle with radius: 5.00'

def test_dunder_repr():
    c = Circle(5)
    print(str(c))
    assert repr(c) == 'Circle(5)'

def test_dunder_add():
    c = Circle(5)
    c2 = Circle(10)
    assert c.radius + c2.radius == 15

def test_dunder_mul():
    c = Circle(5)
    assert c.radius * 6 == 30
    assert 6 * c.radius == 30

def test_dunder_rmul():
    c = Circle(5)
    assert 6 * c.radius == 30
    assert c.radius * 6 == 30