#!/usr/bin/env python3

class Circle(object):
    radius = 0

    def __init__(self, radius):
        if str(radius).isnumeric is False:
            raise TypeError
        self.radius = radius
