"""
Christine Kim
Lesson 8
Assignment Spheres
"""
from sphere import Sphere

#test sphere
def test_sphere():
    s = Sphere(4)
    assert s.radius == 4
    assert s.diameter == 8

#test print sphere
def test_str():
    s = Sphere(5)
    assert str(s) == "Sphere with radius: 5"

def test_repr():
    s = Sphere(6)
    assert repr(s) == "Sphere(6)"

def test_volume():
    s = Sphere(10)
    assert s.volume() == 4188.790204786391


def test_area():
    s = Sphere(10)
    assert s.area() == 1256.6370614359173

def test_sphere_from_di():
    s = Sphere.from_diameter(8)
    assert s.diameter == 4
    assert s.diameter == 2