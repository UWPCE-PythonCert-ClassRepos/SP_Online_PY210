#!/usr/bin/env python

from math import pi

"""
joli umetsu
lesson 08
circle class exercise
py210
"""

"""
class that represents a simple circle, allowing definition by radius or diameter and querying.
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    @property
    def diameter(self):  # diameter property
        return 2*self.radius
        
    @property
    def area(self):  # area property
        return pi*self.radius**2
    
    @diameter.setter
    def diameter(self, value):  # optional diameter setter
        self.radius = value/2
        
    @classmethod
    def from_diameter(cls, value):  # alternate constructor
        return cls(value/2)
        
    def __str__(self):
        return f"Circle with radius: {self.radius:.6f}"
    
    def __repr__(self):
        return "Circle({})".format(self.radius)
        
    def __add__(self, other):  # add two circles
        return Circle(self.radius + other.radius)
        
    def __mul__(self, mult):  # multiply circle by a number
        return Circle(self.radius * mult)
        
    def __eq__(self, other):  # compare two circles - equal
        return (self.radius == other.radius)      
        
    def __lt__(self, other):  # compare two circles - less than
        return (self.radius < other.radius)      


class Sphere(Circle):
    def __str__(self):
        return f"Sphere with radius: {self.radius:.6f}"
    
    def __repr__(self):
        return "Sphere({})".format(self.radius)
        
    @property
    def volume(self):  # volume property
        return (4/3)*pi*self.radius**3
        
    @property
    def area(self):  # surface area property
        return 4*pi*self.radius**2