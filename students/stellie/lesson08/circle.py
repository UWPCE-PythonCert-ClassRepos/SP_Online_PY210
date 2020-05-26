#!/usr/bin/env python3

# Stella Kim
# Assignment 7: The Circle Class

import math


class Circle(object):
    """A class based program that represents a simple circle."""
    def __init__(self, radius):  # circle is defined by specifying radius
        self.radius = radius

    @property  # set as property to obtain diameter of circle
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property  # set as property to obtain area of circle
    def area(self):
        return math.pi * self.radius ** 2

    @area.setter
    def area(self, value):
        raise AttributeError('The area of a circle can not be set.')

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    # Special Methods: numerics, comparison operators
    def __str__(self):
        return f'Circle with radius: {self.radius:.2f}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, other):  # to be able to add two circles together
        return Circle(self.radius + other.radius)

    def __sub__(self, other):  # to be able to subtract one circle from another
        return Circle(self.radius - other.radius)

    def __mul__(self, other):  # to be able to multiply two circles together
        if type(other) is int:
            return Circle(self.radius * other)
        else:
            return Circle(self.radius * other.radius)

    # Check to see how circles compare to one another
    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    # Sort a list of circles
    def circle_list(self, *other):
        return sorted([self, *other])


class Sphere(Circle):
    """Create a Sphere Class that sublclasses Circle"""
    # Override the __str__ and __repr__ methods to be appropriate for Spheres
    def __str__(self):
        return f'Sphere with radius: {self.radius:.2f}'

    def __repr__(self):
        return f'Sphere({self.radius})'

    # Special Methods: numerics, comparison operators
    def __add__(self, other):  # to be able to add two spheres together
        return Sphere(self.radius + other.radius)

    def __mul__(self, other):  # to be able to multiply two spheres together
        if type(other) is int:
            return Sphere(self.radius * other)
        else:
            return Sphere(self.radius * other.radius)

    # Sort a list of spheres
    def sphere_list(self, *other):
        return sorted([self, *other])

    @property  # set as property to obtain surface area of sphere
    def area(self):
        return 4 * math.pi * self.radius ** 2

    @property  # set as property to obtain volume of sphere
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3
