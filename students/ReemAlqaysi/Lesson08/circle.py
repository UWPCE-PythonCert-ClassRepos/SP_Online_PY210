#!/usr/bin/env python3

import math

"""Step 1:
Create class called Circle"""
class Circle(object):
    
    def __init__(self, radius): #Require parameters: Radius
        self.radius = radius

    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self, radius):
        self.radius = radius

"""Step 2:
Add a “diameter” property, so the user can get the diameter of the circle:"""
    @property
    def diameter(self):
        return self.radius * 2
"""Step 3:
Set up the diameter property so that the user can set the diameter of the circle:"""
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

"""Step 4:
Add an area property so the user can get the area of the circle:"""
    @property
    def area(self):
        return math.pow(self.radius, 2)*math.pi

"""Step 5:
Add an “alternate constructor” that lets the user create a Circle directly with the diameter:"""
    def from_diameter(self,diameter):
    	return self.radius = diameter/2

"""Step 6:
Every class should have a nice way to print it out…
Add __str__ and __repr__ methods to your Circle class."""
    def __str__(self):
        return "Circle with radius: {:.6d}".format(self.radius)

    def __repr__(self):
        return "Circle({:.0d})".format(self.radius)
