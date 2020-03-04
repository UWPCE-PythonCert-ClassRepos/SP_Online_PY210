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


    def __add__(self, other_radius):
        return Circle(self.radius + other_radius.radius)

    def __mul__(self, value):
        return Circle(self.radius * value)

    def __lt__(self, other):
        return (self.radius, self.diameter, self.area) < (other.radius, other.diameter, other.area)

    def __eq__(self, other):
        return (self.radius, self.diameter, self.area) == (other.radius, other.diameter, other.area)
