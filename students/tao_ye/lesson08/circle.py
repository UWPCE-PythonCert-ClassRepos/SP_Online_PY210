#!/usr/bin/env python3

import math as m
from functools import total_ordering


@total_ordering
class Circle():
    def __init__(self, the_radius):
        self.radius = the_radius

    def __str__(self):
        return f"Circle with radius: {self.radius:0.6f}"

    def __repr__(self):
        return f"Circle({self.radius})"

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2.0)

    @property
    def diameter(self):
        return self.radius * 2.0

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        return m.pi * self.radius ** 2

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            return NotImplemented

    def __mul__(self, other):
        # for Circle Object * number
        if type(other) == int or type(other) == float:
            return Circle(self.radius * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        # for number * Circle Object
        return Circle.__mul__(self, other)

    def __eq__(self, other):
        if isinstance(self, Circle) and isinstance(other, Circle):
            return self.radius == other.radius
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(self, Circle) and isinstance(other, Circle):
            return self.radius < other.radius
        else:
            return NotImplemented

    def sort_key(self):
        """
        sorting key function --used to pass in to sort functions
        to get faster sorting

        Example::

          sorted(list_of_simple_objects, key=Simple.sort_key)

        """
        return self.radius


class Sphere(Circle):
    def __str__(self):
        return f"Sphere with radius: {self.radius:0.6f}"

    def __repr__(self):
        return f"Sphere({self.radius})"

    @property
    def volume(self):
        return 4/3 * m.pi * self.radius ** 3

    @property
    def area(self):
        return 4 * m.pi * self.radius ** 2
