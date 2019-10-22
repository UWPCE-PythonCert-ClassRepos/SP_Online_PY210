from math import pi

class Circle(object):
    """circle object class"""

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @radius.setter
    def radius(self, value):
        self._radius = value

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    @property
    def area(self):
        """calculates the area of a circle"""
        return round(pi * (self._radius ** 2), 4)

    @classmethod
    def from_diameter(cls, diameter):
        """creates a circle object from diameter"""
        return cls(diameter / 2)

    def __str__(self):
        return (f"Circle with a radius: {self._radius}")

    def __repr__(self):
        return (f"Circle({self._radius})")

    def __add__(self, other):
        """adds two circles together - by radius"""
        return (f"Circle({self._radius + other._radius})")

    def __mul__(self, other):
        """multiplies two circles together - by radius"""
        return (f"Circle({self._radius * other})")

    def __rmul__(self, other):
        """reverse - multiplies two circles together - by radius"""
        return (f"Circle({self._radius * other})")

    def __lt__(self, other):
        """compares two circles together (less than) - by radius"""
        return (self._radius < other._radius)

    def __gt__(self, other):
        """compares two circles together (greater than) - by radius"""
        return (self._radius > other._radius)

    def __eq__(self, other):
        """compares two circles together (equal to) - by radius"""
        return (self._radius == other._radius)

    def __truediv__(self, other):
        """divides a circle's radius by an integer"""
        return (f"Circle({self._radius / other})")

    def __rtruediv__(self, other):
        """reverse - cannot divide an integer by a circle"""
        return ("You cannot divide an integer by a Circle.")


class Sphere(Circle):
    """sphere object, subclass of circle object"""

    @property
    def volume(self):
        """calculates the volume of a sphere"""
        area = round((4/3) * pi * (self._radius ** 3), 4)
        return area

    @property
    def area(self):
        """calculates the surface area of a sphere"""
        area = round(4 * pi * (self._radius ** 2), 4)
        return area

    def __str__(self):
        return (f"Sphere with a radius: {self._radius}")

    def __repr__(self):
        return (f"Sphere({self._radius})")
