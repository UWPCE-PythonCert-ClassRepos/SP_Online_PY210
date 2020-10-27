#!/usr/bin/env python3

# Testing circle.py

import math
import circle as cir

def test_check_rad_diameter():
    '''
    checks radius and diameter
    '''
    # initialized with radius 5
    c1 = cir.Circle(5)
    assert c1.radius == 5
    assert c1.diameter == 10

    # Set diameter
    c2 = cir.Circle()
    c2.diameter = 20
    assert c2.diameter == 20
    assert c2.radius == 10

def test_area():
    '''
    checks area
    '''
    c3 = cir.Circle(10)
    assert c3.area == math.pi * 10 ** 2


def test_circle_alter_constructor():
    '''
    checks from_diameter constructor
    '''
    c4 = cir.Circle().from_diameter(10)
    assert c4.radius == 5
    assert c4.diameter == 10

def test_printing():
    '''
    test printing
    '''
    c5 = cir.Circle(10)
    assert repr(c5) == "Circle(10)"
    assert str(c5) == "Circle with radius 10"


def test_circles_numeric_compare_sort():
    c6 = cir.Circle(4)
    c7 = cir.Circle(5)
    c8 = cir.Circle(5)
    assert (c6 < c7) is True
    assert (c6 > c7) is False
    assert (c7 == c8) is True
    c8.radius = 5 * 2
    assert c8.radius == 10
    assert c8.radius == c7.radius + c7.radius
    assert c8.radius == c7.radius * 2
    assert c8.radius == 2 * c7.radius
    circles = [cir.Circle(6), cir.Circle(7), cir.Circle(5)]
    assert circles[0].radius == 6
    assert circles[1].radius == 7
    assert sorted(circles) == [cir.Circle(5), cir.Circle(6), cir.Circle(7)]

def test_sphere():
    s = cir.Sphere(10)
    assert s.radius == 10
    assert s.diameter == 20
    assert s.area == 4 * math.pi * 10 ** 2
    assert s.volume == math.pi * pow(10,3) ** (4/3)
    s2 = cir.Sphere(4)
    s3 = cir.Sphere.from_diameter(8)
    assert s2.radius == s3.radius
    assert s2.area == s3.area
    assert s3.volume == s2.volume
