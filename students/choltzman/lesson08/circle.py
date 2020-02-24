#!/usr/bin/env python3
import math
from functools import total_ordering


@total_ordering
class Circle:
    def __init__(self, radius):
        try:
            self.radius = float(radius)
        except ValueError:
            print("Input to Circle class must be a number.")
            exit(1)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, value):
        return Circle(self.radius * value)

    def __rmul__(self, value):
        return Circle(self.radius * value)

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, value):
        return cls(value / 2)


class Sphere(Circle):
    """IDK"""

    def __str__(self):
        return f"Sphere with radius: {self.radius}"

    def __repr__(self):
        return f"Sphere({self.radius})"

    @property
    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    @property
    def volume(self):
        return math.pi * 4/3 * (self.radius ** 3)
