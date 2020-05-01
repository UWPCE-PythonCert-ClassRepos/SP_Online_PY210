#!/usr/bin/env python3

"""
Created on Thu Apr 30 18:21:07 2020

@author: Clifford Butler

Test functions for circle.py classes/functions
"""

import circle

def test_circle():
    assert c.area() == 200.96
    assert c.perimeter() == 50.24
    
if __name__ == "__main__":
    test_circle()
    print('Tests passed!!')