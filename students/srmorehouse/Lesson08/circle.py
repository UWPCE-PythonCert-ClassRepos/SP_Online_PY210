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
        return self.radius * math.pi

    @diameter.setter
    def diameter (self, diameter):
        self.radius = diameter / math.pi

