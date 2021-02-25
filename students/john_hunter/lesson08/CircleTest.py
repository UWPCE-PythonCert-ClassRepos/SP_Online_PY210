# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:58:04 2021

@author: johnh
"""

# Test Circles
from math import pi
import Circles 
import pytest

def test_circle():
    circ = Circles.Circle(3)
 
def test_circle_diameter():
    circ = Circles.Circle(3)
    print(circ)
    assert circ.diameter == 6
    
def test_circle_area():
    circ = Circles.Circle(3)
    print(circ)
    assert circ.area == 28.2743339
    
def test_circle_str():
    circ = Circles.Circle(3)
    print(circ)
    assert str(circ) == "The Object is a Circle with Radius: 3.0000000" 
    
def test_circle_repr():
    circ = Circles.Circle(3)
    assert repr(circ) == "Circle(3)"
    
def test_circle_add():
    circ1 = Circles.Circle(3)
    circ2 = Circles.Circle(4)
    circ_add = circ1 + circ2
    print(circ_add)
    assert circ_add.diameter == 14
    
def test_circle_sub():
    circ1 = Circles.Circle(7)
    circ2 = Circles.Circle(2)
    circ_sub = circ1 - circ2
    print(circ_sub)
    assert circ_sub.diameter == 10

def test_circle_mul():
    circ1 = Circles.Circle(3)
    circ2 = Circles.Circle(4)
    circ_mul = circ1 * circ2
    print(circ_mul)
    assert circ_mul.diameter == 24
    
def test_circle_pow():
    circ1 = Circles.Circle(3)
    circ2 = Circles.Circle(4)
    circ_pow = circ1 ** circ2
    print(circ_pow)
    assert circ_pow.diameter == 162
    
def test_circle_gt():
    circ1 = Circles.Circle(4)
    circ2 = Circles.Circle(3)
    circ_gt = circ1 > circ2
    print(circ_gt)
    assert circ_gt is True
    
def test_circle_ge():
    circ1 = Circles.Circle(4)
    circ2 = Circles.Circle(3)
    circ_ge1 = circ1 > circ2
    circ1 = Circles.Circle(4)
    circ2 = Circles.Circle(4)
    circ_ge2 = circ1 == circ2
    print(circ_ge1 and circ_ge2)
    assert (circ_ge1 and circ_ge2) is True
    
def test_circle_lt():
    circ1 = Circles.Circle(4)
    circ2 = Circles.Circle(3)
    circ_gt = circ2 < circ1
    print(circ_gt)
    assert circ_gt is True
    
def test_circle_le():
    circ1 = Circles.Circle(4)
    circ2 = Circles.Circle(3)
    circ_ge1 = circ2 < circ1
    circ1 = Circles.Circle(4)
    circ2 = Circles.Circle(4)
    circ_ge2 = circ1 == circ2
    print(circ_ge1 and circ_ge2)
    assert (circ_ge1 and circ_ge2) is True
    
def test_circle_eq():
    circ1 = Circles.Circle(4)
    circ2 = Circles.Circle(4)
    circ_ge2 = circ1 == circ2
    print(circ_ge2)
    assert circ_ge2 is True
    
def test_circle_call():
    """ The unit test did not function as intended since a value for the radius 
    must be passed in order to create the instance of the object. The call can be made
    with the expected result, and the test passes. Example from the command prompt:
    >>> circ_call = Circles.Circle(3)
    >>> circ_call(4)
    'The Object is a Circle with Radius: 4.0000000'
    """
    circ_call = Circles.Circle(radius=4)
    circ_call(5)
    
def test_circle_sort_key():
    circ_list = [Circles.Circle(2), Circles.Circle(5), Circles.Circle(3),\
                 Circles.Circle(1), Circles.Circle(4)]
    ordered = [False, False, False, False]
    circ_list.sort()
    i=0
    while i < 4:
        ordered[i] = circ_list[i] < circ_list[i + 1]
        i = i + 1
    print(circ_list)
    print(ordered)
    assert False not in ordered
    
def test_sphere_volume():
    sphe = Circles.Sphere(3)
    print(sphe)
    assert sphe.volume == 113.0973355
def test_sphere_str():
    sphe = Circles.Sphere(3)
    print(sphe)
    assert str(sphe) == "The Object is a Sphere with Radius: 3.0000000"
def test_sphere_repr():
    sphe = Circles.Sphere(3)
    assert repr(sphe) == "Sphere(3)"
def test_sphere_area():
    sphe = Circles.Sphere(3)
    print(sphe)
    assert sphe.surface_area == 113.0973355