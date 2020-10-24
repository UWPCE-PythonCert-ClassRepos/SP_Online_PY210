#!/usr/bin/env python3

import math

class Circle(object):

    def __init__(self, radius):
        self.radius = radius 

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diamter(self, value):
        self.radius = 2 / value

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        cls.diameter = diameter
        radius = diameter / 2
        return cls(radius)       

    def __str__(self):
        return 'Circle with a radius of {}'.format(self.radius) 

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)
    
    def __mul__(self, other):
        if type(other) == int:
            return Circle(self.radius * other)
        else:
            return Circle(self.radius * self.other)
    
    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ne__(self, other):
        return self.radius != other.radius

class Sphere(Circle):

    def __str__(self):
        return 'Sphere with a radius of {}'.format(self.radius) 

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)
    
    @property
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    @property
    def area(self):
        return 4 * math.pi * self.radius ** 2
