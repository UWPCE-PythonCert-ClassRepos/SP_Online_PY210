#!/usr/bin/env python3
from math import pi


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    def __str__(self):
        return "Circle with radius: {self.radius}".format(self=self)

    def __repr__(self):
        return "Circle(" + str(self.radius) + ")"

    def __add__(self, other):
        combined_radius = self.radius + other.radius
        return Circle(combined_radius)

    def __iadd__(self, other):
        combined_radius = self.radius + other.radius
        return Circle(combined_radius)

    def __mul__(self, integer):
        mult_radius = self.radius * integer
        return Circle(mult_radius)

    def __rmul__(self, integer):
        mult_radius = self.radius * integer
        return Circle(mult_radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

class Sphere(Circle):
    def __str__(self):
        return "Sphere with radius: {self.radius}".format(self=self)

    def __repr__(self):
        return "Sphere(" + str(self.radius) + ")"

    @property
    def volume(self):
        return (4/3)*pi * (self.radius ** 3)

    @property
    def area(self):
        return 4*pi * (self.radius ** 2)

