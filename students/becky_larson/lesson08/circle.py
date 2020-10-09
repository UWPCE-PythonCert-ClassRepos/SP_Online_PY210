#!/usr/bin/env python3
import math

"""
Becky Larson 10/1/2020
"""

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius*2
        
    @diameter.setter 
    def diameter(self, d): 
        self.radius = d/2 

    @property
    def area(self):
        return self.radius*self.radius*math.pi
        
    @classmethod
    def from_diameter(cls,d):
        return cls(d/2)

    def __str__(self):
       return f'Circle with radius: {self.radius:.6f}' 

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self,other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __mul__(self,other):
        if isinstance(other,Circle):
            return Circle(self.radius * other.radius)
        else:
            return Circle(self.radius * other)

    def __rmul__(self,other):
        if isinstance(other,Circle):
            return Circle(self.radius * other.radius)
        else:
            return Circle(self.radius * other)

    def __gt__(self,other):
        return self.radius > other.radius

    def __lt__(self,other):
        return self.radius < other.radius

    def __eq__(self,other):
        return self.radius == other.radius

    def __iadd__(self,other):
        return Circle(self.radius + other.radius)

    def __imul__(self,other):
        if isinstance(other,Circle):
            return Circle(self.radius * other.radius)
        else:
            return Circle(self.radius * other)

class Sphere(Circle):

    def __str__(self):
       return f'Sphere with radius: {self.radius:.6f}' 

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume (self):
        return 4/3*math.pi*self.radius*self.radius*self.radius

    @property
    def area(self):
        return 4*math.pi*self.radius*self.radius

