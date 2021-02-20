#!/usr/bin/env python3
"""
Created on Sun Jan 10 16:02:44 2021

@author: johnh
"""

# Callable Example

class Quadratic():
    
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c