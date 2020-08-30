"""Implements the Circle class"""

import math


class Circle:
    """A circle"""

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        """Gets the diameter"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, new_diam):
        """
        Sets the new diameter of the circle

        Parameters
        ----------
        new_diam : int|float
            Diameter to set for the circle
        """
        self.radius = new_diam / 2

    @property
    def area(self):
        """Gets the area"""
        return math.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        """
        Alternate constructor of Circle using diameter

        Parameters
        ----------
        diameter : int|float
            The largest straight measurement accross a circle

        Returns
        -------
        Circle
            The circle class
        """
        return cls(diameter / 2)

    def __str__(self):
        return f"Circle with radius: {self.radius:.2f}"

    def __repr__(self):
        return f"Circle({self.radius:.2f})"

    def __add__(self, other):
        radius = self.radius + other.radius
        return self.__class__(radius=radius)

    def __mul__(self, scalar):
        radius = self.radius * scalar
        return self.__class__(radius=radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __truediv__(self, scalar):
        radius = self.radius / scalar
        return self.__class__(radius=radius)

    __rmul__ = __mul__
