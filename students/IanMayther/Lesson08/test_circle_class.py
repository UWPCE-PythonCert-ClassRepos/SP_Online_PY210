"""
test code for circle_class.py

This is just a start -- you will need more tests!
"""

import io
import pytest
import math

# import * is often bad form, but makes it easier to test everything in a module.
from circle_class import *

########
# Step 1
########

def test_circle():
    with pytest.raises(AttributeError):
        c = Circle()

def test_radius():
    c = Circle(4)

    assert c.radius == 4

########
# Step 2
########

def test_diameter():
    c = Circle(4)

    assert c.diameter == 8

########
# Step 3
########

def test_dia_rad():
    c = Circle(8)

    assert c.radius == 8
    assert c.diameter == 16

    c.diameter = 8

    assert c.radius == 4
    assert c.diameter == 8

########
# Step 4
########

def test_area_calc():
    c = Circle(2)
    
    assert c.area == 12.566370

def test_area_set():
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 42

########
# Step 5
########

def test_class_method():
    c = Circle.from_diameter(8)

    assert c.diameter == 8
    assert c.radius == 4


########
# Step 6
########

def test_printing():
    c = Circle(4)

    assert str(c) == 'Circle with radius: 4.0000'
    assert repr(c) == 'Circle(4)'

########
# Step 7
########

def test_circle_add():
    '''Testing math functions'''
    c1 = Circle(2)
    c2 = Circle(4)

    assert Circle(6) == Circle(6)
    assert c1 + c2 == Circle(6)
    assert c1 * c2 == Circle(8)
    assert c2 * 3 == Circle(12)
    assert 3 * c2 == Circle(12)
    assert 3 * c2 == c2 * 3

########
# Step 8
########

def test_comparability():
    '''Testing if comparing functions'''
    c1 = Circle(2)
    c2 = Circle(4)

    assert not c1 > c2
    assert c1 < c2
    assert not c1 == c2

    c3 = Circle(4)

    assert c2 == c3

def test_circle_list():
    '''Testing sort function'''
    c1 = Circle(1)
    c2 = Circle(2)
    c5 = Circle(5)
    circles = [c2, c1, c5]
    circles.sort()

    assert circles == [Circle(1), Circle(2), Circle(5)]

########
# Step 9
########

'''Sphere testing'''
def test_sphere():
    with pytest.raises(AttributeError):
        s = Sphere()

def test_sphere_radius():
    s = Sphere(4)

    assert s.radius == 4

def test_sphere_diameter():
    s = Sphere(4)

    assert s.diameter == 8

def test_volume():
    s = Sphere(1)

    assert s.volume == (4/3) * math.pi

def test_surface_area():
    s = Sphere(2)
    
    assert s.area == 4 * math.pi * 4

def test_sphere_dunder():
    s = Sphere(4)

    assert str(s) == 'Sphere with radius: 4.0000'
    assert repr(s) == 'Sphere(4)'