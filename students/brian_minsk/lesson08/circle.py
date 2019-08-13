# Author: Brian Minsk

class Circle(object):
    def __init__(self, radius=1):
        if not isinstance(radius, (int, float)):
            raise ValueError("Radius must be a number.")
        if radius < 0:
            raise ValueError("Negative radius is not possible.")
        self._radius = radius
        self._diameter = 2 * radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Radius must be a number.")
        if value < 0:
            raise ValueError("Negative radius is not possible.")
        self._radius = value
        self._diameter = 2 * value

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Diameter must be a number.")
        if value < 0:
            raise ValueError("Negative diameter is not possible.")
        self._radius = 0.5 * value
        self._diameter = value

    