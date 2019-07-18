#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 17:10:25 2019

@author: humberto
"""

import math
pi = math.pi


class Circle:
    def __init__(self,radius):
        self._radius = radius
        self._diameter = self._radius*2
        self._area = 2*pi*self._radius
    
    def __str__(self):
        return "Circle with radius: {}".format(self._radius)
    
    def __repr__(self):
        return "Circle({})".format(self._radius)
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self,radius):
        self._radius = radius
        self._area = 2*pi*self._radius
    
    @property
    def diameter(self):
        return 2*self._radius
    
    @diameter.setter
    def diameter(self,diameter):
        self._radius = diameter/2
        self._area = 2*pi*self._radius
    
    @property
    def area(self):
        return self._area
    
    @classmethod
    def from_diameter(cls,diameter):
        self = cls(diameter/2)
        return self
    
    def __add__(self,other):
        return Circle(self._radius+other._radius)
    
    def __mul__(self,val):
        return Circle(val*self._radius)
    
    def __lt__(self,other):
        return self._radius > other._radius
    
    def __eq__(self,other):
        return self._radius == other._radius


class Sphere(Circle):
    
    def __str__(self):
        return "Sphere with radius: {}".format(self._radius)
    
    def __repr__(self):
        return "Sphere({})".format(self._radius)
    
    @property
    def area(self):
        return (self._radius**2)*(4/3)*(pi)
    
    @classmethod
    def from_diameter(cls,diameter):
        self = cls(diameter/2)
        return self
