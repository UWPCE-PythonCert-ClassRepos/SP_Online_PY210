#!/usr/bin/env python3

class Circle(object):
    radius = 0

    def __init__(self, radius):
        try:
            self.radius = float(radius)
        except ValueError:
            raise TypeError("radius expects a float")
