#!/usr/bin/env python3

"""
A class-based system for rendering a circle.
"""

import math

class Circle(object):
    def __init__(self, rad=None):
        if rad is None:
            raise AttributeError
        else:
            self.radius = rad

    @property
    def diameter(self):
        return 2 * self.radius