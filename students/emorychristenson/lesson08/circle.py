#!/usr/bin/env python3

import math

class Circle(object):

    def __init__(self, radius):
        """ Instantiate the circle """
        self.radius = radius

    def __str__(self):
        """ Pretty printing! """
        return "Circle with radius {:.2f}".format(self.radius)

    def __repr__(self):
        """ Representational string! (this was a new one for me) """
        return "Circle({})".format(self.radius)

    def __add__(self, circle2):
        """ Addition functionality """
        total = self.radius + circle2.radius
        return Circle(total)

    def __mul__(self, number):
        """ Multiply functionality """
        total = self.radius * number
        return Circle(total)
    
    def __rmul__(self, number):
        """ Right hand multiply functionality """
        total = number * self.radius
        return Circle(total)

    def __lt__(self, circle2):
        """ Less than comparator """
        if self.radius < circle2.radius:
            return True
        else:
            return False

    def __gt__(self, circle2):
        """ Greater than comparator """
        if self.radius > circle2.radius:
            return True
        else:
            return False

    def __eq__(self, circle2):
        """ Equals comparator """
        if self.radius == circle2.radius:
            return True
        else:
            return False

    @property
    def diameter(self):
        """ Calculate the diameter """
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, the_diameter):
        """ Set the diameter """
        self.radius = the_diameter / 2

    @property
    def area(self):
        """ Calculate area """
        return math.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        """ Class method for creating the circle from the diameter """
        return cls(diameter / 2)


class Sphere(Circle):

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        """ Pretty printing! """
        return "Sphere with radius {:.2f}".format(self.radius)

    def __repr__(self):
        """ Representational string! (this was a new one for me) """
        return "Sphere({})".format(self.radius)

    @property
    def volume(self):
        """ Calculate the volume """
        return 4 / 3 * math.pi * (self.radius ** 3)

    @property
    def area(self):
        """ Calculate surface area """
        return 4 * math.pi * (self.radius ** 2)
