from circle_class import *
import math


# test radius
def test_radius():
    c = Circle(4)
    assert c.radius == 4
    d = Circle(8)
    assert d.radius == 8


# test diameter property
def test_diameter():
    c = Circle(4)
    assert c.diameter == 8
    d = Circle(8)
    assert d.diameter == 16


# test diameter setter
def test_diameter_setter():
    c = Circle(4)
    c.diameter = 5
    assert c.diameter == 5


# test area property
def test_area_property():
    c = Circle(5)
    assert c.area == round(math.pi * 5 ** 2, 6)


# test alternate constructor
def test_diameter_constructor():
    c = Circle.from_diameter(8)
    assert c.radius == 4


# test string method
def test_circle_str():
    c = Circle(4)
    assert str(c) == "Circle with radius: 4.000000"
    d = Circle.from_diameter(5)
    assert str(d) == "Circle with radius: 2.500000"


def test_circle_repr():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'


def test_add_protocol():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 + c2).radius == 6
    assert (c2 + c1).radius == 6


def test_mul_protocal():
    c1 = Circle(5)
    assert (c1 * 3).radius == 15
    assert (3 * c1).radius == 15
    assert c1 * 3 == 3 * c1


def test_equal_comp():
    c1 = Circle(6)
    c2 = Circle(8)
    c3 = Circle(6)
    assert c1.radius != c2.radius
    assert c3.radius == c1.radius


def test_lt_comp():
    c1 = Circle(6)
    c2 = Circle(8)
    assert c1.radius < c2.radius
    assert c2.radius > c1.radius


def test_tru_div():
    c1 = Circle(6)
    c2 = Circle(8)
    assert c1.radius / c2.radius == 6 / 8
    assert c2.radius / c1.radius == 8 / 6


def test_aug_add():
    c1 = Circle(6)
    c2 = Circle(8)
    c2 += c1
    assert c2.radius == 14


def test_aug_mul():
    c1 = Circle(6)
    c1 *= 2
    assert c1.radius == 12


def test_pow():
    c1 = Circle(5)
    assert c1.radius ** 2 == 25


def test_sphere_str():
    c = Sphere(4)
    assert str(c) == "Sphere with radius: 4.000000"
    d = Sphere.from_diameter(5)
    assert str(d) == "Sphere with radius: 2.500000"


def test_sphere_repr():
    c = Sphere(4)
    assert repr(c) == 'Sphere(4)'

def test_volume():
    c = Sphere(4)
    assert c.diameter == 4 / 3 * pi * 4 ** 3
    d = Circle(8)
    assert d.diameter == 4 / 3 * pi * 8 ** 3