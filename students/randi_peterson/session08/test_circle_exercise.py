import pytest
from math import pi

from circle_exercise import *

def test_create_circle(rad = 3):
    #Tests creation of a circle of specified radius
    c = Circle(rad)
    assert c.radius == rad

def test_get_diameter(rad = 3):
    #Tests getting diameter when creating a circle of a given radius
    c = Circle(rad)
    assert c.diameter == 6

def test_change_diameter(rad = 3, val = 4):
    #Test if radius and diameter get updated with user input
    c = Circle(rad)
    assert c.radius == 3
    assert c.diameter == 6

    c.diameter = val
    assert c.diameter == 4
    assert c.radius == 2

def test_area(rad = 3):
    #Tests if the area calculation is correct
    c = Circle(rad)
    assert c.area == pi * rad**2

def test_diam_constructor(diam = 6):
    #Tests if circle can be created from diameter instead
    c = Circle.from_diameter(diam)
    assert c.radius == 3
    assert c.diameter == 6

def test_str_method(rad=3):
    #Tests str method of the Circle class
    c = Circle(rad)
    assert str(c) == 'Circle with radius: 3.00'

def test_repr_method(rad=3):
    #Tests repr method of the Circle class
    c = Circle(rad)
    assert repr(c) == 'Circle(3)'

def test_add(rad1=2,rad2=4):
    #Test add method
    c1 = Circle(rad1)
    c2 = Circle(rad2)
    assert c1 + c2 == Circle(6)

def test_multiply(rad1=2,val=3):
    #Test multiplication
    c1 = Circle(rad1)
    assert c1 * val == Circle(6)
    assert val * c1 == Circle(6)

def test_less_than(rad1=2,rad2=4):
    #Test less than and greater than features
    c1 = Circle(rad1)
    c2 = Circle(rad2)
    assert c1 < c2
    assert c2 > c1

def test_sort(rad1=1,rad2=2,rad3=3,rad4=4):
    #Test the sort function
    c1 = Circle(rad1)
    c2 = Circle(rad2)
    c3 = Circle(rad3)
    c4 = Circle(rad4)
    circles = [c4, c2, c3, c1]
    circles.sort()
    assert circles == [c1,c2,c3,c4]

def test_sphere(rad = 3):
    #Test a sphere can be created and has volume and str and repr methods
    s = Sphere(rad)
    assert s.radius == 3
    assert s.volume == (4/3)*pi*s.radius**3
    assert str(s) == 'Sphere with radius: 3.00'
    assert repr(s) == 'Sphere(3)'
    assert s.area == 4*pi*s.radius**2