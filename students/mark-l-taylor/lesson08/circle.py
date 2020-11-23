#!/usr/bin/env python

from math import pi

class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    def __str__(self):
        return 'Circle with radius: {:.6f}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        elif isinstance(other, (int, float)):
            return Circle(self.radius + other)
        else:
            raise TypeError('Circle does not support adding {}'.format(type(other)))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Circle):
            other = other.radius
        elif isinstance(other, (int, float)):
            pass
        else:
            raise TypeError('Circle does not support adding {}'.format(type(other)))

        new_radius = self.radius - other
        if new_radius >= 0:
            return Circle(new_radius)
        else:
            raise ValueError('New Circle radius must be greater than or equal to zero. Calculated radius = {}'.format(new_radius))

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        elif isinstance(other, (int, float)):
            return Circle(self.radius * other)
        else:
            raise TypeError('Circle does not support multiplying by  {}'.format(type(other)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius ** other.radius)
        elif isinstance(other, (int, float)):
            return Circle(self.radius ** other)
        else:
            raise TypeError('Circle does not support power by  {}'.format(type(other)))

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            raise TypeError('Circle does not support comparing by  {}'.format(type(other)))

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise TypeError('Circle does not support comparing by  {}'.format(type(other)))

class Sphere(Circle):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return 'Sphere with radius: {:.6f}'.format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume(self):
        return 4/3 * pi * (self.radius **3)

    @property
    def area(self):
        return 4 * pi * (self.radius ** 2)