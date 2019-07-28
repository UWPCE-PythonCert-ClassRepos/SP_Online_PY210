"""
The goal is to create a class that represents a simple circle.

A Circle can be defined by either specifying the radius or the diameter,
and the user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area.
Print the circle and get something nice.
Be able to add two circles together.
Be able to compare two circles to see which is bigger.
Be able to compare to see if they are are equal.
(follows from above) be able to put them in a list and sort them.

"""
import math


class Circle():

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def _is_valid_operand(self, other):
        return (hasattr(other, "radius"))

    def __add__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return Circle(self.radius - other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle.__mul__(self, other)

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.radius < other.radius

    def __iadd__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return Circle(self.radius + other.radius)

    def __imul__(self, other):
        return Circle(self.radius * other)

    @classmethod
    def from_diameter(cls, val):
        self = cls((val/2))
        return self

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return math.pi * self.radius * self.radius

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2


class Sphere(Circle):
    def __repr__(self):
        return f"Sphere({self.radius})"

    def __str__(self):
        return f"Sphere with radius: {self.radius}"

    @property
    def volume(self):
        return (4/3) * math.pi * (self.radius * self.radius * self.radius)

    @property
    def area(self):
        return 4 * math.pi * (self.radius * self.radius)
