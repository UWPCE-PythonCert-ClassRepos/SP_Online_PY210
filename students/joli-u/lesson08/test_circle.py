import pytest
from circle import *
from math import pi

"""
joli umetsu
lesson 08
test code for circle.py
py210
"""

### STEP 1
def test_circle_init():
    c = Circle(4)
    assert c.radius == 4

### STEP 2
def test_circle_diameter():
    c = Circle(4)
    assert c.diameter == 8
    
### STEP 3
def test_circle_set_diameter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1
    
### STEP 4
def test_circle_area():
    c = Circle(2)
    assert c.area == (pi*2**2)
    
### STEP 5
def test_circle_alt_constr():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4
    
### STEP 6
def test_circle_print():
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4.000000'
    assert repr(c) == 'Circle(4)'
    assert eval(repr(c)) == Circle(4)
    
### STEP 7
def test_circle_num_protocol():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)
    assert c2 * 3 == Circle(12)
    
### STEP 8
def test_circle_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert (c1 > c2) is False
    assert (c1 < c2) is True
    assert (c1 == c2) is False
    assert (c2 == c3) is True
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

### STEP 9
def test_sphere_print():
    s = Sphere(5)
    assert str(s) == 'Sphere with radius: 5.000000'
    assert repr(s) == 'Sphere(5)'
    assert eval(repr(s)) == Sphere(5)
    
def test_sphere_volume():
    s = Sphere(5)
    assert s.volume == (4/3*pi*5**3)
    
def test_sphere_alt_constr():
    s = Sphere.from_diameter(8)
    assert s.diameter == 8
    assert s.radius == 4

def test_sphere_area():
    s = Sphere(3)
    assert s.area == (4*pi*(3**2))
    