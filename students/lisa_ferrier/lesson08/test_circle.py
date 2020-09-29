#!/usr/bin/env python
# test_circle.py
# L Ferrier
# Python 201, Assignment 08

import pytest
from circle import*


########
# step 1
########

def test_circle():
    c = Circle(4)
    s = Sphere(4)
    # print(c.radius)

    assert c.radius == 4
    assert s.radius == 4

########
# step 2
########

def test_diameter():
    c = Circle(4)
    s = Sphere(8)
    print(c.diameter, s.diameter)

    assert c.diameter == 8
    assert s.diameter == 16

########
# step 3
########

def test_diameter_setter():
    c = Circle(4)
    c.diameter = 2
    print(c.radius, c.diameter)

    assert c.diameter == 2
    assert c.radius == 1

    s = Sphere(4)
    s.diameter = 2
    assert s.diameter == 2
    assert s.radius == 1


########
# step 4
########

def test_area():
    c = Circle(2)
    s = Sphere(2)
    assert c.area == 12.566370614359172
    assert s.area == 50.26548245743669


########
# step 5
########

def test_from_diameter():
    c = Circle.from_diameter(8)
    print(c.diameter)

    assert c.radius == 4

    s = Sphere.from_diameter(8)
    print (s.diameter)

    assert s.radius == 4


########
# step 6
########

def test_str():
    c = Circle(4)
    s = Sphere(5)
    print(str(c))

    assert str(c) == 'Circle with radius: 4'
    assert str(s) == 'Sphere with radius: 5'


def test_repr():
    c = Circle(4)
    s = Sphere(5)
    print(repr(c))

    assert repr(c) == 'Circle(4)'
    assert repr(s) == 'Sphere(5)'


########
# step 7
########

def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    # print(repr(c1 + c2))
    assert repr(c1 + c2) == 'Circle(6)'
    assert repr(Circle(3) + c2) == 'Circle(7)'

    s1 = Sphere(2)
    s2 = Sphere(4)
    assert repr(s1 + s2) == 'Sphere(6)'
    assert repr(Sphere(3) + s2) == 'Sphere(7)'


def test_mul():
    c1 = Circle(2)
    c2 = Circle(4)

    assert repr(c1 * 3) == 'Circle(6)'
    assert repr(3 * c2) == 'Circle(12)'


def test_div():
    c1 = Circle(4)
    s1 = Sphere(4)

    assert repr(c1 // 2) == 'Circle(2)'
    assert repr(s1 // 2) == 'Sphere(2)'

    # check to make sure floats are rounded to nearest int
    assert repr(c1 // 3) == 'Circle(1)'
    assert repr(s1 // 3) == 'Sphere(1)'


########
# step 8
########

def test_compare():
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = Circle(4)
    c4 = Circle(3)

    assert c1 < c4
    assert c2 > c1
    assert c1 == c4
    assert c3 != c4

    s1 = Sphere(2)
    s2 = Sphere(3)
    s3 = Sphere(4)
    s4 = Sphere(3)

    assert s1 < s4
    assert s2 > s1
    assert s1 == s4
    assert s3 != s4

def test_sort_circles():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

############################
# step 8 - optional features
############################

def test_reflection():
    c1 = Circle(4)
    assert c1 * 3 == 3 * c1

    s1 = Sphere(4)
    assert s1 * 3 == 3 * s1
