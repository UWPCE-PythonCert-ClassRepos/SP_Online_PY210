#!/usr/bin/env python3

"""
Classed based circles!.
"""
import math

class Circle(object):
    def __init__(self, radius = 1, **kwargs):
        self.radius = radius
        
    @classmethod
    def from_diameter(cls, diameter):
        self = cls()
        self.radius = diameter / 2
        return self
    
    @property 
    def diameter(self):
        return self.radius * 2
    
    @property 
    def area(self):
        return math.pi * self.radius ** 2

    @diameter.setter
    def diameter(self, diameter):
        """Set the diameter"""
        self.radius = diameter / 2
        
    def __repr__(self):
        return "Circle({})".format(self.radius)
    
    def __str__(self):
        return "Circle with radius: {}".format(self.radius)
        
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    
    def __rmul__(self, other):
        try:
            return Circle(self.radius * other)
        except:
            try:
                return Circle(radius * other)
            except:
                return "Not Implemented"
        
    def __mul__(self, other):
        try:
            return Circle(self.radius * other)
        except:
            try:
                return Circle(radius * other)
            except:
                return "Not Implemented"

    
    def  __lt__(self, other):
        return (self.radius < other.radius)
    
    def  __gt__(self, other):
        return (self.radius > other.radius)
    
    def __eq__(self, other):
        return (self.radius == other.radius)
    
    
class Sphere(Circle):
    
    def __repr__(self):
        return "Sphere({})".format(self.radius)
    
    def __str__(self):
        return "Sphere with radius: {}".format(self.radius)
    
    def volume(self):
        return  (4/3) * math.pi * self.radius ** 3
        
    def surfuce_area(self):
        return 4 * math.pi * self.radius ** 2
        

