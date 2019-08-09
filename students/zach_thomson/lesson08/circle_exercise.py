#!/usr/bin/env python3

from math import pi

class Circle():

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = value / 2

    @property
    def area(self):
        return (self.radius ** 2) * pi

    @classmethod
    def from_diameter(cls, value):
        diameter = value / 2
        return cls(diameter)

    def __str__(self):
        return 'Circle with radius: {:.6f}'.format(float(self.radius))

    def __repr__(self):
        return "Circle({})".format(self.radius)
