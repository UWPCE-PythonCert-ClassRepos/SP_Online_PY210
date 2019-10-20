#!/usr/bin/env python

import math


class Circle():

    def __init__(self, the_radius):
        self.radius = the_radius
        self._diameter = 2 * the_radius

    def __repr__(self):
        return f"Circle({self.radius})"

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)
    def __rmul__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)


    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
        self._diameter = value

    @property
    def area(self):
        self._area = math.pi * (self.radius ** 2)
        return self._area

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
        
