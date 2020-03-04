#!/usr/bin/env python3


import math




class Circle(object):
    radius = ()

    def __init__(self, radius):
        try:
            self.radius = float(radius)
            if self.radius <= 0:
                print("Must use a positive interger")
                raise ValueError
        except TypeError:
            raise TypeError


    @property
    def diameter(self):
        return self.radius * 2

    # def expand(self, factor=2):
    #     self.diameter = self.diameter * factor
    #     return None  # note that if you leave that off, it will still return None
    #
    # def area(self):
    #     area = (self.diameter / 2)**2 * math.pi
    #     return area