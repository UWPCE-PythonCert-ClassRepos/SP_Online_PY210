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

    @property
    def diameter(self):
        self._diameter = self._radius * 2
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        if not isinstance(diameter, (int, float)):
            raise ValueError("Diameter must be a number.")
        if diameter < 0:
            raise ValueError("Negative diameter is not possible.")
        self._radius = 0.5 * diameter
        self._diameter = diameter

    @property
    def area(self):
        self._area = pi * self._radius ** 2
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
        return self

    def class_name(self):
        return type(self).__name__

    def __str__(self):
        return "{} with radius: {:f}".format(self.class_name(),
                                             float(self.radius))

    def __repr__(self):
        return "{}({})".format(self.class_name(), self.radius)

    def __add__(self, other):
        """ Note that a Sphere (or any subclass of Circle) can be added to a
        circle and vice versa. Might not make sense but I'm not sure so I'll
        just leave it.
        """
        # test that the 2nd argument is a Circle
        if not isinstance(other, Circle):
            error_str = "Only a {} can be added to a {}.".format(self.class_name(), self.class_name())
            raise TypeError(error_str)
        else:
            new_radius = self.radius + other.radius
            return self.__class__(new_radius)

    def __iadd__(self, other):
        """ Note that a Sphere (or any subclass of Circle) can be added to a
        circle and vice versa. Might not make sense but I'm not sure so I'll
        just leave it.
        """
        # test that the 2nd argument is a Circle
        if not isinstance(other, Circle):
            error_str = "Only a {} can be added to a {}.".format(self.class_name(), self.class_name())
            raise TypeError(error_str)
        else:
            self.radius = self.radius + other.radius
            return self

    def __mul__(self, other):
        # test that the 2nd argument is an int or float
        if not isinstance(other, (int, float)):
            error_str = "A {} can only be multiplied by a number.".format(self.class_name())
            raise TypeError(error_str)
        else:
            new_radius = self.radius * other
            return self.__class__(new_radius)

    # This handles the case when the number is first, e.g. 3 * Circle(2)
    __rmul__ = __mul__

    def __imul__(self, other):
        # test that the 2nd argument is an int or float
        if not isinstance(other, (int, float)):
            error_str = "A {} can only be multiplied by a number.".format(self.class_name())
            raise TypeError(error_str)
        else:
            self.radius = self.radius * other
            return self

    def __eq__(self, other):
        if not isinstance(other, Circle):
            error_str = "A {} can only be compared with another {}.".format(self.class_name(), self.class_name())
            raise TypeError(error_str)
        return self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            error_str = "A {} can only be compared with another {}.".format(self.class_name(), self.class_name())
            raise TypeError(error_str)
        return self.radius < other.radius


class Sphere(Circle):
    @property
    def area(self):
        self._area = 4 * pi * self._radius ** 2
        return self._area

    @property
    def volume(self):
        self._volume = 4 / 3 * pi * self._radius ** 3
        return self._volume

    @volume.setter
    def volume(self, volume):
        """ Prevent volume from being set.
        """
        raise AttributeError("Volume cannot be set.")
