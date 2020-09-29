#!/usr/bin/env python3
""" Lesson 8, Excercise 1

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/circle_class.html

Description:
    Creating circle class and a sphere sub-class
"""
import math

class Circle(object):
    # @classmethod
    def __init__(self, the_radius=0):
        self.radius = the_radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2.0)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,radius):
        self._radius = radius
    
    @property
    def diameter(self):
        return self._radius *2.0
    
    @diameter.setter
    def diameter(self,diameter):
        self._radius = diameter/2.0

    @property
    def area(self):
        return self._radius*2.0*math.pi

    def __str__(self):
        return f"Circle with radius: {self.radius:.6f}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)
    
    def __mul__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)
        elif isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        else:
            raise TypeError("Invalid operator")
    
    def __rmul__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)
        elif isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        else:
            raise TypeError("Invalid operator")

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self, other):
        if isinstance(other, int):
            return self.radius == other
        elif isinstance(other, Circle):
            return self.radius == other.radius
        else:
            raise TypeError("Invalid Operator")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.radius = self.radius + other
        elif isinstance(other, Circle):
            self.radius = self.radius + other.radius
        else:
            raise TypeError("Invalid Operator")

        return self.radius

    def __imult__(self, other):
        if isinstance(other, int):
            self.radius = self.radius * other
        elif isinstance(other, Circle):
            self.radius = self.radius * other.radius
        else:
            raise TypeError("Invalid Operator")

        return self.radius

class Sphere(Circle):
    
    @property
    def area(self):
        raise NotImplementedError  

    @property
    def volume(self):
        return 4/3 * math.pi * (self.radius**3)

    def __str__(self):
        return f"Sphere with radius: {self.radius}"

    def __repr__(self):
        return f"Sphere({self.radius})"

