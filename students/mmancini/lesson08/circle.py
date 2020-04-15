#!/usr/bin/env python3

import math


###################################

class Circle:
    def __init__(self, in_radius):
        i = 0
        self.radius = in_radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, x):
        self.radius = x / 2
