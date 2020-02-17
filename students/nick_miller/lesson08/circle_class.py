#!/usr/bin/env python3

"""PY210_SP - circle class
author: Nick Miller"""


import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "This circle has a radius of : {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        total = self.radius + other.radius
        return Circle(total)

    def __sub__(self, other):
        total = self.radius - other.radius
        return Circle(total)

    def __mul__(self, value):
        total = self.radius * value
        return Circle(total)

    def __rmul__(self, value):
        total = self.radius * value
        return Circle(total)

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @classmethod
    def from_diameter(cls, the_diameter):
        return cls(the_diameter / 2)

    @property
    def area(self):
        return math.pi * (self.radius ** 2)


class Sphere(Circle):

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "This sphere has a radius of : {}".format(self.radius)
