#!/usr/bin/env python3

"""
Created on Thu Apr 30 18:21:07 2020

@author: Clifford Butler

Test functions for circle.py classes/functions
"""

import circle

def test_circle():
    c = Circle(4)
    print("The radius is:", c.radius)
    assert c.radius == 4
    
if __name__ == "__main__":
    test_circle()
    print('Tests passed!!')