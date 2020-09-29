#!/usr/bin/env python3

#Test code for circle.py

import pytest
import math
from circle import *

# Step 1

def test_init():
    r = 5
    c = Circle(5)
    assert c.radius == 5


# Step 2

def test_diameter():
    c = Circle(5)
    assert c.diameter == 10


# Step 3

def test_diameter_radius_property():
    c = Circle(5)
    assert c.radius == 5
    assert c.diameter == 10

# Step 4

def test_area():
    c = Circle(5)
    assert c.area == 5*5*math.pi


# Step 5

def test_initialize_diameter():
    c = Circle.from_diameter(10)

    # test radius, area, diameter properties
    assert c.diameter == 10
    assert c.radius == 5
    assert c.area == 5*5*math.pi

    # test chaning radius updates diameter and area
    c.radius = 10
    assert c.diameter == 20
    assert c.area == 10*10*math.pi


# Step 6

def test__str__method():
    c = Circle(5)
    d = c.__str__()
    assert d == "Circle with radius: 5.000000"

def test__repr_method():
    c = Circle(5)
    repr(c)
    d = c.__repr__()
    assert d == "Circle(5)"


# Step 7

def test_add_function():
    c = Circle(5)
    c2 = Circle(5)
    c3 = c + c2
    assert c3.radius == 10

def test_multiplication_function():
    c = Circle(5)
    c2 = c * 5
    assert c2.radius == 25

    # test reverse order multiplication
    c3 = 5 * c
    assert c3.radius == 25


# Step 8

def test_less_than_equal():
    c = Circle(5)
    c2 = Circle(10)
    c3 = Circle(5)

    assert (c < c2)
    assert not (c2 < c3)
    assert not (c < c3)


def test_euqal():
    c = Circle(5)
    c2 = Circle(5)
    c3 = Circle(1)

    assert (c == c2)
    assert not (c == c3)



def test_sorting():
    circles = [Circle(5), Circle(2), Circle(12), Circle(2), Circle(7), Circle(56)]
    print(circles)

    circles.sort()
    print(circles)

    # test list got sorted properly
    assert circles == [Circle(2), Circle(2), Circle(5), Circle(7), Circle(12), Circle(56)]


# Step 9

def test_initialize_sphere():
    s = Sphere(5)

    assert s.radius == 5
    assert s.diameter == 10


def test_sphere__str__method():
    s = Sphere(5)
    d = s.__str__()
    assert d == "Sphere with radius: 5.000000"

def test_sphere__repr__method():
    s = Sphere(5)
    repr(s)
    d = s.__repr__()
    assert d == "Sphere(5)"


def test_volume_property():
    s = Sphere(5)
    assert s.volume == 4/3*math.pi*math.pow(s.radius, 3)
    with pytest.raises(AttributeError):
        s.volume = 10


def test_sphere_area_property():
    s = Sphere(5)
    assert s.area == 4*math.pi*math.pow(s.radius, 2)
    with pytest.raises(AttributeError):
        s.area = 10


def test_sphere_numerics():
    s = Sphere(5)
    s2 = Sphere(2)


    # check addition works
    s3 = s + s2
    print(s3)
    assert s3.radius == 7

    # check multiplication works
    s4 = s*2
    print(s4)
    assert s4.radius == 10

    s5 = 2*s
    print(s5)
    assert s5.radius == 10


def test_total_ordering():
    s = Sphere(5)
    s2 = Sphere(10)
    s3 = Sphere(15)

    # check total ordering
    assert s < s3
    assert s3 > s
    assert s2 < s3


def test_sorting():
    s = Sphere(5)
    s2 = Sphere(7)
    s3 = Sphere(10)
    s4 = Sphere(12)
    s5 = Sphere(25)
    s6 = Sphere(30)

    spheres = [s2, s, s5, s4, s6, s3]
    print(spheres)

    spheres.sort()
    print(spheres)

    assert spheres == [s, s2, s3, s4, s5, s6]

def test_from_diameter():
    s = Sphere.from_diameter(10)
    assert s.radius == 5
    assert s.diameter == 10
