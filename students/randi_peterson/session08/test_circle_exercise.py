import pytest

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

#MAKE A TEST TO TEST AREA