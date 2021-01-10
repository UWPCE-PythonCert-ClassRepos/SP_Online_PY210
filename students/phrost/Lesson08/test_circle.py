#!/usr/bin/env python

#Lesson 8 Test Circle

from circle import *

import pytest

#Step 1
def test_init():
    c = Circle(7)
    assert c.radius ==7

#Step 2

def test_diameter():
    c = Circle(2)
    assert c.diameter ==4

#Step 3
def test_set_diameter():
    c = Circle(6)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

#Step 4
def test_area():
    c = Circle(4)
    assert c.area == pytest.approx(50.265482)

#Step 5
def test_from_diameter():
    c = Circle.from_diameter(10)
    assert c.diameter == 10
    assert c.radius == 5

#Step 6
def test_desc():
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4.000'
    assert repr(c) == "Circle(4)"

#Step 7
def test_operator():
    c1 = Circle(10)
    c2 = Circle(10)
    assert repr (c1 + c2) == 'Circle(20)'
    assert c1 * 2 == Circle(20)
    assert repr(2 * c1) == 'Circle(20)'

#Step 8
def test_rela():
    c1 = Circle(5)
    c2 = Circle (10)
    assert c1 < c2
    assert c2 > c1
    assert (c1 == c2) is False
    c2 = Circle (20)
    assert (c1 > c2) is False
    c1 = Circle(20)
    assert c1 == c2

def test_sort():
    circle_list = [Circle(8), Circle(1), Circle(3)]
    circle_list.sort()
    assert circle_list == [Circle(1), Circle(3), Circle(8)]

#Step 8 Bonus
def test_reflected():
    c1 = Circle(7)
    assert c1 * 3 == 3 * c1
    
def test_add():
    c1 = Circle(4)
    c2 = Circle(1)
    c1 += c2
    assert c1 == Circle(5)
    
def test_mul():
    c1 = Circle(7)
    c1 *= 4
    assert c1 == Circle(28)

