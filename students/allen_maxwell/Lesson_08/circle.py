#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 1/3/2020
# circle.py

import math


class Circle(object):

    def __init__(self, radius=0):
        if not isinstance(radius, (int, float)):
            raise ValueError('Radius must be a number')
        elif radius < 0:
            raise ValueError('Radius must be a positive number')
        else:
            self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise ValueError('Radius must be a number')
        elif radius < 0:
            raise ValueError('Radius must be a positive number')
        else:
            self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        if not isinstance(diameter, (int, float)):
            raise ValueError('Diameter must be a number')
        elif diameter < 0:
            raise ValueError('Diameter must be a positive number')
        else:
            self._radius = diameter / 2

    @property
    def area(self):
        return math.pi * self._radius * 2

    @area.setter
    def area(self, area):
        raise AttributeError('Area cannot be set')

    @classmethod
    def from_diameter(cls, diameter):
        if not isinstance(diameter, (int, float)):
            raise ValueError('Diameter must be a number')
        elif diameter < 0:
            raise ValueError('Diameter must be a positive number')
        else:
            return cls(diameter / 2)

    def __str__(self):
        return 'Circle with radius: {}'.format(self._radius)

    def __repr__(self):
        return 'Circle({})'.format(self._radius)

    def __add__(self, other):
        if isinstance(other, str):
            raise ValueError('Value must be a number')
        elif isinstance(other, (int, float)):
            if self.radius + other < 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius + other)
        else:
            return self.__class__(self._radius + other.radius)

    def __radd__(self, other):
        if isinstance(other, str):
            raise ValueError('Value must be a number')
        elif isinstance(other, (int, float)):
            if self.radius + other < 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius + other)
        else:
            return self.__class__(self._radius + other.radius)

    def __iadd__(self, other):
        if isinstance(other, str):
            raise ValueError('Value must be a number')
        elif isinstance(other, (int, float)):
            if self.radius + other < 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius + other)
        else:
            return self.__class__(self._radius + other.radius)

    def __sub__(self, other):
        if isinstance(other, str):
            raise ValueError('Value must be a number')
        elif isinstance(other, (int, float)):
            if self.radius - other < 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius - other)
        else:
            if self.radius - other.radius < 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius - other.radius)

    def __isub__(self, other):
        if isinstance(other, str):
            raise ValueError('Value must be a number')
        elif isinstance(other, (int, float)):
            if self.radius - other < 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius - other)
        else:
            if self.radius - other.radius < 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius - other.radius)

    def __mul__(self, other):
        if isinstance(other, str):
            raise ValueError('Value must be a number')
        elif isinstance(other, (int, float)):
            if self.radius * other < 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius * other)
        else:
            return self.__class__(self._radius * other.radius)

    def __rmul__(self, other):
        if isinstance(other, str):
            raise ValueError('Value must be a number')
        elif isinstance(other, (int, float)):
            if self.radius * other < 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius * other)
        else:
            return self.__class__(self._radius * other.radius)

    def __imul__(self, other):
        if isinstance(other, str):
            raise ValueError('Value must be a number')
        elif isinstance(other, (int, float)):
            if self.radius * other < 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius * other)
        else:
            return self.__class__(self._radius * other.radius)

    def __truediv__(self, other):
        if isinstance(other, str):
            raise ValueError('Value must be a number')
        elif isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius / other)
        else:
            if other.radius <= 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius / other.radius)

    def __idiv__(self, other):
        if isinstance(other, str):
            raise ValueError('Value must be a number')
        elif isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius / other)
        else:
            if other.radius <= 0:
                raise ValueError('Value must less than or equal to the radius')
            else:
                return self.__class__(self._radius / other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def sort_key(self):
        return self.radius


class Sphere(Circle):

    def __str__(self):
        return 'Sphere with radius: {}'.format(self._radius)

    def __repr__(self):
        return 'Sphere({})'.format(self._radius)

    @property
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    @property
    def area(self):
        return 4 * math.pi * self.radius ** 2
