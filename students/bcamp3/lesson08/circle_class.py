#!/usr/bin/env python3

import math

class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter * 0.5
        return cls(radius)

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __add__(self, other):
        if isinstance(other, int):
            return Circle(self.radius + other)
        elif isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            raise TypeError

    def __radd__(self, other):
        # Reversed addition should follow the same rules
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            radius = self.radius - other
            if radius <= 0:
                raise ValueError('Circle radius must be greater than zero.')
            return Circle(radius)
        elif isinstance(other, Circle):
            radius = self.radius - other.radius
            if radius <= 0:
                raise ValueError('Circle radius must be greater than zero.')
            return Circle(radius)
        else:
            raise TypeError

    def __mul__(self,  other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Circle(self.radius / other)
        elif isinstance(other, Circle):
            return Circle(self.radius / other.radius)
        else:
            raise TypeError

    def sort_key(self):
        return self.area

    def __str__(self):
        return (" This is a Circle object:\n"
                f" diameter = {self.diameter:>8.4f}\n"
                f"     area = {self.area:>8.4f}")

    def __repr__(self):
        return f"Circle({self.radius})"


class Sphere(Circle):

    @property
    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    @property
    def area(self):
        return 4 * math.pi * self.radius ** 2

    def __str__(self):
        return (" This is a Sphere object:\n"
                f" diameter = {self.diameter:>8.4f}\n"
                f"     area = {self.area:>8.4f}\n"
                f"   volume = {self.volume:>8.4f}")

    def __repr__(self):
        return f"Sphere({self.radius})"
