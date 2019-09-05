#!/usr/bin/env python3

import math
class Circle:

    def __init__(self, rad_length):
        self.radius = rad_length
    
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, x):
        self.radius = x / 2

    @property
    def area(self):
        return round(math.pi * self.radius**2,5)

    @classmethod
    def from_diameter(cls, diam):
        radius = diam / 2
        return cls(radius)

    def __str__(self):
        return "Circle with radius: {:.4f}".format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        if self.radius - other.radius <= 0:
            return Circle(0)
        else:
            return Circle(self.radius - other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __imul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return (self.radius == other.radius)

    def __lt__(self, other):
        return (self.radius < other.radius)

    def sort_key(self):
        return self.radius

class Sphere(Circle):

    @property
    def area(self):
        return round(4*math.pi * self.radius**2,5)

    @property
    def volume(self):
        return round(4/3*math.pi * self.radius**3,5)

    def __str__(self):
        return "Sphere with radius: {:.4f}".format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)







    
    
