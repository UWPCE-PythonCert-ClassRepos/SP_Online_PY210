#!/usr/bin/env python3

"""
A class-based system for a Circle
"""

import math

class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return self.radius**2 * math.pi

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(a, b):
        return Circle(a.radius + b.radius)

    def __mul__(a, num):
        return Circle(a.radius * num)

    def __lt__(a, b):
        return a.radius < b.radius

    def __eq__(a, b):
        return a.radius == b.radius


class Sphere(Circle):
    def __str__(self):
        return f"Sphere with side: {self.radius}"

    def __repr__(self):
        return f"Sphere({self.radius})"

    @property
    def volume(self):
        return (4 / 3) * self.radius**3 * math.pi

    @property
    def area(self):
        raise NotImplementedError
