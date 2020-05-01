#!/usr/bin/env python3

"""
Created on Thu Apr 30 18:21:07 2020

@author: Clifford Butler

Test functions for circle.py classes/functions
"""

import circle
import pytest


def test_circle():
    # test if circle class is working
    c = Circle(8)
    assert c.radius == 8
    print("test_circle passed")
     
def test_diameter():
    #test if diameter() function is working
    c = Circle(1)
    assert c.radius == 1
    print("test_diameter passed")
    
def test_diameter2():
    #test if diameter2() function is working
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1
    print("test_diameter2 passed")
    
def test_area():
    # test if area() function is working  
    c = Circle(2)
    assert c.area == 12.5664
    print("test_area passed")
    
def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4
    print("test_from_diameter passed")
    
def test_add():
    # test if adding two circle variables adds the two circles together
    c1 = Circle(2)
    c2 = Circle(4)
    c = c1 + c2
    assert str(c) == 'A circle with the radius of: 6'
    print("test_add passed")
    
def test_mul():
    c = Circle(4)
    c1 = Circle(2)
    c2 = Circle(4)
    a = c1 * c2
    assert 'A circle with the radius of: 4' == str(c) 
    assert 'A circle with the radius of: 8' == str(a)      
    print("test_mult passed")
    
def test_str():
    # test the string output of a circle
    c = Circle(4)
    d = eval(repr(c))
    assert 'A circle with the radius of: 4' == str(d)
    print("test_str passed")
    
def test_repr():
    # test the string output of a circle
    c = Circle(7)
    d = repr(c)
    assert 'Circle(7)' == d
    print("test_repr passed")

def test_rmul():
    # test multiplying circle by a number
    c5 = (Circle(4))
    a = repr(c5 * 2)
    b = repr(2 * c5)
    assert 'Circle(8)' == a
    assert 'Circle(8)' == b
    print("test_mult2 passed")

def test_eg():
    # test multiplying circle by a number
    c5 = (Circle(4))
    a = repr(c5 * 2)
    b = repr(2 * c5)
    assert 'Circle(8)' == a
    assert 'Circle(8)' == b
    print("test_eg passed")

def test_lt():
    # test multiplying circle by a number
    c5 = (Circle(4))
    a = repr(c5 * 2)
    b = repr(2 * c5)
    assert 'Circle(8)' == a
    assert 'Circle(8)' == b
    print("test_lt passed")
    
if __name__ == "__main__":
    test_circle()
    test_diameter()
    test_diameter2()
    test_area()
    test_from_diameter()
    test_add()
    test_mul()
    test_str()
    test_repr()
    test_rmul()
    test_eg()
    test_lt()
    print("All tests passed!!")