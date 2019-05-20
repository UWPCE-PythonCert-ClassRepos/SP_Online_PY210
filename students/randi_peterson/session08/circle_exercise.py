from math import pi

class Circle():
    def __init__(self,radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2*self.radius

    @diameter.setter
    def diameter(self,value):
        self.radius = value/2

    @property
    def area(self):
        return pi*(self.radius)**2



