#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

import math


# This is the framework for the circle class
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
    def from_diameter(self, diameter):
        return Circle(diameter/2)
