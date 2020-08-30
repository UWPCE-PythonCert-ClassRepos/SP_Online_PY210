#!/usr/bin/env python
#test code for circle assignment

from circle import *


#######1- test if object can be made and returns the right radius or not####

def test_circle_object():
    c=Circle(5)
    assert c.radius == 5

def test_cal_diameter():
    c=Circle(5)
    #diameter=c.cal_diameter(5)
    assert c.diameter == 10

def test_set_diamter():
    c=Circle(10)
    c.diameter=20
    assert c.diameter == 20
    assert c.radius == 10

def test_area():
    c=Circle(2)
    assert c.area == 12.566370614359172
    try:
        c.area=42
    except AttributeError:
        print("Can not set value for area")

def test_from_diameter():
    c=Circle.from_diameter(8)
    assert c.radius == 4
    assert c.diameter == 8

def test_str_repr():
    c=Circle(8)
    assert str(c)  == "Circle with radius:8"
    assert repr(c) == "'Circle(8)'"

def test_add_mul():
    c1 = Circle(2)
    c2 = Circle(4)

    assert (c1 + c2).radius == 6
    assert (c1 * 4).radius == 8

def test_lt_eq():
    c1=Circle(3)
    c2=Circle(8)

    assert (c1 > c2) == False
    assert (c1 == c2) == False
    assert (c1 < c2) == True

    c3=Circle(8)

    assert (c2 == c3) == True

def test_sort():
    circles=[Circle(18),Circle(16)]#,Circle(4),Circle(11),Circle(30)]
    circles=sorted(circles)
    sorted_circle=circles.__str__()
    assert sorted_circle == "['Circle(16)', 'Circle(18)']"#"['Circle(4)''Circle(11)''Circle(16)''Circle(18)''Circle(30)']"



def test_sphere_str():
    s=Sphere(3)

    assert s.radius == 3
    assert s.diameter == 6
    assert s.area == 113.09733552923255
    assert s.volume == 113.09733552923254

def test_sphere_from_diameter():
    s=Sphere.from_diameter(12)
    c=Circle.from_diameter(10)
    
    assert s.radius == 6
    assert c.radius == 5

