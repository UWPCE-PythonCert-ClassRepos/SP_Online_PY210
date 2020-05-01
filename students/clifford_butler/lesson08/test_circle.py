#!/usr/bin/env python3

"""
Created on Thu Apr 30 18:21:07 2020

@author: Clifford Butler

Test functions for circle.py classes/functions
"""

import circle

def test_circle():
    ''' test circle class is working'''
    c = Circle(8)
    print("test_circle passed")
    assert c.radius == 8
    
def test_diameter():
    ''' test diameter() function is working'''
    c = Circle(1)
    print ("c.radius = ",c.radius)
    print ("c.diameter =",c.diameter())
    assert c.radius == 1
    
if __name__ == "__main__":
    test_circle()
    test_diameter()
    print('Tests passed!!')