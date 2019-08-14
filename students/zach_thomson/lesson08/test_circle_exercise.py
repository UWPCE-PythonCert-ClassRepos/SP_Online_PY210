import pytest
from circle_exercise import *

def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_init():
    '''test to make sure class Circle requires radius'''
    with pytest.raises(TypeError):
        c = Circle()

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 2
    assert c.radius == 1

def test_area():
    c = Circle(2)
    assert c.area == 12.566370614359172
    with pytest.raises(AttributeError):
        c.area = 42

def test_circle_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_circle(capsys):
    c = Circle(4)
    print(str(c))
    captured = capsys.readouterr()
    assert captured.out == 'Circle with radius: 4.000000\n'
    assert repr(c) == "Circle(4)"

def test_numerics():
    c1 = Circle(2)
    c2 = Circle(4)
    d = c1 + c2
    e = c2 * 3
    f = 3 * c2
    assert repr(d) == "Circle(6)"
    assert repr(e) == "Circle(12)"
    assert repr(f) == "Circle(12)"
    a_circle = Circle(3)
    assert a_circle * 3 == 3 * a_circle
    assert c2 / 2 == 2
    c3 = Circle(2)
    c3 += 2
    c1 += c1
    assert c3 == Circle(4)
    assert c1 == Circle(4)
    c2 *= 2
    assert c2 == Circle(8)

def test_compare_circles():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 > c2) == False
    assert (c1 < c2) == True
    assert (c1 == c2) == False
    c3 = Circle(4)
    assert c2 == c3

def test_sort():
    circle_list = [Circle(7), Circle(5), Circle(6), Circle(3), Circle(4), Circle(1)]
    circle_list.sort()
    assert circle_list == [Circle(1), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7)]

def test_sphere():
    s = Sphere(2)
    assert s.radius == 2
    assert s.diameter == 4
    assert s.area == 50.26548245743669
    assert s.volume == 33.510321638291124
    s8 = Sphere.from_diameter(8)
    assert s8.diameter == 8
    assert s8.radius == 4
    with pytest.raises(TypeError):
        s2 = Sphere()


def test_sphere_output(capsys):
    s = Sphere(2)
    print(str(s))
    captured = capsys.readouterr()
    assert captured.out == 'Sphere with radius: 2.000000\n'
    assert repr(s) == "Sphere(2)"
