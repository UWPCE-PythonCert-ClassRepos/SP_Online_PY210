"""
Christine Kim
Lesson 8
Assignment Circles
"""
import math

class Circle():

    #initiate circle with radius
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __radd__(self, other):
        return self.__add__(other)

    def __lt__(self, other):
        return (self.radius, self.diameter, self.area) < (other.radius, other.diameter, other.area)

    def __eq__(self, other):
        return (self.radius, self.diameter, self.area) == (other.radius, other.diameter, other.area)

    def __le__(self, other):
        return (self.radius, self.diameter, self.area) <= (other.radius, other.diameter, other.area)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __truediv__(self, other):
        return Circle(self.radius / other.radius)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(c, diameter):
        self = c(diameter / 2)
        return self 