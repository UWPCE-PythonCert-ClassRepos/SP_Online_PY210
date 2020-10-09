"""
test code for circle.py
Becky Larson 10/1/2020

"""

import pytest
from circle import *
import random
import math


# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.
def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = io.StringIO()
    # this so the tests will work before we tackle indentation
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    return outfile.getvalue()

# Step 1

def test_radius():
    c = Circle(4)
    assert c.radius == 4
    
# Step 2

def test_diamter_get():
    c = Circle(4)
    assert c.diameter == 8

# Step 3

def test_diamter_set():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

# Step 4

def test_area_get():
    c = Circle(2)
    assert c.area > 12
    assert c.radius < 13

# Step 5

def test_from_diamter_set():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

# Step 6
"""
def test_print():
    c = Circle(4)
    temp_1 = print(c)

def test_repr():
    c = Circle(4)
    temp_2 =repr(c)

"""

# Step 7
def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert c3.radius == 6
#    assert False

def test_mul():
    c1 = Circle(4)
    c2 = Circle(6)
    c3 = c1*c2
    assert c3.radius == 24

    c4 = c1*7
    assert c4.radius == 28

def test_rmul():
    c = Circle(4)
    c1= 2*c
    assert c1.radius == 8

    c2 = Circle(9)
    c2= c*c2
    assert c2.radius == 36


# Step 8
def test_gt():
    c1 = Circle(4)
    c2 = Circle(6)
    result = c1 > c2
    assert result == False

    result = c2 > c1
    assert result == True

def test_lt():
    c1 = Circle(4)
    c2 = Circle(6)
    result = c1 < c2
    assert result == True

    result = c2 < c1
    assert result == False

def test_eq():
    c1 = Circle(4)
    c2 = Circle(6)
    result = c1 == c2
    assert result == False
"""
the results look the same but do not assert
def test_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()

    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
#                     [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
"""    

# Step 8 optional

def test_iadd():
    c = Circle(4)
    c += Circle(5)
    assert c.radius == 9

def test_eq():
    a_circle = Circle(4)
    result = a_circle * 3 == 3 * a_circle
    assert  result == True

def test_imul():
    a_circle = Circle(4)
    a_circle *= Circle(2)
    assert a_circle.radius == 8
    a_circle *= 2
    assert a_circle.radius == 16


# Step 9
def test_sphere_area():
    r = 3
    sphere = Sphere(r)
    assert sphere.area == 4*math.pi*r*r

def test_sphere_volume():
    r = 7
    sphere = Sphere(r)
    assert sphere.volume == 4/3*math.pi*r*r*r
#    assert False

    