#!/usr/bin/env python
import pytest
from circle import *

def test_step1_radius():
    c = Circle(5)
    assert c.radius == 5

def test_step2_diameter():
    c = Circle(5)
    assert c.diameter == 10

def test_step3_assign_diameter():
    c = Circle(5)
    assert c.diameter == 10
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

def test_step4_area():
    c = Circle(2)
    assert c.area == 12.566370

def test_step5_create_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_step6_print_circle():
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4.00000'
    #assert repr(c) == 'Circle(4)'
    #assert eval(repr(c)) == Circle(4)

def test_step7_add_mult_circles():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 + c2).radius == Circle(6).radius
    assert (c2 * 3).radius == Circle(12).radius

def test_step8_compare_circles():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 > c2) == False
    assert (c1 < c2) == True
    assert (c1 == c2) == False
    c3 = Circle(4)
    assert (c2 == c3) == True
    circles = [Circle(5), Circle(2), Circle(9), Circle(6), Circle(4), Circle(1)]
    #assert circles.sort() == [Circle(1), Circle(2), Circle(4), Circle(5), Circle(6), Circle(9)]

def test_step9_sphere():
    s1 = Sphere(5)
    assert s1.radius == 5
    assert s1.diameter == 10
    assert str(s1) == 'Sphere with radius: 5.00000'
    #assert repr(c) == 'Sphere(5)'
    assert s1.volume == 523.59878
    assert s1.area == 314.15927
    assert Sphere.from_diameter(6).radius == 3