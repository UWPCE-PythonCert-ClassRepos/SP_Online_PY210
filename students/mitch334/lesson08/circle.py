"""Lesson 08 | Circle"""
# Goal:
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter,
# and the user can query the circle for either its radius or diameter.
#
# Other abilities of a Circle instance:
# Compute the circle’s area.
# Print the circle and get something nice.
# Be able to add two circles together.
# Be able to compare two circles to see which is bigger.
# Be able to compare to see if they are are equal.
# (follows from above) be able to put them in a list and sort them.
# create a shpere subclass from circle

# You will use:
# properties.
# a bunch of “magic methods”.
# a classmethod.

import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Circle with radius: {self.radius}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

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

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


class Sphere(Circle):
    def __str__(self):
        return f'Sphere with radius: {self.radius}'

    def __repr__(self):
        return f'Sphere({self.radius})'

    def __add__(self, other):
        return Sphere(self.radius + other.radius)

    def __mul__(self, other):
        return Sphere(self.radius * other)

    def __rmul__(self, other):
        return Sphere(self.radius * other)

    @property
    def volume(self):
        return (4/3)* math.pi * self.radius ** 3

    @property
    def area(self):
        return 4 * math.pi * self.radius ** 2
