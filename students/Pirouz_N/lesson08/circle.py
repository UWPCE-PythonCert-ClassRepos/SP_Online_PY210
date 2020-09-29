#!/usr/bin/env python3

"""
A class-based system for circles and spheres.
"""

import math


class Circle:
    """Circle is a shape that has a radius or diameter.

        Attributes:
            radius: Attribute that defines a circle.
            diameter: Attribute that can define a circle.
            area: Attribute that defines the area of the circle.
    """
    def __init__(self, radius):
        """Initialises the circle class.

        Args:
            radius: Attribute that defines a circle.
        """
        self._check_value(radius)
        self._radius = radius

    @staticmethod
    def _check_value(value):
        """Checks if the value is not negative and it is a numeric value.

        Arguments:
            value: What should be set for the radius.

        Raises:
            ValueError: When the value is less than zero.
        """
        try:
            float(value)
        except ValueError:
            raise TypeError("Circle radius must be numeric.")
        if value < 0.0:
            raise ValueError("Circle radius and diameter must always be larger than zero.")

    @property
    def radius(self):
        """Property that shows radius of the circle.

        Returns:
            The radius of the circle.
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        """Property that shows radius of the circle.

        Arguments:
            value: What should be set for the radius.
        """
        self._check_value(value)
        self._radius = value

    @property
    def diameter(self):
        """Property that shows diameter of the circle.

        Returns:
            The diameter of the circle.
        """
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        """Property that shows diameter of the circle.

        Arguments:
            value: What should be set for the diameter.
        """
        self._check_value(value)
        self._radius = value / 2

    @property
    def area(self):
        """Property that shows area of the circle.

        Returns:
            The area of the circle.
        """
        return self._radius ** 2 * math.pi

    @property
    def perimeter(self):
        """Property that shows perimeter of the circle.

        Returns:
            The perimeter of the circle.
        """
        return self._radius * 2 * math.pi

    @classmethod
    def from_diameter(cls, diameter):
        """Constructor for circle from diameter.

        Returns:
            An instance of the circle object.
        """
        cls._check_value(diameter)
        return cls(diameter / 2)

    def __str__(self):
        """It returns the string representation of the class."""
        return "{} with radius: {:.6f}".format(self.__class__.__name__, self._radius)

    def __repr__(self):
        """It returns the method used to create the current object."""
        return "{}({})".format(self.__class__.__name__, self._radius)

    @staticmethod
    def _must_be_a_circle(item):
        """Checks if item is a circle."""
        if not isinstance(item, Circle):
            raise TypeError("It must be a circle instance.")

    def __add__(self, other):
        """It adds two circle objects."""
        self._must_be_a_circle(other)
        return Circle(self._radius + other.radius)

    def __sub__(self, other):
        """It subtracts two circle objects."""
        self._must_be_a_circle(other)
        self._check_value(self._radius - other.radius)
        return Circle(self._radius - other.radius)

    def __mul__(self, other):
        """It multiplies a number by a circle object's radius and returns a new circle object with resulting radius."""
        self._check_value(other)
        return Circle(self._radius * other)

    def __rmul__(self, other):
        """It multiplies a number by a circle object's radius and returns a new circle object with resulting radius."""
        self._check_value(other)
        return Circle(self._radius * other)

    def __truediv__(self, other):
        """It divides a circle object's radius by a number and returns a new circle object with resulting radius."""
        self._check_value(other)
        return Circle(self._radius / other)

    def __rtruediv__(self, other):
        """It divides a circle object's radius by a number and returns a new circle object with resulting radius."""
        self._check_value(other)
        return Circle(other / self._radius)

    def __floordiv__(self, other):
        """It divides a circle object's radius by a number and returns a new circle object with resulting radius."""
        self._check_value(other)
        return Circle(self._radius // other)

    def __rfloordiv__(self, other):
        """It divides a circle object's radius by a number and returns a new circle object with resulting radius."""
        self._check_value(other)
        return Circle(other // self._radius)

    def __lt__(self, other):
        """Less than comparator."""
        self._must_be_a_circle(other)
        return self._radius < other.radius

    def __le__(self, other):
        """Less than or equal to comparator."""
        self._must_be_a_circle(other)
        return self._radius <= other.radius

    def __eq__(self, other):
        """Equal to comparator."""
        self._must_be_a_circle(other)
        return self._radius == other.radius

    def __ge__(self, other):
        """Grater than or equal to comparator."""
        self._must_be_a_circle(other)
        return self._radius >= other.radius

    def __gt__(self, other):
        """Grater than comparator."""
        self._must_be_a_circle(other)
        return self._radius > other.radius

    def __ne__(self, other):
        """Not equal to comparator."""
        self._must_be_a_circle(other)
        return self._radius != other.radius

    def __iadd__(self, other):
        """It adds a circle object to current circle object."""
        self._must_be_a_circle(other)
        self._radius += other.radius
        return self

    def __isub__(self, other):
        """It subtracts a circle object from current circle object."""
        self._must_be_a_circle(other)
        self._radius -= other.radius
        return self

    def __imul__(self, other):
        """It multiplies a number by current circle object."""
        self.radius *= other
        return self

    def __itruediv__(self, other):
        """It multiplies a number by current circle object."""
        self.radius /= other
        return self

    def __ifloordiv__(self, other):
        """It multiplies a number by current circle object."""
        self.radius //= other
        return self


class Sphere(Circle):
    """Sphere is a shape that has a radius or diameter.

        Attributes:
            radius: Attribute that defines a circle.
            diameter: Attribute that can define a circle.
            area: Attribute that defines the area of the circle.
    """
    def __init__(self, radius):
        """Initialises the circle class.

        Args:
            radius: Attribute that defines a circle.
        """
        super().__init__(radius)

    @property
    def area(self):
        """Property that shows area of the circle.

        Returns:
            The area of the circle.
        """
        return self._radius ** 2 * math.pi * 4

    @property
    def volume(self):
        """Property that shows volume of the circle.

        Returns:
            The volume of the circle.
        """
        return self._radius ** 3 * math.pi * 4 / 3

    @staticmethod
    def _must_be_a_sphere(item):
        """Checks if item is a sphere."""
        if not isinstance(item, Sphere):
            raise TypeError("It must be a sphere instance.")

    def __add__(self, other):
        """It adds two circle objects."""
        self._must_be_a_sphere(other)
        return Sphere(self._radius + other.radius)

    def __sub__(self, other):
        """It subtracts two circle objects."""
        self._must_be_a_sphere(other)
        self._check_value(self._radius - other.radius)
        return Sphere(self._radius - other.radius)

    def __mul__(self, other):
        """It multiplies a number by a circle object's radius and returns a new circle object with resulting radius."""
        self._check_value(other)
        return Sphere(self._radius * other)

    def __rmul__(self, other):
        """It multiplies a number by a circle object's radius and returns a new circle object with resulting radius."""
        self._check_value(other)
        return Sphere(self._radius * other)

    def __truediv__(self, other):
        """It divides a circle object's radius by a number and returns a new circle object with resulting radius."""
        self._check_value(other)
        return Sphere(self._radius / other)

    def __rtruediv__(self, other):
        """It divides a circle object's radius by a number and returns a new circle object with resulting radius."""
        self._check_value(other)
        return Sphere(other / self._radius)

    def __floordiv__(self, other):
        """It divides a circle object's radius by a number and returns a new circle object with resulting radius."""
        self._check_value(other)
        return Sphere(self._radius // other)

    def __rfloordiv__(self, other):
        """It divides a circle object's radius by a number and returns a new circle object with resulting radius."""
        self._check_value(other)
        return Sphere(other // self._radius)

    def __lt__(self, other):
        """Less than comparator."""
        self._must_be_a_sphere(other)
        return self._radius < other.radius

    def __le__(self, other):
        """Less than or equal to comparator."""
        self._must_be_a_sphere(other)
        return self._radius <= other.radius

    def __eq__(self, other):
        """Equal to comparator."""
        self._must_be_a_sphere(other)
        return self._radius == other.radius

    def __ge__(self, other):
        """Grater than or equal to comparator."""
        self._must_be_a_sphere(other)
        return self._radius >= other.radius

    def __gt__(self, other):
        """Grater than comparator."""
        self._must_be_a_sphere(other)
        return self._radius > other.radius

    def __ne__(self, other):
        """Not equal to comparator."""
        self._must_be_a_sphere(other)
        return self._radius != other.radius

    def __iadd__(self, other):
        """It adds a circle object to current circle object."""
        self._must_be_a_sphere(other)
        self._radius += other.radius
        return self

    def __isub__(self, other):
        """It subtracts a circle object from current circle object."""
        self._must_be_a_sphere(other)
        self._radius -= other.radius
        return self
