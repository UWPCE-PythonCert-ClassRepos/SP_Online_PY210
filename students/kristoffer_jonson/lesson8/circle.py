#!/usr/bin/env python3

import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

    @property
    def diameter(self):
        diameter = self.radius * 2
        return diameter

    @diameter.setter
    def diameter(self,value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius * self.radius

    @classmethod
    def from_diameter(cls,diameter):
        return cls(diameter/2)

    def __str__(self):
        return "Circle with radius:  {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __mul__(self, other):
        if isinstance(other,Circle):
            return Circle(self.radius * other.radius)
        else:
            return Circle(self.radius * other)

    def __rmul__(self, other):
        if isinstance(other,Circle):
            return Circle(self.radius * other.radius)
        else:
            return Circle(self.radius * other)

    def __gt__(self,other):
        return self.radius > other.radius

    def __lt__(self,other):
        return self.radius < other.radius

    def __eq__(self,other):
        return self.radius == other.radius

    def __iadd__(self,other):
        return Circle(self.radius + other.radius)

    def __imul__(self,other):
        if isinstance(other,Circle):
            return Circle(self.radius * other.radius)
        else:
            return Circle(self.radius * other)

class Sphere(Circle):
    @property
    def area(self):
        return 4 * math.pi * self.radius * self.radius

    @property
    def volume(self):
        return 4/3 * math.pi * self.radius * self.radius * self.radius

    def __str__(self):
        return "Sphere with radius:  {:.6f}".format(self.radius)

    def __repr__(self):
        return "Sphere({})".format(self.radius)
