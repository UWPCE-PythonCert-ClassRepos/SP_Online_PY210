#!/usr/bin/env python3

"""
Created on Thu Apr 30 18:21:07 2020

@author: Clifford Butler

Test functions for circle.py classes/functions
"""

import circle as co

def test_circle():
    assert circle(4) == 4
    

if __name__ == "__main__":
    test_circle()
    print('Tests passed!!')