#!/usr/bin/env python3
import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        diameter = self.radius * 2
        return diameter

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        area = self.radius ** 2 * math.pi
        return area

    @classmethod
    def from_diameter(cls, diameter):
        radius = cls(diameter / 2)
        return radius

    def __str__(self):
        return f'Circle with radius: {self.radius}'

    def __repr__(self):
        return f'Circle({self.radius})'

    # Numeric Protocol
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ne__(self, other):
        return self.radius != other.radius


class Sphere(Circle):

    def __str__(self):
        return f'Sphere with radius: {self.radius}'

    def __repr__(self):
        return f'Sphere({self.radius})'

    @property
    def volume(self):
        volume = self.radius ** 3 * math.pi * 4 / 3
        return volume

    @property
    def area(self):
        area = self.radius ** 2 * math.pi * 4
        return area

