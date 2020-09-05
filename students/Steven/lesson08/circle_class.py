#!/usr/bin/env python3
"""
The goal is to create a class that represents a simple circle.

A Circle can be defined by either specifying the radius or the diameter, and the user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area.
Print the circle and get something nice.
Be able to add two circles together.
Be able to compare two circles to see which is bigger.
Be able to compare to see if they are are equal.
(follows from above) be able to put them in a list and sort them.
"""

import math

class Circle():
    # Circle object with a given radius
    def __init__(self, radius):
        self.radius = radius

    @property
    def get_diameter(self):
        return self.radius * 2

    @get_diameter.setter
    def get_diameter(self, value):
        self.radius = value / 2

    @property
    def get_area(self):
        return math.pi * self.radius ** 2

    @get_area.setter
    def get_area(self, value):
        raise AttributeError

    @classmethod
    def from_diameter(cls, value):
        return cls(value / 2)

    # For printing out
    def __str__(self):
        return f"Circle with a radius of: {self.radius}, Diameter of: {self.get_diameter}"

    def __repr__(self):
        return f"Circle({self.radius})"

    # Numeric protocols
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __eq__(self, other):
        return self.radius == other.radius

class Sphere(Circle):

    # Override the Circle str method
    def __str__(self):
        return f"Sphere with a radius of: {self.radius}, Diameter of: {self.get_diameter}"

    # Override the Circle repr method
    def __repr__(self):
        return f"Sphere({self.radius})"

    @property
    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3  # Formula for volume of a sphere

    @property
    def get_area(self):
        return 4 * math.pi * self.radius ** 2  # Formula for the surface area of a sphere