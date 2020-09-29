# Circle Cass exercise for Lesson 8 created by Niels Skvarch

import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    def __str__(self):
        return "A circle with a radius of: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __floordiv__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius // other.radius)
        else:
            return Circle(self.radius // other)

    def __iadd__(self, other):
        return Circle(self.radius + other.radius)

    def __imul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius


class Sphere(Circle):

    @property
    def area(self):
        return self.radius * self.radius * math.pi * 4

    @property
    def volume(self):
        return self.radius * self.radius * self.radius * math.pi * (4/3)

    def __str__(self):
        return "A Sphere with a radius of: {}".format(self.radius)

    def __repr__(self):
        return "Sphere({})".format(self.radius)


