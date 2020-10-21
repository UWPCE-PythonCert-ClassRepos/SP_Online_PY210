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
    #assert print(c) == 'Circle with radius: 4.0000'
    assert repr(c) == 'Circle(4)'

    d = eval(repr(c))

    assert d == Circle(4)