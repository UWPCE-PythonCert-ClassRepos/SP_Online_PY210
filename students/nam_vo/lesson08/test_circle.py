"""
test code for cicle.py
"""

import io
import pytest
import math

from circle import *

########
# Step 1
########

def test_init():
    c = Circle(4)
    print(f"c.radius = {c.radius}")
    assert(c.radius) == 4
    # assert False

########
# Step 2
########

def test_diameter_property():
    c = Circle(4)
    print(f"c.diameter = {c.diameter}")
    assert(c.radius) == 4
    assert(c.diameter) == 8
    # assert False

########
# Step 3
########

def test_diameter_setter():
    c = Circle(4)
    c.diameter = 2
    print(f"c.radius = {c.radius}")
    print(f"c.diameter = {c.diameter}")
    assert(c.radius) == 1
    assert(c.diameter) == 2
    # assert False

########
# Step 4
########

def test_area_property():
    c = Circle(2)
    print(f"c.radius = {c.radius}")
    print(f"c.diameter = {c.diameter}")
    print(f"c.area = {c.area}")
    assert(c.radius) == 2
    assert(c.diameter) == 4
    assert(c.area) == math.pi * math.pow(c.radius, 2)

    with pytest.raises(AttributeError):
        c.area = 42
    # assert False

########
# Step 5
########

def test_init_with_diameter():
    c = Circle.from_diameter(8)
    print(f"c.diameter = {c.diameter}")
    print(f"c.radius = {c.radius}")
    assert(c.diameter) == 8
    assert(c.radius) == 4
    # assert False

########
# Step 6
########

def test_circle_print():
    c = Circle(4)
    print(f"c = {c}")
    assert(c.__str__() == 'Circle with radius: 4.000000')
    repr(c)
    print(f"repr(c) = {repr(c)}")
    assert(repr(c)) == 'Circle(4)'
    d = eval(repr(c))
    print(f"d = {d}")
    # assert False

########
# Step 7
########

def test_circle_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c = c1 + c2
    print(f"c1 = {c1}")
    print(f"c2 = {c2}")
    print(f"c = {c}")
    print(f"c.radius = {c.radius}")
    print(f"c.diameter = {c.diameter}")
    assert(type(c)) == Circle
    assert(c.radius) == 6
    assert(c.diameter) == 12
    # assert False

def test_circle_multiply():
    c2 = Circle(4)
    c = c2 * 3
    print(f"c = {c}")
    print(f"c.radius = {c.radius}")
    print(f"c.diameter = {c.diameter}")
    assert(type(c)) == Circle
    assert(c.radius) == 12
    assert(c.diameter) == 24

    c = 3 * c2
    print(f"c = {c}")
    print(f"c.radius = {c.radius}")
    print(f"c.diameter = {c.diameter}")
    assert(type(c)) == Circle
    assert(c.radius) == 12
    assert(c.diameter) == 24

    # assert False

########
# Step 8
########

def test_circle_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    print(f"c1 = {c1}")
    print(f"c2 = {c2}")
    print(f"c1 < c2 is {c1 < c2}")
    print(f"c1 == c2 is {c1 == c2}")
    assert(c1 > c2) == False
    assert(c1 < c2) == True
    assert(c1 == c2) == False
    
    # assert False

def test_circle_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    print(f"circles = {circles}")
    circles.sort()
    print(f"sorted_circles = {circles}")
    assert(circles) == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

    # assert False

def test_extra_compare():
    c = Circle(2)
    print(f"c * 3 == 3 * c is {c * 3 == 3 * c}")
    assert(c * 3 == 3 * c) == True

    # assert False

########
# Step 9
########

def test_sphere_init():
    s = Sphere(4)
    print(f"s = {s}")
    assert(s.__str__() == 'Sphere with radius: 4.000000')
    print(f"repr(s) = {repr(s)}")
    assert(repr(s)) == 'Sphere(4)'

    # assert False

def test_sphere_volume():
    s = Sphere(2)
    print(f"s = {s}")
    print(f"s.radius = {s.radius}")
    print(f"s.volume = {s.volume}")
    assert(s.volume) == 4/3 * math.pi * math.pow(s.radius, 3)

    # assert False

def test_sphere_area():
    s = Sphere(2)
    print(f"s = {s}")
    print(f"s.radius = {s.radius}")
    with pytest.raises(NotImplementedError):
        print(f"s.area = {s.area}")

    # assert False
    
def test_sphere_from_diameter():
    s = Sphere.from_diameter(8)
    print(f"s = {s}")
    print(f"s.diameter = {s.diameter}")
    print(f"s.radius = {s.radius}")
    assert(s.diameter) == 8
    assert(s.radius) == 4

    # assert False
    