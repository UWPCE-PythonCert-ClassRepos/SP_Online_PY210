#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 1/4/2020
# circle.py
# ver 2

import math

def is_valid_entry(value):
    if isinstance(value, str):
        raise ValueError('Value must be a number')
    elif isinstance(value, (int, float)):
        if value < 0:
            raise ValueError('Value must be a positive number')
        else:
            return True
    else:
        return False

def is_valid_for_div(denominator):
    if is_valid_entry(denominator):
        if denominator == 0:
            raise ValueError('Denominator value must greater than zero')
        else:
            return True
    else:
        if denominator.radius == 0:
            raise ValueError('Denominator value must greater than zero')
        else:
            return False

def is_valid_for_add(self, value):
    if isinstance(value, str):
        raise ValueError('Value must be a number')
    elif isinstance(value, (int, float)):
        if self.radius + value < 0:
            raise ValueError('Value must less than or equal to the radius')
        else:
            return True
    else:
        return False

def is_valid_for_sub(self, value):
    if isinstance(value, str):
        raise ValueError('Value must be a number')
    elif isinstance(value, (int, float)):
        if self.radius - value < 0:
            raise ValueError('Value must less than or equal to the radius')
        else:
            return True
    else:
        if self.radius - value.radius < 0:
            raise ValueError('Value must less than or equal to the radius')
        else:
            return False

class Circle(object):

    def __init__(self, radius=0):
        if is_valid_entry(radius):
            self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if is_valid_entry(radius):
            self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        if is_valid_entry(diameter):
            self._radius = diameter / 2

    @property
    def area(self):
        return math.pi * self._radius * 2

    @area.setter
    def area(self, area):
        raise AttributeError('Area cannot be set')

    @classmethod
    def from_diameter(cls, diameter):
        if is_valid_entry(diameter):
            return cls(diameter / 2)

    def __str__(self):
        return 'Circle with radius: {}'.format(self._radius)

    def __repr__(self):
        return 'Circle({})'.format(self._radius)

    def __add__(self, other):
        if is_valid_for_add(self, other):
            return self.__class__(self._radius + other)
        else:
            return self.__class__(self._radius + other.radius)

    def __radd__(self, other):
        if is_valid_for_add(self, other):
            return self.__class__(self._radius + other)
        else:
            return self.__class__(self._radius + other.radius)

    def __iadd__(self, other):
        if is_valid_for_add(self, other):
            return self.__class__(self._radius + other)
        else:
            return self.__class__(self._radius + other.radius)

    def __sub__(self, other):
        if is_valid_for_sub(self, other):
            return self.__class__(self._radius - other)
        else:
            return self.__class__(self._radius - other.radius)

    def __isub__(self, other):
        if is_valid_for_sub(self, other):
            return self.__class__(self._radius - other)
        else:
            return self.__class__(self._radius - other.radius)

    def __mul__(self, other):
        if is_valid_entry(other):
            return self.__class__(self._radius * other)
        else:
            return self.__class__(self._radius * other.radius)

    def __rmul__(self, other):
        if is_valid_entry(other):
            return self.__class__(self._radius * other)
        else:
            return self.__class__(self._radius * other.radius)

    def __imul__(self, other):
        if is_valid_entry(other):
            return self.__class__(self._radius * other)
        else:
            return self.__class__(self._radius * other.radius)

    def __truediv__(self, other):
        if is_valid_for_div(other):
            return self.__class__(self._radius / other)
        else:
            return self.__class__(self._radius / other.radius)

    def __idiv__(self, other):
        if is_valid_for_div(other):
            return self.__class__(self._radius / other)
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
