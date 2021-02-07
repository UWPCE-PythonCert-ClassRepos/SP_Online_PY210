# ------------------------------------------------------------------------------ #
# Title: Lesson08 - Circle Class Exercise
# Description: Assignment from Lesson08 - Circle Class Exercise
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,02-05-2021, Created Circle Class
# ------------------------------------------------------------------------------ #
import functools
import math

@functools.total_ordering
class Circle(object):
    """
    Class that implements a Circle behaviour
    """

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        try:
            self.__radius = float(radius)
        except ValueError as error:
            raise ValueError("Incorrect value provided as radius. "
                             "Radius must be a floating point number or an integer value. "
                             "Error: {}".format(error))

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        try:
            self.radius = float(diameter) / 2
        except ValueError as error:
            raise ValueError("Incorrect value provided as diameter. "
                             "Diameter must be a floating point number or an integer value. "
                             "Error: {}".format(error))

    @property
    def area(self):
        return math.pi * self.radius**2

    @classmethod
    def from_diameter(cls, diameter):
        try:
            radius = float(diameter) / 2
        except ValueError as error:
            raise ValueError("Incorrect value provided as diameter. "
                             "Diameter must be a floating point number or an integer value. "
                             "Error: {}".format(error))
        return cls(radius)

    def __str__(self):
        return f"Circle with radius: {self.radius:.3f}"

    def __repr__(self):
        return f"Circle({self.radius})"


    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __add__(self, other):
        if isinstance(other, Circle):
            return type(self)(self.radius + other.radius)
        elif isinstance(other, int) or isinstance(other, float):
            return type(self)(self.radius + other)
        else:
            raise ValueError("It is not possible to add a Circle to a an instance of type {}".format(type(other)))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Circle):
            return type(self)(self.radius - other.radius)
        elif isinstance(other, int) or isinstance(other, float):
            return type(self)(self.radius - other)
        else:
            raise ValueError("It is not possible to subtract a Circle to a an instance of type {}".format(type(other)))

    def __rsub__(self, other):
        if isinstance(other, Circle):
            return type(self)(other.radius - self.radius)
        elif isinstance(other, int) or isinstance(other, float):
            return type(self)(other - self.radius)
        else:
            raise ValueError("It is not possible to subtract a Circle to a an instance of type {}".format(type(other)))

    def __mul__(self, other):
        if isinstance(other, Circle):
            return type(self)(self.radius * other.radius)
        elif isinstance(other, int) or isinstance(other, float):
            return type(self)(self.radius * other)
        else:
            raise ValueError("It is not possible to multiply a Circle by a an instance of type {}".format(type(other)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Circle):
            return type(self)(self.radius / other.radius)
        elif isinstance(other, int) or isinstance(other, float):
            return type(self)(self.radius / other)
        else:
            raise ValueError("It is not possible to divide a Circle by a an instance of type {}".format(type(other)))

    def __rtruediv__(self, other):
        if isinstance(other, Circle):
            return type(self)(other.radius / self.radius)
        elif isinstance(other, int) or isinstance(other, float):
            return type(self)(other / self.radius)
        else:
            raise ValueError("It is not possible to divide a Circle by a an instance of type {}".format(type(other)))


