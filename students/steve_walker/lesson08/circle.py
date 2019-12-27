#!/usr/bin/env python3

"""
Classing circles.
"""

from math import pi


class Circle():

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return pi * self.radius ** 2

    # Note to self: classmethod can give different ways to instantiate classes
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, value):
        return Circle(self.radius * value)

    def __rmul__(self, value):
        return Circle(self.radius * value)

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius


class Sphere(Circle):

    @property
    def area(self):
        return 4 * pi * self.radius ** 2

    @property
    def volume(self):
        return (4/3) * pi * self.radius ** 3

    def __str__(self):
        return f"Sphere with radius: {self.radius}"

    def __repr__(self):
        return f"Sphere({self.radius})"
