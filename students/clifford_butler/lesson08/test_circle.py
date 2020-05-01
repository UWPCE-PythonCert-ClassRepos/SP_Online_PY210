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
    c1 = Circle(2)
    c2 = Circle(4)
    a = (c1 + c2)
    g = eval(repr(Circle(6)))
    print (g)
    print(a)
    print('Circle(6)')
    assert str(a) == 'Circle(6)'  
    print("test_add passed")
    
def test_mult():
    c1 = Circle(2)
    c2 = Circle(4)
    a = (c1 * c2)
    assert (Circle(8)) == a  
    print("test_mult passed")
    
def test_str():
    # test the string output of a circle
    c = Circle(7)
    d = eval(repr(c))
    print(c)
    print(d)
    text = "Circle(7)"
    assert 'Circle(7)' == str(d)
    assert text != d    
    
if __name__ == "__main__":
    test_circle()
    test_diameter()
    test_diameter2()
    test_area()
    test_from_diameter()
    test_add()
    test_str()
    print("All tests passed!!")