# Author: Brian Minsk

from math import pi
from functools import total_ordering

@total_ordering
class Circle(object):
    def __init__(self, radius=0):
        if not isinstance(radius, (int, float)):
            raise ValueError("Radius must be a number.")
        if radius < 0:
            raise ValueError("Negative radius is not possible.")
        self._radius = radius
        self._diameter = 2 * radius
        self._area = pi * radius ** 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise ValueError("Radius must be a number.")
        if radius < 0:
            raise ValueError("Negative radius is not possible.")
        self._radius = radius
        self._diameter = 2 * radius
        self._area = pi * radius ** 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        if not isinstance(diameter, (int, float)):
            raise ValueError("Diameter must be a number.")
        if diameter < 0:
            raise ValueError("Negative diameter is not possible.")
        self._radius = 0.5 * diameter
        self._diameter = diameter
        self._area = pi * ((0.5 * diameter) ** 2)

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        """ Prevent area from being set.
        """
        raise AttributeError("Area cannot be set.")

    @classmethod
    def from_diameter(cls, diameter=0):
        """ Alternate constructor using diameter.
        """
        if not isinstance(diameter, (int, float)):
            raise ValueError("Diameter must be a number.")
        if diameter < 0:
            raise ValueError("Negative diameter is not possible.")

        self = cls()
        self._radius = 0.5 * diameter
        self._diameter = diameter
        self._area = pi * ((0.5 * diameter) ** 2)
        return self

    def __str__(self):
        return "Circle with radius: {:f}".format(float(self.radius))

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        # test that the 2nd argument is a Circle
        if not isinstance(other, Circle):
            raise TypeError("Only a Circle (or subclass) can be added to a Circle.")
        else:
            new_radius = self.radius + other.radius
            return Circle(new_radius)

    def __iadd__(self, other):
        # test that the 2nd argument is a Circle
        if not isinstance(other, Circle):
            raise TypeError("Only a Circle (or subclass) can be added to a Circle.")
        else:
            self.radius = self.radius + other.radius
            return self


    def __mul__(self, other):
        # test that the 2nd argument is an int or float
        if not isinstance(other, (int, float)):
            raise TypeError("A Circle can only be multiplied by a number.")
        else:
            new_radius = self.radius * other
            return Circle(new_radius)

    # This handles the case when the number is first, e.g. 3 * Circle(2)
    __rmul__ = __mul__

    def __imul__(self, other):
        # test that the 2nd argument is an int or float
        if not isinstance(other, (int, float)):
            raise TypeError("A Circle can only be multiplied by a number.")
        else:
            self.radius = self.radius * other
            return self

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("A Circle can only be compared with another Circle.")
        return self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("A Circle can only be compared with another Circle.")
        return self.radius < other.radius
    
