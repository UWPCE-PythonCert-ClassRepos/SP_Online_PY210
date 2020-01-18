#test cases

import pytest


from circle import *

def test_circle_radius():
    c = Circle(4)
    assert c.radius == 4

def test_circle_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_circle_diameter_setter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

def test_circle_area():
    c = Circle(2)
    assert c.area == 12.566370614359172

def test_circle_area_set():
    with pytest.raises(AttributeError):
        c = Circle(2)
        c.area = 42

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

    
def test_rep_circle():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'
    d = eval(repr(c))
    assert d.radius == 4

def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(c1 + c2) == repr(Circle(6))


def test_multiply():
    c1 = Circle(4)
    assert repr(c1 * 3) == repr(Circle(12))

def test_lessthan():
    c1 = Circle(4)
    c2 = Circle(12)
    assert c1 < c2

def test_greaterthan():
    c1 = Circle(4)
    c2 = Circle(12)
    assert c2 > c1


def test_equal():
    c1 = Circle(12)
    c2 = Circle(12)
    assert c1 == c2

def test_sort():
    list_of_circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    list_of_circles.sort(key=Circle.sort_key)
    assert list_of_circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

#Sphere class tests
def test_sphere():
    s1 = Sphere(4)
    assert s1.radius == 4 

def test_sphere_volume():
    s1 = Sphere(4)
    assert s1.volume == 268.082573106329


def test_rep_sphere():
    s = Sphere(4)
    assert repr(s) == 'Sphere(4)'
    d = eval(repr(s))
    assert d.radius == 4


def test_sphere_area():
    s = Sphere(4)
    assert s.surface_area == 201.06192982974676

def test_add_sphere():
    s1 = Sphere(2)
    s2 = Sphere(4)
    assert repr(s1 + s2) == repr(Sphere(6))


def test_multiply_sphere():
    s1 = Sphere(4)
    assert repr(s1 * 3) == repr(Sphere(12))

def test_lessthan_sphere():
    s1 = Sphere(4)
    s2 = Sphere(12)
    assert s1 < s2

def test_greaterthan_sphere():
    s1 = Sphere(4)
    s2 = Sphere(12)
    assert s2 > s1


def test_equal_sphere():
    s1 = Sphere(12)
    s2 = Sphere(12)
    assert s1 == s2

def test_sort_sphere():
    list_of_spheres = [Sphere(6), Sphere(7), Sphere(8), Sphere(4), Sphere(0), Sphere(2), Sphere(3), Sphere(5), Sphere(9), Sphere(1)]
    list_of_spheres.sort(key=Sphere.sort_key)
    assert list_of_spheres == [Sphere(0), Sphere(1), Sphere(2), Sphere(3), Sphere(4), Sphere(5), Sphere(6), Sphere(7), Sphere(8), Sphere(9)]


