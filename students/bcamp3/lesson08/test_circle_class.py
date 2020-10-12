#!/usr/bin/env python3

from circle_class import *


def test_init():
    """
    This tests that it can be initialized with a diameter input
    """
    c = Circle(1)
    assert c.diameter == 2.0
    assert c.radius == 1.0
    assert f"{c.area:.5f}" == "3.14159"


def test_repr():
    c = Circle(1)
    assert c.__repr__() == "Circle(1)"
    assert c.__str__() == ' This is a Circle object:\n diameter =   2.0000\n     area =   3.1416'


def test_compare():
    a = Circle(2)
    b = Circle(4)
    c = Circle(2)
    assert a < b
    assert b > a
    assert a == c

def test_sort():
    a = Circle(7)
    b = Circle(4)
    c = Circle(5)
    assert sorted([a, b, c], key=Circle.sort_key) == [b, c, a]


def test_from_diammeter():
    c = Circle.from_diameter(2)
    assert c.radius == 1.0
    assert c.diameter == 2.0
    assert f"{c.area:.5f}" == "3.14159"


def test_add():
    a = Circle(2)
    b = Circle(4)
    c = a + b
    assert c.radius == 6.0
    assert c.diameter == 12.0
    assert f"{c.area:.5f}" == "113.09734"
    a += b
    assert a == c
    b += 1
    assert b == (c-1)
    assert b == (Circle(10) - Circle(5))


def test_mul():
    a = Circle(2)
    c = a * 3
    assert c.radius == 6.0
    assert c.diameter == 12.0
    assert f"{c.area:.5f}" == "113.09734"
    a *= 3
    assert a == c


def test_rmul():
    a = Circle(2)
    c = 3 * a
    assert c.radius == 6.0
    assert c.diameter == 12.0
    assert f"{c.area:.5f}" == "113.09734"
    assert a * 3 == 3 * a


def test_div():
    a = Circle(12)
    b = Circle(3)
    assert a / b == Circle(4)
    assert a / 4 == Circle(3)
    

def test_sphere_repr():
    c = Sphere(1)
    assert c.__repr__() == "Sphere(1)"
    assert c.__str__() == (' This is a Sphere object:\n'
                           ' diameter =   2.0000\n'
                           '     area =  12.5664\n'
                           '   volume =   4.1888')


def test_sphere_from_diameter():
    c = Sphere.from_diameter(2)
    assert c.__str__() == (' This is a Sphere object:\n'
                           ' diameter =   2.0000\n'
                           '     area =  12.5664\n'
                           '   volume =   4.1888')


def test_sphere_sorting():
    a = Sphere(7)
    b = Sphere(4)
    c = Sphere(5)
    assert sorted([a, b, c], key=Sphere.sort_key) == [b, c, a]
