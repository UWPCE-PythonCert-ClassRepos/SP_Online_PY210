#!/usr/bin/env python3

"""
Created on Thu Apr 30 18:21:07 2020

@author: Clifford Butler

Circle Class Exercise

Goal:
The goal is to create a class that represents a simple circle.

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
import math

class Circle(object):
    '''a class to form circles'''
    def __init__(self, radius):
        self.the_radius = radius
    
    @property    
    def radius(self):
        return self.the_radius
    
    @radius.setter
    def radius(self, value):
        self.the_radius = value 
        
    @property    
    def area(self):
        return round(math.pi * (self.the_radius ** 2), 4) 
    
    @property
    def perimeter(self):
        return 2 * self.the_radius * math.pi
    
    @property
    def diameter(self):
        return self.the_radius * 2

    @diameter.setter
    def diameter(self, value):
        self.the_radius = value / 2    
        
    @classmethod
    def from_diameter(a,diameter):
        # creates a circle from diameter
        return a(diameter/2)

    def __str__(self):
        return(f"A circle with the radius of: {self.the_radius}")    

    def __repr__(self):
        return (f"Circle({self.the_radius})")   
    
    def __add__(self, b):
        # adds two circles by radius
        new_radius = self.radius + b.radius
        return Circle(new_radius)     

    def __mul__(self, b):
        # mult a circle by radius
        try:
            mul_radius = self.radius * b.radius
        except(AttributeError):
            mul_radius = self.radius * b
        return Circle(mul_radius) 
    
    def __rmul__(self, b):
        # mult a circle by radius
        try:
            mul2_radius = b.radius * self.radius 
        except(AttributeError):
            mul2_radius = b * self.radius
        return Circle(mul2_radius)     

    def __eg__(self, b):
        return self.radius == b.radius

    def __lt__(self, b):
        return self.radius < b.radius    

class Sphere(Circle):
    '''a sub class to form spheres'''
    
    def __str__(self):
        return (f"A sphere with the radius of: {self.radius}")
    
    def __repr__(self):
        return (f"Sphere({self.radius})")

    @property
    def volume(self):
        return 4 / 3 * math.pi * self.radius ** 3

    @property
    def area(self):
        return 4 * math.pi * self.radius ** 2 