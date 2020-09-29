#!/usr/bin/env python3

import numpy as np






class Circle(object):

    tag = "Circle"
    
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, var):
        self.radius = var / 2

    @property
    def area(self):
        return (3.14 * self.radius * self.radius)

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(repr(self.radius))

    def __add__(self, other):
        s_val = str(self.radius + other.radius)
        print (("{}(" + s_val + ")").format(self.tag))

# I couldn't figure out how to put number first and get a result (3 * c2)
    def __mul__(self, other):
        if type(other) == int:
            m_val = str(self.radius * other)
            print (("{}(" + m_val + ")").format(self.tag))

    def __lt__(self, other):
        return self.radius < other.radius


class Sphere(Circle):

    tag = "Sphere"

    def __str__(self):
        return "Sphere with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Sphere({})".format(repr(self.radius))

    @property
    def valume(self):
        vpi = (4/3) * 3.14
        return (vpi * self.radius**3)

    @property
    def area(self):
        return (4 * 3.14 * self.radius * self.radius)
