#!/usr/bin/env python3

"""
A class-based system that represents a simple circle.
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = int(value / 2)

    @property
    def area(self):
        return math.pi * math.pow(self.radius, 2)

    @classmethod
    def from_diameter(cls, value):
        self = cls(int(value / 2))
        return self

    def __str__(self):
        return 'Circle with radius: {:.6f}'.format(self.radius)
    
    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, a_cicle):
        return Circle(self.radius + a_cicle.radius)

    def __mul__(self, value):
        return Circle(self.radius * value)

    def __rmul__(self, value):
        return Circle(self.radius * value)

    def __gt__(self, a_cicle):
        return self.radius > a_cicle.radius
    
    def __lt__(self, a_cicle):
        return self.radius < a_cicle.radius
    
    def __eq__(self, a_cicle):
        return self.radius == a_cicle.radius

class Sphere(Circle):
    def __init__(self, radius):
        self.radius =  radius
        Circle.__init__(self, radius)
    
    def __str__(self):
        return 'Sphere with radius: {:.6f}'.format(self.radius)
    
    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume(self):
        return 4/3 * math.pi * math.pow(self.radius, 3)

    @property
    def area(self):
        raise NotImplementedError("Method has not been implemented!!!")
