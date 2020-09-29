#!/usr/bin/env python
# circle.py
# L Ferrier
# Python 201, Assignment 08

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
        # return self.radius

    @property
    def area(self):
        return math.pi * (self.radius**2)

    @classmethod
    def from_diameter(cls, diameter):
        radius = (diameter / 2)
        return cls(radius)

    def __str__(self):
        return(self.__class__.__name__ + ' with radius: {}'.format(self.radius))

    def __repr__(self):
        return (self.__class__.__name__ + '({})'.format(self.radius))

    def __add__(self, other):
        return self.__class__(self.radius + other.radius)

    def __mul__(self, other):
        return self.__class__(self.radius * other)

    def __rmul__(self, other):
        return self.__class__(self.radius * other)

    def __floordiv__(self, other):
        return self.__class__(self.radius // other)

    def __lt__(self, other):
        return self.__class__(self.radius < other.radius)

    def __gt__(self, other):
        return self.__class__(self.radius > other.radius)

    def __eq__(self, other):
        return self.__class__(self.radius == other.radius)

    def __ne__(self, other):
        return self.__class__(self.radius != other.radius)


class Sphere(Circle):
    @property
    def volume(self):
        return math.pi * (4 / 3) * (self.radius ** 3)

    @volume.setter
    def volume(self, value):
        self.radius = (value ** ((3 * value) / (4 * math.pi)))
        return self.radius

    @property
    def area(self):
        return ((self.radius ** 2) * (4 * math.pi))

