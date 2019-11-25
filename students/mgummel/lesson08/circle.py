#! /usr/bin/env python3
from math import pi
from functools import total_ordering


@total_ordering
class Circle(object):
    radius = None

    def __init__(self, radius):
        """
        Instantiates a Circle object with it's radius.

        :param radius: the radius of the circle
        :type radius: float or int
        """
        self.radius = radius

    def __str__(self):
        """
        Returns a string that displays the class attribute radius.
        """
        return f"Circle with radius: {self.radius:.5f}"

    def __repr__(self):
        """
        Returns the Circle instance definition in a string format.
        """
        return f"Circle({self.radius})"

    def __add__(self, other):
        """
        Adds two Circle objects together and creates another Circle
        based on the combinded radius size.
        """
        return Circle(self.radius + other.radius)

    def __mul__(self, scalar):
        """
        Returns a new Circle object based on the size of the scalar multiplier
        (i.e. scalar * Circle).

        :param scalar: Multiplier to increase the radisu by
        :type scalar: int
        """
        return Circle(self.radius * scalar)

    def __rmul__(self, scalar):
        """
        Returns a new Circle object based on the size of the scalar multiplier.
        Allows for the scalar to be the multiplied after the circle object
        (i.e. Circle * scalar).

        :param scalar: Multiplier to increase the radisu by
        :type scalar: int
        """
        return self.__mul__(scalar)

    def __lt__(self, other):
        """
        Returns True if this instance object is smaller than another Circle
        object. Returns False otherwise.
        """
        return (self.radius < other.radius)

    def __eq__(self, other):
        """
        Returns True if the Circles objects have the same radius size. Returns
        False if the radius' aren't the same.
        """
        return (self.radius == other.radius)

    @property
    def diameter(self):
        """
        Returns the Circle's diameter which is twice the radisu.
        """
        return self.radius * 2

    @diameter.setter
    def diameter(self, new_value):
        """
        Sets the diameter and the radius based on new diameter.
        """
        self.radius = new_value / 2
        return new_value

    @property
    def area(self):
        """
        Returns the area of the Circle based on its radius.
        """
        return (self.radius ** 2) * pi

    @classmethod
    def from_diameter(cls, diameter):
        """
        Creates a new Circle object based on diameter instead of
        the radius.
        """
        if diameter % 2 == 0:
            return cls(int(diameter / 2))
        else:
            return cls(diameter / 2)


class Sphere(Circle):

    def __add__(self, other):
        """
        Adds two Sphere objects together and creates another Sphere
        based on the combinded radius size.
        """
        return Sphere(self.radius + other.radius)


    def __mul__(self, scalar):
        """
        Returns a new Sphere object based on the size of the scalar multiplier
        (i.e. scalar * Sphere).

        :param scalar: Multiplier to increase the radisu by
        :type scalar: int
        """
        return Sphere(self.radius * scalar)


    def __rmul__(self, scalar):
        """
        Returns a new Sphere object based on the size of the scalar multiplier.
        Allows for the scalar to be the multiplied after the sphere object
        (i.e. Sphere * scalar).

        :param scalar: Multiplier to increase the radisu by
        :type scalar: int
        """
        return self.__mul__(scalar)


    #def __lt__(self, other):
        """
        Returns True if this instance object is smaller than another Circle
        object. Returns False otherwise.
        """
    #    return (self.radius < other.radius)

    
    #def __eq__(self, other):
        """
        Returns True if the Circles objects have the same radius size. Returns
        False if the radius' aren't the same.
        """
    #    return (self.radius == other.radius)
    def __str__(self):
        """
        Returns a string that displays the sphere's radius.
        """
        return f"Sphere with radius: {self.radius:.5f}"


    def __repr__(self):
        """
        Returns a string of the representation of a Sphere based on 
        its radius.
        """
        return f"Sphere({self.radius})"

    @property
    def volume(self):
        """
        Returns a calculation of the sphere's volume based on radius
        """
        return (4 / 3) * pi * (self.radius ** 3)

    @property
    def area(self):
        """
        Returns the surface area of a sphere based on radius.
        """
        return 4 * pi * self.radius ** 2
