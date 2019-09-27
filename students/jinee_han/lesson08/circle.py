#!/usr/bin/env python3

from math import pi

class Circle:

    '''
    A circle class
    '''

    def __init__(self, radius_value):
        ''' Initialize a new instance of the Circle class '''

        self.radius = radius_value


    @property
    def diameter(self):
        '''
        Diameter property
        :return: the diameter of the circle
        '''

        return self.radius * 2


    @diameter.setter
    def diameter(self, diameter_value):
        '''
        Set the diameter value
        :param diameter_value: the diameter value
        :return: nothing
        '''

        self.radius = diameter_value / 2


    @property
    def area(self):
        '''
        The circle area property
        :return: The area of the circle
        '''

        return pi * self.radius ** 2


    @classmethod
    def from_diameter(cls, diameter_value):
        '''
        The diameter constructor
        :param diameter_value: The diameter value of the circle
        :return: a Circle object specified with the desired diameter / radius
        '''

        return cls(diameter_value / 2)


    def __str__(self):
        '''
        Override the string method
        :return: The desired string format
        '''

        return "Circle with radius: {}".format(self.radius)


    def __repr__(self):
        '''
        Override the representation method
        :return: The desired representation
        '''

        return "Circle({})".format(self.radius)


    def __add__(self, other):
        '''
        Override the add method
        :param other: The other object to add
        :return: a Circle with the current radius added to the other radius
        '''

        return Circle(self.radius + other.radius)


    def __mul__(self, other):
        '''
        Override the multiplication method
        :param other: The other scalar to multiply
        :return: a Circle with the current radius multiplied by the other factor
        '''

        return Circle(self.radius * other)


    def __gt__(self, other):
        '''
        Override the greater than method
        :param other: The other object to compare
        :return: True if self is greater than other radius
        '''

        return self.radius > other.radius


    def __ge__(self, other):
        '''
        Override the greater than or equal method
        :param other: The other object to compare
        :return: True if self is greater than or equal to other radius
        '''

        return self.radius >= other.radius


    def __lt__(self, other):
        '''
        Override the less than method
        :param other: The other object to compare
        :return: True if self is less than other radius
        '''

        return self.radius < other.radius


    def __le__(self, other):
        '''
        Override the less than or equal than method
        :param other: The other object to compare
        :return: True if self is less than or equal to other radius
        '''

        return self.radius <= other.radius


    def __eq__(self, other):
        '''
        Override the equal method
        :param other: The other object to compare
        :return: True if two objects are equal, false if not
        '''

        return self.radius == other.radius


class Sphere(Circle):

    '''
    A sphere subclass derived from a Circle class
    '''

    def __str__(self):
        '''
        Override the string method
        :return: The sphere's string formatting
        '''
        return "Sphere with radius: {}".format(self.radius)


    def __repr__(self):
        '''
        Override the representation method
        :return: The sphere's representation
        '''
        return "Sphere({})".format(self.radius)
    
    
    @property
    def volume(self):
        '''
        Calculate the volume of a sphere
        :return: The volume of a sphere for the given radius
        '''
        # volume of a sphere is: 4/3 pi r^3
        return 4 / 3 * pi * self.radius ** 3


    @property
    def area(self):
        '''
        Calculate the surface area
        :return: the surface area for the given radius
        '''
        return 4 * pi * self.radius ** 2
