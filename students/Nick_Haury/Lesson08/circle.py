#!/usr/bin/env python3
import math

"""
Lesson08 assignment; creating a class to represent
a circle.  The class should be capable of the following:
- computing the circles area
- priting the circle "pretty"
- adding two circles together
- sort circles
- compare if circles are equal
"""

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius

    def __repr__(self):
        return str(self.radius)