#!/usr/bin/env python3

from math import sqrt, pi, pow


class Circle(object):
    """
    Circle takes a radius or diameter and supports a variety of functions
    """
    def __init__(self, the_radius):
        self.radius = round(float(the_radius), 2)

    def __call__(self, radius, area):
        return self._radius, self._area

    @property
    def radius(self):
        """
        getter for radius
        :return: internal radius
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        """
        setter for radius
        :param value: radius
        :return:
        """
        if value <= 0:
            raise ValueError("radius must be greater than zero")
        self._radius = value

    @property
    def diameter(self):
        """
        getter for diameter
        :return: diameter of circle
        """
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        """
        setter for diameter; syncs radius value
        :param value: diameter
        :return:
        """
        self.radius = value / 2

    @property
    def area(self):
        """
        calculate area of circle: a = pi * (r^2)
        :return: area of circle
        """
        return round(pi * pow(self.radius, 2), 2)

    @classmethod
    def from_diameter(cls, value=None):
        """
        Circle alternate constructor
        :param value: diameter
        """
        return cls(value / 2)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __mul__(self, other):
        try:
            isinstance(other, int)
        except TypeError as mult_error:
            raise mult_error("circles can only be multiplied by int")
        finally:
            return Circle(self.radius * other)

    def __rmul__(self, other):
        try:
            isinstance(other, int)
        except TypeError as mult_error:
            raise mult_error("circles can only be multiplied by int")
        finally:
            return self.__mul__(other)

    def __imul__(self, other):
        if isinstance(self, int) and isinstance(other, Circle):
            return self.__mul__(other.radius)
        if isinstance(self, Circle) and isinstance(other, int):
            return self.__mul__(other.radius)
        if isinstance(self, Circle) and isinstance(other, Circle):
            return self.__mul__(other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __str__(self):
        """
        prints Circle object
        :return: String representation of Circle object
        """
        return f"Circle with radius: {self._radius}"

    def __repr__(self):
        """
        :return: string of self instantiation
        """
        return f"Circle({self._radius})"


class Sphere(Circle):
    """
    Sphere object derives from Circle class
    """

    @property
    def area(self):
        """
        area of sphere
        :return: area of sphere
        """
        return 4 * super().area

    @property
    def volume(self):
        """
        calculate area of sphere: a = (4/3) * pi * (r^3)
        :return: volume of sphere
        """
        return round((4/3) * pi * (pow(self.radius, 3)), 2)

    def __repr__(self):
        return f"Sphere({self.radius})"

    def __str__(self):
        return f"Sphere with radius: {self.radius}"

