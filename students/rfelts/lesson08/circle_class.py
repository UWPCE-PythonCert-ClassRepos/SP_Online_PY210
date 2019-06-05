#!/usr/bin/env python3

# Russell Felts
# Assignment 8 - Circle Class

import math


# This is the circle class
class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __gt__(self, other):
        return True if self.radius > other.radius else False

    def __eq__(self, other):
        return True if self.radius == other.radius else False


# This is the Sphere subclassed from the Circle class
class Sphere(Circle):

    def __init__(self, radius):
        super().__init__(radius)

    def __str__(self):
        return f"Sphere with radius: {self.radius}"

    def __repr__(self):
        return f"Sphere({self.radius})"

    @property
    def volume(self):
        return (4/30) * math.pi * self.radius ** 3

    @property
    def area(self):
        return 4 * math.pi * self.radius ** 2
