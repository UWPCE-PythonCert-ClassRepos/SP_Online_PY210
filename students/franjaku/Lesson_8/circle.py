#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

import math
from functools import total_ordering

# This is the framework for the circle class
@total_ordering
class Circle(object):
    """This is the circle class"""

    def __init__(self, radius):
        """
        Require parameters: Radius
        """
        self._radius = radius

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({:.0f})".format(self.radius)

    def __add__(self, c2):
        return Circle(self.radius + c2.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        return (self.radius < other.radius)

    def __eq__(self, other):
        return (self.radius == other.radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2

    @property
    def area(self):
        return math.pow(self.radius, 2)*math.pi

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)


class Sphere(Circle):
    """
    Simple sphere class that subclasses from circle.
    """

    def __str__(self):
        return "Sphere with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Sphere({:.0f})".format(self.radius)

    @property
    def area(self):
        return 4*math.pi*math.pow(self.radius, 2)

    @property
    def volume(self):
        return 4/3*math.pi*math.pow(self.radius, 3)
