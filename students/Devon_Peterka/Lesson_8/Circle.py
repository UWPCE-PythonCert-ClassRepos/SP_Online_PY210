#!/usr/bin/env python3

import math

class Circle(object):
    def __init__(self, input):
        self.radius = input

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
    
    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return (f'Circle with radius: {self.radius}')

    def __repr__(self):
        return (f'Circle({self.radius})')

    def __add__(self, circle):
        return Circle(self.radius + circle.radius)

    def __mul__(self, value):
        return Circle(self.radius * value)

    def __lt__(self, circle):
        return self.radius < circle.radius

    def __eq__(self, circle):
        return self.radius == circle.radius
    
    def __le__(self, circle):
        return self.radius <= circle.radius

class Sphere(Circle):
    def __str__(self):
        return(f'Sphere of radius: {self.radius}')
    
    def __repr__(self):
        return(f'Sphere({self.radius})')
    
    @property
    def volume(self):
        return (4/3 * math.pi * self.radius ** 2)

    @property
    def area(self):
        return 4 * math.pi * self.radius ** 2
