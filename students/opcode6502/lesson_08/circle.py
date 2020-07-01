# circle.py
# opcode6502: SP_Online_PY210

import math

class Circle():

    def __init__(self, radius):
        self.radius = radius

    @ property
    def area(self):
        return self.radius ** 2 * math.pi

    @area.setter
    def area(self, value):
        raise AttributeError

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
