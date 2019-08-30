#!/usr/bin/env python3

import math

class Circle(object):
    _radius = None
    _diameter = None

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


    def __sub__(self, other):
        try:
            return self.__class__(self._radius - other._radius)
        except AttributeError:
            return self.__class__(self._radius - other)


    def __mul__(self, other):
        try:
            return self.__class__(self._radius * other._radius)
        except AttributeError:
            return self.__class__(self._radius * other)


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
