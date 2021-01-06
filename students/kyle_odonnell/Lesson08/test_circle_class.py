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
def test_str_method():
    c = Circle(4)
    assert str(c) == "Circle with radius: 4.000000"
    d = Circle.from_diameter(5)
    assert str(d) == "Circle with radius: 2.500000"


def test_repr_method():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'


def test_add_protocol():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 + c2).radius == 6

def test_mul_protocal():
    c1 = Circle(5)
    assert (c1 * 3).radius == 15
    assert (3 * c1).radius == 15


