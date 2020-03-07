#!/usr/bin/env python
__author__ = 'Timothy Lurvey'

from math import pi, floor

num = (int, float, complex)


class Circle(object):
    _r = 0.

    def __init__(self, radius: num = 0.):
        """Create a circle class of a given radius.  c= Circle(radius=1.2) -> c.radius=1.2"""
        self._set_radius(radius=radius)

    def __str__(self):
        return "{0} class with radius of {1:.3f}".format(type(self).__name__, self.radius)

    def __repr__(self):
        return type(self).__name__ + "({})".format(self._r)

    def _new_instance(self, x):
        if isinstance(x, type(self)):
            return x
        else:
            try:
                return type(self)(float(x))
            except ValueError:
                raise ValueError("Unable to get numeric value from {}".format(type(x)))

    def __add__(self, other):
        return type(self)(self.radius + self._new_instance(other).radius)

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return type(self)(self.radius - self._new_instance(other).radius)

    def __isub__(self, other):
        return self.__sub__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        return type(self)(self.radius * self._new_instance(other).radius)

    def __imul__(self, other):
        return self.__mul__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return type(self)(self.radius / self._new_instance(other).radius)

    def __idiv__(self, other):
        return self.__truediv__(other)

    def __floordiv__(self, other):
        return type(self)(floor(self.__truediv__(other).radius))

    def __ifloordiv__(self, other):
        return self.__ifloordiv__(other)

    def __eq__(self, other):
        if self.radius == self._new_instance(other).radius:
            return True
        return False

    def __gt__(self, other):
        if self.radius > self._new_instance(other).radius:
            return True
        return False

    def __lt__(self, other):
        if self.radius < self._new_instance(other).radius:
            return True
        return False

    def __ge__(self, other):
        if self.__eq__(other) or self.__gt__(other):
            return True
        return False

    def __le__(self, other):
        if self.__eq__(other) or self.__lt__(other):
            return True
        return False

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, new_radius):
        self._set_radius(radius=new_radius)

    def _set_radius(self, radius):
        try:
            assert isinstance(radius, (int, float, complex))
            self._r = float(radius)
        except AssertionError:
            raise TypeError("radius input must be numeric")

    @property
    def diameter(self):
        return 2 * self._r

    @property
    def area(self):
        return pi * (self._r ** 2)

    @classmethod
    def from_diamter(cls, diamter):
        return cls(radius=diamter / 2)


class Sphere(Circle):

    def __init__(self, radius: num = 0.):
        super().__init__(radius=radius)

    @property
    def volume(self):
        return 4 / 3 * pi * self._r ** 3

    @property
    def area(self):
        return 4 * super().area
