# Author: Brian Minsk

from math import pi

class Circle(object):
    def __init__(self, radius=1):
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