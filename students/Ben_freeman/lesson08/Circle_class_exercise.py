import math


class Circle(object):

    def __init__(self,radius_value):
        self.radius = radius_value

    @property
    def diameter(self):
        return 2*self.radius

    @diameter.setter
    def diameter(self,value):
        self.radius = value/2
    
    @property
    def area(self):
        return self.radius**2*math.pi

    @area.setter
    def area(selfs,value):
        raise AttributeError

    @classmethod
    def from_diameter(cls,value):
        return Circle(value/2)

    def __repr__(cls):
        return f"Circle({cls.radius})"

    def __str__(cls):
        return f"Circle with radius: {cls.radius}"

