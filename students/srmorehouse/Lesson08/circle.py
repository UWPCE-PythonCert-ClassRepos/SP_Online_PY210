#!/usr/bin/env python3

import math

####################################################
# Lesson 08
# Steve Morehouse
####################################################

class Circle (object):

    def __init__ (self, radius):
        if radius <=0:
            raise ValueError ('radius needs to be positive')
        else:
            self.radius = float (radius)

    @property
    def diameter (self):
        return self.radius * 2

    @property
    def area (self):
        return (self.radius**2) * math.pi

    @diameter.setter
    def diameter (self, diameter):
        self.radius = diameter / 2

    @classmethod
    def using_diameter (cir, diameter):
        return cir (diameter / 2)

