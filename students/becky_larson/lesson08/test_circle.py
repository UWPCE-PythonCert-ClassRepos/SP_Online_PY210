"""
test code for circle.py

"""

import pytest
from circle import *


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
    print(f'circle radius is:  {c.radius}')
    assert c.radius == 4
    
# Step 2

def test_diamter_get():
    c = Circle(4)
    print(f'circle diameter is:  {c.diameter}')
    assert c.diameter == 8

# Step 3

def test_diamter_set():
    c = Circle(4)
    c.diameter = 2
    print(f'circle diameter is:  {c.diameter}')
    assert c.diameter == 2
    assert c.radius == 1

# Step 4

def test_area_get():
    c = Circle(2)
    print(f'circle area is:  {c.area}')
    assert c.area > 12
    assert c.radius < 13

# Step 5

def test_from_diamter_set():
    c = Circle.from_diameter(8)
    print(f'circle radius is:  {c.radius}')
    print(f'circle diameter is:  {c.diameter}')
    assert c.diameter == 8
    assert c.radius == 4

# Step 6

def test_print():
    c = Circle(4)
    temp_1 = print(c)
    print(f'****************************** temp_1 is:  {temp_1}')
    assert False

def test_repr():
    c = Circle(4)
    temp_2 =repr(c)
    print(f'****************************** temp_2 is:  {temp_2}')
    assert False

# Step 7

# Step 8

# Step 8 optional

# Step 9






    