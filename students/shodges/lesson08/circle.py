#!/usr/bin/env python3

class Circle(object):
    _radius = None
    _diameter = None

    def __init__(self, radius):
        try:
            self._radius = float(radius)
            self._diameter = float(radius) * 2
        except ValueError:
            raise TypeError("radius expects a float")


    @property
    def radius(self):
        return self._radius


    @property
    def diameter(self):
        return self._diameter


    @radius.setter
    def radius(self, value):
        try:
            self._radius = float(value)
            self._diameter = float(value) * 2
        except ValueError:
            raise TypeError("radius expects a float")


    @diameter.setter
    def diameter(self, value):
        try:
            self._radius = float(value) / 2
            self._diameter = float(value)
        except ValueError:
            raise TypeError("radius expects a float")
