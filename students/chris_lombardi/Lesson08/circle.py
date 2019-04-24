#!/usr/bin/env python

import math

class Circle:
    """
    Class definition for a circle with a specified radius
    """
    def __init__(self, value):
        self.radius = value

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return (self.radius ** 2 * math.pi)

    @classmethod
    def from_diameter(cls, value):
        radius = value / 2
        return cls(radius)

    def __str__(self):
        return 'Circle with radius: {:.4f}'.format(self.radius)

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, obj):
        return Circle(self.radius + obj.radius)

    def __mul__(self, obj):
        return Circle(self.radius * obj)

    def __sub__(self,obj):
        if self.radius - obj.radius <= 0:
            return Circle(0)
        else:
            return Circle(self.radius - obj.radius)

    def __eq__(self,other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def sort_key(self):
        return self.radius

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __iadd__(self, value):
        return Circle(self.radius + value)

    def __imul__(self, value):
        return Circle(self.radius * valuec1)

class Sphere(Circle):
    """
    Class definition for a sphere with a specified radius
    """

    @property
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    @property
    def area(self):
        raise NotImplementedError

    def __str__(self):
        return 'Sphere with radius: {:.4f}'.format(self.radius)

    def __repr__(self):
        return f'Sphere({self.radius})'