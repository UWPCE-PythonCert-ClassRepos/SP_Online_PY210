#!/usr/bin/env python3

"""
A class-based system for a circle
"""

import math


# This is the framework for the base class
from abc import ABC


class Circle(object):

    def __init__(self, the_radius):
        self.radius = the_radius

    def __str__(self):
        return (self.__class__.__name__ + " with radius: {0:.6f}").format(self.radius)

    def __repr__(self):
        return (self.__class__.__name__ + "({})").format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, the_diameter):
        self.radius = the_diameter/2

    @property
    def area(self):
        # Read only attribute
        return math.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter/2)
        return self
