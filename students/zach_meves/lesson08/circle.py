"""
circle.py
Zachary Meves
Python 210
Lesson 08

Circle Assignment
"""

import math


class Circle:
    """A class defining a circle."""

    def __init__(self, radius: float):
        """Construct a circle with a given radius.

        Parameters
        ----------
        radius : float
            Radius to initialize circle with
        """

        self._radius = 0
        self.radius = radius

    @property
    def radius(self):
        """The circle's radius."""

        return self._radius

    @radius.setter
    def radius(self, new_radius: float):
        if new_radius >= 0:
            self._radius = float(new_radius)
        else:
            raise ValueError("Radius must be >= 0")

    @property
    def diameter(self):
        """The circle's diameter."""

        return 2 * self._radius

    @diameter.setter
    def diameter(self, new_diameter: float):
        self.radius = new_diameter / 2

    @property
    def area(self) -> float:
        """Area of the circle."""

        return math.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter: float):
        """Construct a Circle with a given diameter.

        Parameters
        ----------
        diameter : float
            Diameter of Circle to make.

        Returns
        -------
        Circle
            Circle with given diameter
        """

        return cls(diameter / 2)

    def __repr__(self):
        return f"Circle({self.radius:g})"

    def __str__(self):
        return f"Circle with radius: {self.radius:.6f}"

    def __add__(self, other):
        try:
            return Circle(self. radius + other.radius)
        except AttributeError:
            raise TypeError("A Circle can only be added with another Circle")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        try:
            return Circle(self.radius - other.radius)
        except AttributeError:
            raise TypeError("A Circle can only be subtracted from another Circle.")

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        try:
            return Circle(self.radius * other)
        except AttributeError:
            raise TypeError("A Circle can only be multiplied by a number.")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self.__mul__(1 / other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __pow__(self, power, modulo=None):
        return Circle(self.radius ** power)


class Sphere(Circle):
    """A class defining a sphere."""

    @property
    def volume(self):
        """Volume of the sphere."""
        return 4/3 * math.pi * self.radius ** 3

    @property
    def area(self):
        return 4 * super().area

    def __repr__(self):
        return f"Sphere({self.radius:g})"

    def __str__(self):
        return f"Sphere with radius: {self.radius:.6f}"
