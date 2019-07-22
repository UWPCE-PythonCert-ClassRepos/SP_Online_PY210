#!/usr/bin/env python3

import math

class Circle(object):

    def __init__(self, the_radius):
        """ Initialize circle based on given radius """
        self.radius = the_radius

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, circle_2):
        total = self.radius + circle_2.radius
        return Circle(total)

    def __mul__(self, value):
        total = self.radius * value
        return Circle(total)

    def __rmul__(self, value):
        total = self.radius * value
        return Circle(total)

    def __lt__(self, circle_2):
        if self.radius < circle_2.radius:
            return True
        else:
            return False

    def __eq__(self, circle_2):
        if self.radius == circle_2.radius:
            return True
        else:
            return False

    @property
    def diameter(self):
        """ Calculate diamater based on radius """
        return self.radius * 2

    @diameter.setter
    def diameter(self, the_diameter):
        """ Set diameter to a given value """
        self.radius = the_diameter / 2

    @property
    def area(self):
        """ Calculate area based on radius """
        return math.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, the_diameter):
        """ Create a Circle directly with the diameter """
        return cls(the_diameter / 2)

class Sphere(Circle):
    def __str__(self):
        return "Sphere with radius: {}".format(self.radius)

    def __repr__(self):
        return "Sphere({})".format(self.radius)

    @property
    def volume(self):
        """ Calculate volume based on radius """
        return 4 / 3 * math.pi * (self.radius ** 3)

    @property
    def area(self):
        """ Calcuate area based on radius """
        return 4 * math.pi * (self.radius ** 2)