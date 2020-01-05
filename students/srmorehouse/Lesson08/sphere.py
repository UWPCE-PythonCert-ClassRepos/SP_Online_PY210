#!/usr/bin/env python3

from circle import Circle
import math

####################################################
# Lesson 08
# Steve Morehouse
####################################################

class Sphere(Circle):

    @property
    def volume(self):
        return 4/3 * math.pi * self.radius**3


    @property
    def area(self):
        return 4 * math.pi * self.radius**2


    def __str__(self):
        return f"Sphere with radius: {self.radius}"


    def __repr__(self):
        return f"Sphere({self.radius})"
 
