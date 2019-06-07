#!/usr/bin/env python3

# Circle class
from math import pi

class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    @property
    def diameter(self):
        return self._radius * 2

    @radius.setter
    def radius(self, value):
        self._radius = value
    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    @property
    def area(self):
        return pi * self._radius ** 2

    @classmethod
    def from_diameter(cls, value):
        # Construct circle with radius as usual
        return cls(value / 2)

    def __str__(self):
        return 'Circle with radius {:f}'.format(self._radius)

    def __repr__(self):
        return 'Circle({:f})'.format(self._radius)
