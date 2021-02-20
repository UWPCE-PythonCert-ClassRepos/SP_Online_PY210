#!/usr/bin/env python3
"""
Created on Sun Jan 10 14:38:21 2021

@author: johnh
"""

#Circles

from math import pi


class Circle():
    """
    base class for the circle objects
    """

    radius = float()

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2*self.radius

    @property
    def area(self):
        return round(self.radius ** 2 * pi, 7)

    @diameter.setter
    def diameter(self, value):
        self.radius = value/2

    @classmethod
    def from_diameter(cls, value):
        return cls(value/2)

    def __call__(self, value):
        return str(Circle(value))

    def __str__(self):
        return f'The Object is a Circle with Radius: {self.radius:.7f}'
    def __repr__(self):
        return "Circle({})".format(self.radius)
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    def __sub__(self, other):
        return Circle(self.radius - other.radius)
    def __mul__(self, other):
        return Circle(self.radius * other.radius)
    def __pow__(self, other):
        return Circle(self.radius ** other.radius)
    def __gt__(self, other):
        return self.radius > other.radius
    def __ge__(self, other):
        return self.radius >= other.radius
    def __lt__(self, other):
        return self.radius < other.radius
    def __le__(self, other):
        return self.radius <= other.radius
    def __eq__(self, other):
        return self.radius == other.radius
    def sort_key(self):
        return self.val


class Sphere(Circle):
    def __str__(self):
        return f'The Object is a Sphere with Radius: {self.radius:.7f}'

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume(self):
        return round(self.radius**3 * 4/3 * pi, 7)

    @property
    def surface_area(self):
        return round(self.radius ** 2 * 4 * pi, 7)
    