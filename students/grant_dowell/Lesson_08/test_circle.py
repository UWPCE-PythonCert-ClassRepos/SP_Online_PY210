# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 20:13:36 2020

@author: travel_laptop
"""
import math
import unittest as ut
from circle import *

def test_properties():
    c = Circle(10)
    assert c.radius == 10
    assert c.diameter == 20
    print(c.area)
    assert c.area == math.pi * 100
    
    c.diameter = 6
    assert c.radius == 3
    
def test_diameter_init():
    c = Circle.from_diameter(8)
    assert c.radius == 4
    
def test_print():
    c = Circle(6)
    print(c)
    assert str(c) == 'Circle with radius: 6.000000'
    assert repr(c) == "Circle(6.00)"
    
def test_math():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    print(c3)
    assert c3.radius == 6
    
    c4 = c1 * 3
    print(c4)
    assert c4.radius == 6
    
def test_compares():
    c1 = Circle(2)
    c2 = Circle(4)
    
    assert (c1 > c2) is False
    assert c1 < c2
    assert (c1 == c2) is False
    
    c3 = Circle(4)
    assert c2 == c3
    
def test_sort():
    circles = [Circle(6), Circle(7), Circle(2), Circle(1)]
    sorted_circles = [Circle(1), Circle(2), Circle(6), Circle(7)]
    circles.sort()
    assert circles == sorted_circles