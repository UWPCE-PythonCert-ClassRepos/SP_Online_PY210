#!/usr/bin/env python3

import math

class Circle(object):
    def __init__(self, radius):
        try:
            self._radius = float(radius)
            self._diameter = float(radius) * 2
        except ValueError:
            raise TypeError("radius expects a float")


    def __str__(self):
        return 'Circle with radius {:.5f}'.format(self._radius)


    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self._radius)


    def __add__(self, other):
        try:
            return self.__class__(self._radius + other._radius)
        except AttributeError:
            return self.__class__(self._radius + other)


    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, other):
        try:
            return self.__class__(self._radius - other._radius)
        except AttributeError:
            return self.__class__(self._radius - other)


    def __rsub__(self, other):
        return self.__class__(other - self._radius)


    def __mul__(self, other):
        try:
            return self.__class__(self._radius * other._radius)
        except AttributeError:
            return self.__class__(self._radius * other)


    def __rmul__(self, other):
        return self.__mul__(other)


    def __truediv__(self, other):
        try:
            return self.__class__(self._radius / other._radius)
        except AttributeError:
            return self.__class__(self._radius / other)


    def __rtruediv__(self, other):
        return self.__class__(other / self._radius)


    def __lt__(self, other):
        return self._radius < other._radius


    def __gt__(self, other):
        return self._radius > other._radius


    def __le__(self, other):
        return self._radius <= other._radius


    def __ge__(self, other):
        return self._radius >= other._radius


    def __eq__(self, other):
        return self._radius == other._radius


    def __ne__(self, other):
        return self._radius != other._radius


    @property
    def radius(self):
        return self._radius


    @property
    def diameter(self):
        return self._diameter


    @property
    def area(self):
        return math.pow(self._radius, 2) * math.pi


    @classmethod
    def from_diameter(cls, value):
        return cls(value / 2)


    @radius.setter
    def radius(self, value):
        try:
            self._radius = float(value)
            self._diameter = float(value) * 2
        except ValueError:
            raise TypeError("radius expects a float")


    @diameter.setter
    def diameter(self, value):
        try:
            self._radius = float(value) / 2
            self._diameter = float(value)
        except ValueError:
            raise TypeError("radius expects a float")


class Sphere(Circle):
    def __str__(self):
        return 'Sphere with radius {:.5f}'.format(self._radius)


    @property
    def area(self):
        return 4 * math.pow(self._radius, 2) * math.pi


    @property
    def volume(self):
        return (4/3) * math.pow(self._radius, 3) * math.pi
