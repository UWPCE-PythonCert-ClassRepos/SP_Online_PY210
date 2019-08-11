#!/usr/bin/env python3

"""
Test for a class-based circle/sphere maker
"""

from circle import *

def test_str_dunder():
    s = Sphere(9.99)
    assert s.__str__() == "Sphere with a radius of: 9.99"

def test_repr_dunder():
    s = Sphere(9.99)
    assert s.__repr__() == "Sphere(9.99)"

def test_sphere_volume():
    s1 = Sphere(9)
    assert '{0:.2f}'.format(s1.volume) == '3053.63'

def test_sphere_area():
    s1 = Sphere(9)
    assert '{0:.2f}'.format(s1.area) == '1017.88'