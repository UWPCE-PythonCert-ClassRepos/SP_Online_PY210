
import io
import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from circle import *

def test_circle_import_radius():
    c = Circle(4)
    assert c.radius == 4


def test_circle_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_diameter_set():
    c = Circle(8)
    c.diameter = 4
    assert c.diameter == 4
    assert c.radius == 2

def test_circle_area():
    c = Circle(2)
    assert c.area == 12.566370

def test_class_method():

    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_str_repr():

    c = Circle(4)
    d = eval(repr(c))
    print (c)
    assert str(c) == 'Circle with radius: 4.0000'
    assert repr(c) == 'Circle({})'.format(4)
    assert str(c)  == str(d)

def test_math_circle():
    c_1 = Circle(4)
    c_2 = Circle(2)
    print (3*c_2)
    assert repr(c_1+c_2) == 'Circle({})'.format(4+2)
    assert repr(c_1-c_2) == 'Circle({})'.format(4-2)
    assert repr(c_2-c_1) == 'Circle(0)'
    assert repr(c_2 *3) == 'Circle({})'.format(2*3)
    assert repr(3 *c_2) == 'Circle({})'.format(2*3)

def test_eq_circle():
    c_1 = Circle(4)
    c_2 = Circle(4)
    assert c_1 == c_2

def test_lt_circle():
    c_1 = Circle(3)
    c_2 = Circle(4)
    assert c_1 < c_2

def test_sort_key():
    c_1 = Circle(3)
    c_2 = Circle(4)
    c_3 = Circle(5)
    circles = [c_1, c_3, c_2]
    circles.sort()
    assert circles == [Circle(3),Circle(4),Circle(5)]

def test_augment_operators():
    c_1 = Circle(4)
    c_2 = Circle(5)
    c_1 += c_2
    assert c_1 == (Circle(4)+c_2)
    c_1 *= 2
    assert c_1 == (Circle(18))

def test_sphere():
    s_1 = Sphere(4)
    s_2 = Sphere(2)
    assert (s_1+s_2) == Sphere(6)
    assert s_1.volume == 268.08257
    assert s_1.area == 201.06193

def test_sphere_sort():
    s_1 = Sphere(3)
    s_2 = Sphere(4)
    s_3 = Sphere(5)
    spheres = [s_1, s_3, s_2]
    spheres.sort()
    assert spheres == [Sphere(3),Sphere(4),Sphere(5)]






