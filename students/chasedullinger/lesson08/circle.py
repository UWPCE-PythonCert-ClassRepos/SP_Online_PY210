#!/usr/bin/env python

""" Circle class for lesson 08 - Chase Dullinger"""

import math


class Circle:
    """Circle class capable of storing radius, diameter, and area"""
    def __init__(self, radius=0):
        if radius < 0:
            raise ValueError("Radius can not be less than 0")
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            raise ValueError("Radius can not be less than 0")
        else:
            self._radius = new_radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, new_diameter):
        if new_diameter < 0:
            raise ValueError("Diameter can not be less than 0")
        else:
            self._radius = new_diameter / 2

    @property
    def area(self):
        return math.pi * (self._radius ** 2)  # pi*r^2 for area of a circle

    @classmethod
    def from_diameter(cls, diameter=0):
        """Alternate class creation method:
        Creates object using diameter instead of radius."""
        return cls(diameter / 2)

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, circle2):
        if isinstance(circle2, Circle):
            return Circle(self.radius + circle2.radius)
        elif isinstance(circle2, (int, float)):
            if self.radius + circle2 < 0:
                raise ValueError("Resulting circle will have negative radius")
            return Circle(self.radius + circle2)
        else:
            raise TypeError("Addition requires circles or circle + number")

    def __radd__(self, circle2):
        return self.__add__(circle2)

    def __iadd__(self, radius_to_add):
        if isinstance(radius_to_add, Circle):
            self.radius = self.radius + radius_to_add.radius
            return self
        elif isinstance(radius_to_add, (int, float)):
            if self.radius + radius_to_add < 0:
                raise ValueError("Resulting circle will have negative radius")
            self.radius = self.radius + radius_to_add
            return self
        else:
            raise TypeError("Addition requires circles or circle + number")

    def __sub__(self, circle2):
        if isinstance(circle2, Circle):
            if self.radius - circle2.radius < 0:
                raise ValueError("Resulting circle will have negative radius")
            return Circle(self.radius - circle2.radius)
        elif isinstance(circle2, (int, float)):
            if self.radius + circle2 < 0:
                raise ValueError("Resulting circle will have negative radius")
            return Circle(self.radius - circle2)
        else:
            raise TypeError("Subtraction requires circles or circle + number")

    def __rsub__(self, circle2):
        return self.__sub__(circle2)

    def __isub__(self, radius_to_sub):
        if isinstance(radius_to_sub, Circle):
            if radius_to_sub.radius > self.radius:
                raise ValueError("Resulting circle will have negative radius")
            self.radius = self.radius - radius_to_sub.radius
            return self
        elif isinstance(radius_to_sub, (int, float)):
            if self.radius - radius_to_sub < 0:
                raise ValueError("Resulting circle will have negative radius")
            self.radius = self.radius - radius_to_sub
            return self
        else:
            raise TypeError("Addition requires circles or circle + number")

    def __mul__(self, circle2):
        if isinstance(circle2, Circle):
            return Circle(self.radius * circle2.radius)
        elif isinstance(circle2, (int, float)):
            if circle2 < 0:
                raise ValueError("Resulting circle will have negative radius")
            return Circle(self.radius * circle2)
        else:
            raise TypeError("Multiplication requires circles or\
 circle + number")

    def __rmul__(self, circle2):
        return self.__mul__(circle2)

    def __truediv__(self, circle2):
        if not isinstance(circle2, (int, float, Circle)):
            raise TypeError("Division requires circles or\
         circle + number")
        return self.__mul__(1 / circle2)

    def __rtruediv__(self, circle2):
        if isinstance(circle2, Circle):
            return Circle(circle2.radius / self.radius)
        elif isinstance(circle2, (int, float)):
            if circle2 < 0:
                raise ValueError("Resulting circle will have negative radius")
            return Circle(circle2 / self.radius)
        else:
            raise TypeError("Division requires circles or\
         circle + number")

    def __eq__(self, circle2):
        if isinstance(circle2, Circle):
            return self.radius == circle2.radius
        elif isinstance(circle2, (int, float)):
            return self.radius == circle2
        else:
            raise TypeError("Incompatible types for comparision")

    def __lt__(self, circle2):
        if isinstance(circle2, Circle):
            return self.radius < circle2.radius
        elif isinstance(circle2, (int, float)):
            return self.radius < circle2
        else:
            raise TypeError("Incompatible types for comparision")

    def __gt__(self, circle2):
        if isinstance(circle2, Circle):
            return self.radius > circle2.radius
        elif isinstance(circle2, (int, float)):
            return self.radius > circle2
        else:
            raise TypeError("Incompatible types for comparision")

    def __le__(self, circle2):
        return self.__lt__(circle2) or self.__eq__(circle2)

    def __ge__(self, circle2):
        return self.__gt__(circle2) or self.__eq__(circle2)

    def __ne__(self, circle2):
        return not self.__eq__(circle2)


class Sphere(Circle):
    """Sphere class capable of storing radius, diameter, area, and volume"""

    @property
    def area(self):
        # 4 *pi*r^2 for area of a sphere
        return 4 * math.pi * (self._radius ** 2)

    @property
    def volume(self):
        # 4/3*pi*r^3 for volume of sphere
        return (4 / 3) * math.pi * (self._radius ** 3)

    def __str__(self):
        return f"Sphere with radius {self.radius}"

    def __repr__(self):
        return f"Sphere({self.radius})"

    def __add__(self, sphere2):
        if isinstance(sphere2, Sphere):
            return Sphere(self.radius + sphere2.radius)
        elif isinstance(sphere2, (int, float)):
            if self.radius + sphere2 < 0:
                raise ValueError("Resulting sphere will have negative radius")
            return Sphere(self.radius + sphere2)
        else:
            raise TypeError("Addition requires spheres or sphere + number")

    def __sub__(self, sphere2):
        if isinstance(sphere2, Sphere):
            if self.radius - sphere2.radius < 0:
                raise ValueError("Resulting sphere will have negative radius")
            return Sphere(self.radius - sphere2.radius)
        elif isinstance(sphere2, (int, float)):
            if self.radius + sphere2 < 0:
                raise ValueError("Resulting sphere will have negative radius")
            return Sphere(self.radius - sphere2)
        else:
            raise TypeError("Subtraction requires spheres or sphere + number")

    def __mul__(self, sphere2):
        if isinstance(sphere2, Sphere):
            return Sphere(self.radius * sphere2.radius)
        elif isinstance(sphere2, (int, float)):
            if sphere2 < 0:
                raise ValueError("Resulting sphere will have negative radius")
            return Sphere(self.radius * sphere2)
        else:
            raise TypeError("Multiplication requires spheres or\
 sphere + number")

    def __truediv__(self, sphere2):
        if not isinstance(sphere2, (int, float, Sphere)):
            raise TypeError("Division requires spheres or\
         sphere + number")
        return self.__mul__(1 / sphere2)

    def __rtruediv__(self, sphere2):
        if isinstance(sphere2, Sphere):
            return Sphere(sphere2.radius / self.radius)
        elif isinstance(sphere2, (int, float)):
            if sphere2 < 0:
                raise ValueError("Resulting sphere will have negative radius")
            return Sphere(sphere2 / self.radius)
        else:
            raise TypeError("Division requires spheres or\
         sphere + number")
