#!/usr/bin/env python

#Lesson 8 The Circle Class

import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
        
    @diameter.setter
    def diameter(self, value):
        self.radius = value/2
    
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2.0)
        
    def __str__(self):
        return f'Circle with radius: {self.radius:.3f}'
        
    def __repr__(self):
        return 'Circle({})'.format(self.radius)
        
    def __add__(self, other):
        return Circle(self.radius + other.radius)
        
    def __mul__(self, other):
        return Circle(self.radius * other)
            
    def __rmul__(self, other):
        return Circle(self.radius * other)
            
    def __floordiv__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius // other.radius)
        else:
            return Circle(self.radius // other)
            
    def __iadd__(self, other):
        return Circle(self.radius + other.radius)
        
    def __imul__(self, other):
        return Circle(self.radius * other)
        
    def __imul__(self, other):
        return Circle(self.radius * other)
            
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __le__(self, other):
        return self.radius <= other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius
