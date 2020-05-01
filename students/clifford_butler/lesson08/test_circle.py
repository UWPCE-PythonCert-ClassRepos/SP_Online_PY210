#!/usr/bin/env python3

"""
Created on Thu Apr 30 18:21:07 2020

@author: Clifford Butler

Test functions for circle.py classes/functions
"""

import circle
import pytest


def test_circle():
    # test circle class is working
    c = Circle(8)
    assert c.radius == 8
    print("test_circle passed")
     
def test_diameter():
    #test diameter() function is working
    c = Circle(1)
    assert c.radius == 1
    print("test_diameter passed")
    
def test_diameter2():
    ''' test diameter2() function is working'''
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 4
    print("test_diameter2 passed")
    
if __name__ == "__main__":
    test_circle()
    test_diameter()
    test_diameter2()
    
    print('All tests passed!!')