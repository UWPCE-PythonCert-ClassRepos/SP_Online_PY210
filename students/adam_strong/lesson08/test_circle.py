#!/usr/bin/env python3

"""
Tests for the circle

"""

from circle import *

# Step 1: Determine that a circle object can be made and a radius can be printed

def test_circle_object_instantiation():
    ''' Tests that you can make a Circle object '''
    c = Circle(5)
    assert c._radius == 5

def test_diameter_from_radius():
    ''' Tests that you can calculate diameter from inputted radius'''
    c = Circle(5)
    assert c.diameter == 10

def test_radius_updates_from_diameter():
    ''' Tests that you can change the diameter and then have it change
    the radius of the circle object'''
    c = Circle(5)
    c.diameter = 20
    assert c._radius == 10

def test_greater_than_zero():
    '''Tests that your value must be zero or greater'''
    try:
        c = Circle(-5)
        assert 0
    except ValueError:
        pass

def test_area():
    '''Tests area calculated from circle object'''
    c = Circle(5)
    assert c.area == 78.53981633974483

def test_cannot_set_area():
    '''Tests that an attribute error was called when trying to set area'''
    c = Circle(5)  
    try:
        c.area = 500
        assert 0
    except AttributeError:
        pass

def test_repr():
    '''Tests that the __repr__ is set '''
    c = Circle(5)
    assert repr(c) == 'Circle(5)'

def test_add():
    '''Tests that two Circle objects can be added'''
    c1 = Circle(5)
    c2 = Circle(4)
    c3 = c1 + c2
    assert c3._radius == 9

def test_multiply():
    '''Tests that a circle times an integer multiplies the radius by that much 
    in a new circle object. Test ensures it works in both:
     a 5 * Circle(x) and a Circle(x) * 5 method'''
    c1 = Circle(5)
    multicircle1 = 5 * c1
    multicircle2 = c1 * 4
    assert multicircle1._radius == 25
    assert multicircle2._radius == 20

def test_equivilency():
    c1 = Circle(5)
    c2 = Circle(5)
    assert c1 == c2

def test_sorting():
    '''Tests that __lt__ has been defined for Circle objects'''
    circles = [Circle(10), Circle(4), Circle(3), Circle(11), Circle(5)]
    circles = sorted(circles)
    string = circles.__str__()
    assert string == '[Circle(3), Circle(4), Circle(5), Circle(10), Circle(11)]'

def test_sphere():
    s1 = Sphere(5)
    c1 = Circle(5)
    assert s1._radius == 5
    assert s1.diameter == 10
    assert s1.area == 314.1592653589793
    assert s1.volume == 523.5987755982989
    assert c1.area == 78.53981633974483
    try:
        c1.volume
        assert 0
    except AttributeError:
        pass

def test_sphere_repr():
    '''Tests that the __repr__ is set for Sphere objects'''
    c = Sphere(5)
    assert repr(c) == 'Sphere(5)'

def test_from_diameter():
    cD = Circle.from_diameter(10)
    sD = Sphere.from_diameter(10)
    assert cD._radius == 5
    assert cD.area == 78.53981633974483
    assert sD._radius == 5
    assert sD.area == 314.1592653589793