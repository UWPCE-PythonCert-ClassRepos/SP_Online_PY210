#!/usr/bin/env python

import math


# step 1
class Circle():
    def __init__(self, the_radius):
        self.radius = the_radius
# step 2
        self._diameter = 2 * the_radius

# c = Circle(3.5)
# print(c.radius)
# print(c._diameter)

# step 3
# have to use @property to make the 'diameter' like a method even
# though it's an attribute
    @property
    def diameter(self):
        return self._diameter

# can now use to the @property 'diameter' to alter the object.
# A backwards update
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
        self._diameter = value

# c2 = Circle(4)
# print(c2.diameter)
# print(c2.radius)
# c2.diameter = 10
# print(c2.diameter)
# print(c2.radius)

# step 4
    @property
    def area(self):
        self._area = math.pi * (self.radius ** 2)
        return self._area


# c3 = Circle(4)
# print(c3.area)

# step 5
# this is a way to update a class backwards, like the @property + .setter way
    @classmethod
    def from_diameter(cls, stupid):
        return cls(stupid / 2)

# c5 = Circle.from_diameter(8)
# print(c5.diameter)

# step 6
    def __repr__(self):
        return f"Circle({self.radius})"

    def __str__(self):
        return f"Circle with radius: {self.radius}"

# step 7
    def __add__(self, other):
        if isinstance(other, int):
            return Circle(self.radius + other)
        elif isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            raise TypeError('Try again.')

    def __mul__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)
        elif isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        else:
            raise TypeError('No, wrong.')

# c7 = Circle(5)
# c7b = Circle(6)
# print(c7+c7b*'v')
# print(c7*6)

# step 8
    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __le__(self, other):
        if self.radius <= other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.radius >= other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.radius != other.radius:
            return True
        else:
            return False


# step 9
class Sphere(Circle):
    def __repr__(self):
        return f"Sphere({self.radius})"

    def __str__(self):
        return f"Sphere with radius: {self.radius}"

    @property
    def volume(self):
        self._volume = (4/3) * math.pi * (self.radius ** 3)
        return self._volume

    @property
    def area(self):
        raise NotImplementedError


# s = Sphere.from_diameter(5)
# print(s.volume)
