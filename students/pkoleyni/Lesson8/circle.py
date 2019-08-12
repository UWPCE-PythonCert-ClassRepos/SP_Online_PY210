#! /usr/bin/env python3
from math import pi

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self,value):
        if value != 0:
            self.radius = value / 2
        else:
            raise ValueError ('Invalid Diameter value ')

    @property
    def area(self):
        return '{0:.6f}'.format(pi * (self.radius ** 2))

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)


    def __add__(self, other):
        value = other if not isinstance(other, Circle) else other.radius
        return Circle(self.radius + value)

    def __radd__(self, other):
        value = other if not isinstance(other, Circle) else other.radius
        return Circle(self.radius + value)
        
    def __rmul__(self, other):
        value = other if not isinstance(other, Circle) else other.radius
        return Circle(self.radius * value)

    def __mul__(self, other):
        value = other if not isinstance(other, Circle) else other.radius
        return Circle(self.radius * value)

    def __iadd__(self, other):
        value = other.radius
        self.diameter = self.diameter + value


    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
            return True if self.radius == other.radius else False

    def __le__(self, other):
        return self.radius <= other.radius


    def __truediv__(self, other):
        return Circle.from_diameter((self.radius / other.radius) * 2)


    @staticmethod
    def sort_key(self):
        return self.radius

class Sphere(Circle):

    def __repr__(self):
        return "Sphere({})".format(self.radius)

    def __str__(self):
        return "Sphere with radius:{}".format(self.radius)

    @property
    def volume(self):
        return (4/3 * pi * (self.radius**3))


circle_list = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
c1 = Circle(4)
c2 = Circle(6)
c3 = Circle (8)