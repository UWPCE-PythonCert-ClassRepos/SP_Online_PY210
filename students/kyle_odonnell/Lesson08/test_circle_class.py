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


# test area propert
def test_area_property():
    c = Circle(5)
    assert c.area == math.pi * 5 ** 2

# test alternate constructor
def test_diameter_constructor():
    c = Circle.from_diameter(8)
    assert c.radius == 4


def test_docstring():
    c = Circle(4)
    assert print(c) == "Circle with radius: 4.000000"
