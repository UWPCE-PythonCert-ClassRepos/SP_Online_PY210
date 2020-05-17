#!/usr/bin/env python3
"""
Jack Anderson
03/14/2020
UW PY210
Lesson 08

Circle and Sphere classes
"""
import math



class Circle(object):

    def __init__(self, radius):
        try:
            self.radius = radius
            if self.radius <= 0:
                print("Must use a positive interger")
                raise ValueError
        except TypeError:
            raise TypeError


    @property
    def diameter(self):
        return self.radius * 2


    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return round((self.radius ** 2) * math.pi, 3)

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter * 2)
        return self


    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f'Circle({self.radius})'


    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __radd__(self, other):
        return Circle(self.radius + other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Circle(self.radius - other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __lt__(self, other):
        return (self.radius, self.diameter, self.area) < (other.radius, other.diameter, other.area)

    def __eq__(self, other):
        return (self.radius, self.diameter, self.area) == (other.radius, other.diameter, other.area)

    def __truediv__(self, other):
        return Circle(self.radius / other.radius)

    def __floordiv__(self, other):
        return Circle(self.radius // other.radius)


class Sphere(Circle):

    def __str__(self):
        return f"Sphere with radius: {self.radius}"

    def __repr__(self):
        return f'Sphere({self.radius})'

    @property
    def volume(self):
        # Volume of a sphere: 4/3 * pi * radius^3
        x = (((4/3) * math.pi) * (self.radius ** 3))
        return float(f"{x:.2f}")

    @property
    def area(self):
        # A = 4 * pi * radius^2
        x = ((self.radius ** 2) * math.pi) * 4
        return float(f"{x:.2f}")

