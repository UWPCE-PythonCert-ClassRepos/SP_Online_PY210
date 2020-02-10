# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 20:14:33 2020

@author: travel_laptop
"""
import math

class Circle(object):
    
    def __init__(self, radius):
        self._radius = radius
        
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, new_radius):
        if new_radius >= 0:
            self._radius = new_radius
        else:
            raise ValueError
            
    @property
    def diameter(self):
        return self._radius*2
    @diameter.setter
    def diameter(self, new_diameter):
        if new_diameter >= 0:
            self._radius = new_diameter / 2
        else:
            raise ValueError
    
    @property
    def area(self):
        return math.pi * self._radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)