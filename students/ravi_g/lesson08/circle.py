#!/usr/bin/env python3

"""
Class for Circle and Sphere
"""

import math

# circle class
class Circle:


    # radius initialized with 0 radius
    def __init__(self, radius=0):
        self.radius = radius

    # diameter
    @property
    def diameter(self):
        return self.radius * 2

    # use diameter to set radius
    @diameter.setter
    def diameter(self,diameter):
        self.radius = diameter / 2

    # area of circle
    @property
    def area(self):
        return math.pi * self.radius ** 2

    # creating a circle from given diameter
    @classmethod
    def from_diameter(cls, diameter=1):
        return cls(diameter/2)

    def __str__(self):
        return 'Circle with radius {}'.format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    # adding two circles based on radius
    def __iadd__(self, other):
        self.radius += other.radius

    # multiplying a circle based on a multiplier
    def __imul__(self, other):
        self.radius *= other

    # Creating a circle with two radius added
    def __add__(self, other):
        return self.radius + other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    # multiplier
    def __mul__(self,other):
        if isinstance(other, circle):
            return Circle(self.radius * other)
        else:
            return Circle(self * other.radius)
    # multiplier with a number
    def __rmul__(self,other):
        if isinstance(self, Circle):
            return Circle(self.radius * other)
        else:
            return Circle(self * other.radius)

    @staticmethod
    def sort_key(self):
        return self.radius


# Sphere
class Sphere(Circle):

    def __str__(self):
        return 'Sphere of radius {}'.format(self.radius)

    def __repr__(self):
        return "Sphere({})".format(self.radius)

    # volume of sphere
    @property
    def volume(self):
        return math.pi * pow(self.radius,3) ** (4/3)

    # volume of sphere
    @property
    def area(self):
        if isinstance(self, Sphere):
            return 4 * math.pi * self.radius ** 2
        else:
            raise (NotImplementedError, 'Not a Sphere Object')
