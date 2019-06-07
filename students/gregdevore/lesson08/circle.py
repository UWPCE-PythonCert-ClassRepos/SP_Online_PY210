#!/usr/bin/env python3

# Circle class
from math import pi

class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    @property
    def diameter(self):
        return self._radius * 2

    @radius.setter
    def radius(self, value):
        self._radius = value
    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    @property
    def area(self):
        return pi * self._radius ** 2

    @classmethod
    def from_diameter(cls, value):
        # Construct circle with radius as usual
        return cls(value / 2)

    def __str__(self):
        return 'Circle with radius {:f}'.format(self._radius)

    def __repr__(self):
        return 'Circle({:f})'.format(self._radius)

    def __add__(self, other):
        if isinstance(other, int):
            # Adding a constant should produce a circle with the new radius
            return Circle(self.radius + other)
        elif isinstance(other, Circle):
            # Adding two circles should produce a circle with the combined radius
            return Circle(self.radius + other.radius)
        else:
            # Other combinations not supported
            raise TypeError('unsupported operand type(s) for +: \'Circle\' and \'{}\''.format(type(other).__name__))

    def __radd__(self, other):
        # Reversed addition should follow the same rules
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            result = self.radius - other
            if result <= 0:
                raise ValueError('Circle radius must be positive.')
            # Adding a constant should produce a circle with the new radius
            return Circle(result)
        elif isinstance(other, Circle):
            result = self.radius - other.radius
            if result <= 0:
                raise ValueError('Circle radius must be positive.')
            # Adding two circles should produce a circle with the combined radius
            return Circle(result)
        else:
            # Other combinations not supported
            raise TypeError('unsupported operand type(s) for -: \'Circle\' and \'{}\''.format(type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, int):
            # Multiplying by a constant should produce a circle with the new radius
            return Circle(self.radius * other)
        elif isinstance(other, Circle):
            # Multiplying two circles should produce a circle with the combined radius
            return Circle(self.radius * other.radius)
        else:
            # Other combinations not supported
            raise TypeError('unsupported operand type(s) for *: \'Circle\' and \'{}\''.format(type(other).__name__))

    def __rmul__(self, other):
        # Reversed multiplication should follow the same rules
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            # Dividing by a constant should produce a circle with the new radius
            return Circle(self.radius / other)
        elif isinstance(other, Circle):
            # Dividing two circles should produce a circle with the new radius
            return Circle(self.radius / other.radius)
        else:
            # Other combinations not supported
            raise TypeError('unsupported operand type(s) for /: \'Circle\' and \'{}\''.format(type(other).__name__))

    def __pow__(self, other):
        if isinstance(other, int):
            # Dividing by a constant should produce a circle with the new radius
            return Circle(self.radius ** other)
        else:
            # Other combinations not supported
            raise TypeError('unsupported operand type(s) for /: \'Circle\' and \'{}\''.format(type(other).__name__))

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius
