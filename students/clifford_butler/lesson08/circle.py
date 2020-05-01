#!/usr/bin/env python3

"""
Created on Thu Apr 30 18:21:07 2020

@author: Clifford Butler

Circle Class Exercise

Goal:
The goal is to create a class that represents a simple circle.

A Circle can be defined by either specifying the radius or the diameter, 
and the user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area.
Print the circle and get something nice.
Be able to add two circles together.
Be able to compare two circles to see which is bigger.
Be able to compare to see if they are are equal.
(follows from above) be able to put them in a list and sort them.

You will use:

properties.
a bunch of “magic methods”.
a classmethod.
"""
#import math

class Circle:
    '''a class to form circles'''
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14
    
c = Circle(8)    
print(c.area())
print(c.perimeter())


