#!/usr/bin/env python3

import pytest
import math
from circle import Circle, Sphere

def radius_test():
    c = Circle(5)
    assert c.radius == 5
    
def diameter_test():
    c = Circle(5)
    assert c.diameter == 5 * 2

def user_diameter_set_test():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

def area_test():
    c = Circle(2)
    assert c.area == math.pi * 2 ** 2 
    
def alt_constuctor_test():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4
    
def print_test():
     c = Circle(4)
     assert c.__str__() == 'Circle with radius: 4'
     assert repr(c) == 'Circle(4)'
     
def numeric_protocol():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)
    assert c2 * 3 == Circle(12)
    
def compare_test():
    c1 = Circle(2)
    c2 = Circle(4)
    assert not(c1 > c2)
    assert c1 < c2
    assert not(c1 == c2)
    c3 = Circle(4)
    assert c3 == c2
    
def sphere_test():
    s = Sphere(2)
    assert s.volume()  == (4/3) * math.pi * 2 ** 3
    assert s.surfuce_area() == 4 * math.pi * 2 ** 2
    
