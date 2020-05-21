#!/usr/bin/env python3

# Stella Kim
# Assignment 7: The Circle Class

import math

"""
A class based program that represents a simple circle.
"""
# User can use radius or diameter to query the circle's dimensions
# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare to see if they are are equal
# (follows from above) be able to put them in a list and sort them


class Circle(object):
    def __init__(self, radius):  # circle is defined by specifying radius
        self.radius = radius
        # print('Circle radius:{:.2f}'.format(round(self.radius)))

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
