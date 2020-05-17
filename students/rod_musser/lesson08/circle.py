#!/usr/bin/env python3
from math import pi
from functools import total_ordering

"""
A class representing a circle
"""


@total_ordering
class Circle(object):

    def __init__(self, the_radius):
        self._radius = the_radius

    def __str__(self):
        return 'Circle with radius: {:.6f}'.format(self.radius)

    def __repr__(self):
        return 'Circle({:d})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        new_radius = self.radius - other.radius
        if new_radius < 0:
            raise ValueError("Resulting radius must be greater than 0")
        return Circle(new_radius)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if type(other) is int:
            return Circle(self.radius * other)
        else:
            return Circle(self.radius * other.radius)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        divisor = 0
        if type(other) is int:
            divisor = other
        else:
            divisor = other.radius
        if divisor == 0:
            raise ValueError("Cannot divide by 0")
        return Circle(self.radius / divisor)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __int__(self):
        return self.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return self.radius**2 * pi

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


class Sphere(Circle):

    def __str__(self):
        return 'Sphere with radius: {:.6f}'.format(self.radius)

    def __repr__(self):
        return 'Sphere({:d})'.format(self.radius)

    @property
    def volume(self):
        return self.radius**3 * ((4 / 3) * pi)

    @property
    def area(self):
        return self.radius**2 * (4 * pi)
