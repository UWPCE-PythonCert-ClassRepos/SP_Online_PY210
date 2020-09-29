#!/usr/bin/env python3

"""
A class-based circle/sphere maker
"""

from math import pi


class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    #  Make sure properties are derived from _radius
    def diameter(self):
        return 2 * self._radius

    @radius.setter
    #  Add ability to set new radius on existing objects
    def radius(self, value):
        self._radius = value

    @diameter.setter
    #  Set new diameter on already-created object by resetting the _radius
    def diameter(self, value):
        self._radius = value / 2

    @property
    def area(self):
        return pi * (self._radius**2)


    @classmethod
    #  Add ability to create a Circle object by diameter (as well as default radius)
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        #  Human readable
        return 'Circle with a radius of: {}'.format(self._radius)

    def __repr__(self):
        #  For debugging, return actual Python that was run to create the object
        return 'Circle({})'.format(self._radius)

    def __add__(self, other):
        #  Addition magic method, handle Circles and ints. Fail on others
        if isinstance(other, int):
            return Circle(self.radius + other)
        elif isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        elif isinstance(other, int):
            return Circle(other + Circle.radius)

    def __mul__(self, other):
        #  Multiplication
        if isinstance(other, int):
            return Circle(self.radius * other)
        elif isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        elif isinstance(other, int):
            return Circle(other * Circle.radius)

    def __truediv__(self, other):
        #  Division
        if isinstance(other, int):
            return Circle(self.radius / other)
        elif isinstance(other, Circle):
            return Circle(self.radius / other.radius)
        elif isinstance(other, int):
            return Circle(other / Circle.radius)

    def __le__(self, other):
        #  Less than or equal
        if isinstance(other, int):
            return self.radius <= other
        elif isinstance(other, Circle):
            return self.radius <= other.radius
        elif isinstance(other, int):
            return other <= Circle.radius

    def __ge__(self, other):
        #  Greater than or equal
        if isinstance(other, int):
            return self.radius >= other
        elif isinstance(other, Circle):
            return self.radius >= other.radius
        elif isinstance(other, int):
            return other >= Circle.radius

    def __lt__(self, other):
        # <
        if isinstance(other, int):
            return self.radius < other
        elif isinstance(other, Circle):
            return self.radius < other.radius
        elif isinstance(other, int):
            return other < Circle.radius

    def __gt__(self, other):
        # >
        if isinstance(other, int):
            return self.radius > other
        elif isinstance(other, Circle):
            return self.radius > other.radius
        elif isinstance(other, int):
            return other > Circle.radius

    def __eq__(self, other):
        # ==
        if isinstance(other, int):
            return self.radius == other
        elif isinstance(other, Circle):
            return self.radius == other.radius
        elif isinstance(other, int):
            return other == Circle.radius


class Sphere(Circle):
    # Override circle's area property
    @property
    def area(self):
        return 4 * pi * self._radius ** 2

    @property
    # Find Sphere's volume
    def volume(self):
        return (4/3) * pi * self._radius ** 3

    # Override string and repr
    def __str__(self):
        return 'Sphere with a radius of: {}'.format(self._radius)

    def __repr__(self):
        return 'Sphere({})'.format(self._radius)







