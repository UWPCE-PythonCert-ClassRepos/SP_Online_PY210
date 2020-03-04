#!/usr/bin/env python3


import math




class Circle(object):

    radius = ()

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


