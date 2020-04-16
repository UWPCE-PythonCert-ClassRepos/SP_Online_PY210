#!/usr/bin/env python3

import math

###################################


class Circle:
    def __init__(self, in_radius):
        self.radius = in_radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, x):
        self.radius = x / 2

    @property
    def area(self):
        return math.pi * (self.radius**2)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        return 'circle.Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'circle.Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        return Circle(self.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __imul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


class Sphere(Circle):

    @property
    def volume(self):
        return (4/3) * math.pi * (self.radius**3)

    @property
    def area(self):
        return 4 * math.pi * self.radius**2

    def __str__(self):
        return 'Sphere with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)
