#!/usr/bin/env python

import math


class Circle():

    # Magic Methods
    def __init__(self, the_radius):
        self.radius = the_radius
        self._diameter = 2 * the_radius

    def __repr__(self):
        return f"Circle({self.radius})"

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        if isinstance(self, int) & isinstance(other, Circle):
            return Circle(self + other.radius)
        if isinstance(self, Circle) & isinstance(other, int):
            return Circle(self.radius + other)
        if isinstance(self, Circle) & isinstance(other, Circle):
            return Circle(self.radius + other.radius)

    def __mul__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)

    def __rmul__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __le__(self, other):
        if self.radius <= other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.radius >= other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.radius != other.radius:
            return True
        else:
            return False

    # Properties and Class Methods
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


class Sphere(Circle):
    def __repr__(self):
        return f"Sphere({self.radius})"

    def __str__(self):
        return f"Sphere with radius: {self.radius}"

    @property
    def area(self):
        raise NotImplementedError

    @property
    def volume(self):
        self._volume = (4/3) * math.pi * (self.radius ** 3)
        return self._volume
