"""
test code for circle_class.py

"""
import io
import pytest
import math

from circle_class import *

## step 1 ##

def test_circle_init():
    c = Circle(5)
    assert c.radius == 5

## step 2, 3 ##

def test_diamter():
    c = Circle(10)
    assert c.diameter == 20

def test_radius_sync_diamater():
    c = Circle(5)
    c.diameter = 2
    assert c.radius == 1

## step 4 ##
def test_area():
    c = Circle(2)
    assert c.area == math.pi*2*2

## step 5 ##
def test_alternate_construct():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

## step 6 ##
def test_print():
    c = Circle(20.1)
    assert c.__str__() == 'Circle with radius: 20.100000'
    assert c.__repr__() == 'Circle(20.1)'

## step 7 ##
def test_operator_overloading():
    c= Circle (20)
    d= Circle (10)
    assert c+d == Circle(30)
    assert 5*d == Circle(50)

## step 8 ##
def test_compare():
    c= Circle (20)
    d= Circle (10)
    e= Circle (20)
    assert c > d 
    assert d < c 
    assert c == e 
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

## step 9 ##
def test_sphere_init():
    s = Sphere(5)
    assert s.radius == 5

def test_sphere_volume():
    s = Sphere(1)
    assert s.volume == (4/3)*math.pi

def test_sphere_compare():
    c= Sphere(20)
    d= Sphere(10)
    e= Sphere(20)
    assert c > d 
    assert d < c 
    assert c == e 




  