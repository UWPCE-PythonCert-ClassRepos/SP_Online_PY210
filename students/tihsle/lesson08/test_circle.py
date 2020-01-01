#!/usr/bin/env python3

"""

test script for circle class

From the exercise description:

Circle Class
The ultimate circle….

Goal:
The goal is to create a class that represents a simple circle.

A Circle can be defined by either specifying the radius or the diameter, and the user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area.
Print the circle and get something nice.
Be able to add two circles together.
Be able to compare two circles to see which is bigger.
Be able to compare to see if they are are equal.
(follows from above) be able to put them in a list and sort them.
You will use:

properties.
a bunch of “magic methods”.
a classmethod.

"""

import pytest
import math
from circle import Circle, Sphere

#step 1
def test_radius():
    c = Circle(4)
    assert c.radius == 4

#step 2
def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

#step 3
def test_user_diameter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

#step 4
def test_area():
    c = Circle(2)
    assert c.area == math.pi * 2 ** 2

#step 5
def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

#step 6
def test_print():
     c = Circle(4)
     assert c.__str__() == 'Circle with radius: 4'
     assert repr(c) == 'Circle(4)'

#step 7
def test_add_circles():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)
    assert c2 * 3 == Circle(12)

#step 8
def test_compare():
    c1 = Circle(4)
    c2 = Circle(8)
    assert not(c1 > c2)
    assert c1 < c2
    assert not(c1 == c2)
    c3 = Circle(4)
    assert c3 == c1

#step 9
def test_sphere():
    s = Sphere(4)
    assert s.volume()  == (4/3) * math.pi * 4 ** 3
    assert s.surface_area() == 4 * math.pi * 4 ** 2

#All together
test_radius()
test_diameter()
test_user_diameter()
test_area()
test_from_diameter()
test_print()
test_add_circles()
test_compare()
test_sphere()
