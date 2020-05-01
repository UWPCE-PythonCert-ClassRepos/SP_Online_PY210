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
    
if __name__ == "__main__":
    test_circle()
    test_diameter()
    test_diameter2()
    test_area()
    test_from_diameter()
    print("All tests passed!!")