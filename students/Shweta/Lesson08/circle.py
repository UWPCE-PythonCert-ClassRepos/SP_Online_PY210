#!/usr/bin/env python

#circel program assignment for lesson08

import math

class Circle(object):
    def __init__(self,radius):
        self.radius=radius
       # self._radius=radius

    @classmethod 
    def from_diameter(cls,_diameter):
        #self=cls()
        radius = _diameter/ 2
        return cls(radius)
    @property
    def diameter(self):
        #self.diameter=self.radius*2
        diameter=self.radius*2
        return diameter
    
    @diameter.setter
    def diameter(self,value):
        self.radius = value / 2
        #return value


    @property
    def area(self):
        area=(self.radius ** 2)*math.pi
        return area

    def __str__(self):
        return "Circle with radius:" + str(self.radius)

    def __repr__(self):
        return f"'{self.__class__.__name__}({self.radius})'"

    def __add__(self,other):
        return Circle(self.radius + other.radius)

    def __mul__(self,other):
        return Circle(self.radius * other)
    def __lt__(self,other):
        return (self.radius < other.radius)
    def __eq__(self,other):
        return(self.radius == other.radius)


    

class Sphere(Circle):

    def __str__(self):
        return "Sphere radius {} and diameter is {}".format(self.radius,self.diameter)
    def __repr__(self):
        return "Sphere()".format(self.radius)
    @property
    def area(self):
        return (self.radius ** 2) * math.pi * 4

    @property
    def volume(self):
        return (self.radius ** 3) *math.pi * (4/3)




c=Circle(5)
print(c.radius)
print(c.diameter)

c.diameter = int(20)
print(c.radius)
print(c.diameter)

c=Circle(2)
print(c.area)

c=Circle.from_diameter(4)
print(c.radius)
print(c.diameter)

c=Circle(4)
print(c)

print(repr(c))


c1=Circle(4)
c2=Circle(2)

print(c1 + c2)
print(c1 * 3)
print(c1 > c2)
print(c1 == c2)

