"""
Programming In Python - Lesson 8 Assignment 1: Spheres
Code Poet: Anthony McKeever
Start Date: 09/06/2019
End Date: 09/06/2019
"""

from sphere import Sphere


def test_sphere_init():
    s = Sphere(2)

    assert s.radius == 2
    assert s.diameter == 4


def test_sphere_diameter_init():
    s = Sphere.from_diameter(6)

    assert s.diameter == 6
    assert s.radius == 3


def test_volume():
    s = Sphere(2)
    assert round(s.volume, 2) == 33.51


def test_area():
    s = Sphere(2)
    assert round(s.area, 3) == 50.265


def test_str():
    s = Sphere(4)
    assert str(s) == "Sphere with radius: 4"

    
def test_repr():
    s = Sphere(4)
    assert repr(s) == "Sphere(4)"
    
    s2 = eval(repr(s))
    assert s2.radius == 4
