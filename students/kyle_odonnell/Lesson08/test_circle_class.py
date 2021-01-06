"""
test code for circle_class.py
"""


from circle_class import *
import math


# test radius constructor
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


# test str() method
def test_circle_str():
    c = Circle(4)
    assert str(c) == "Circle with radius: 4.000000"
    d = Circle.from_diameter(5)
    assert str(d) == "Circle with radius: 2.500000"

# test repr() method
def test_circle_repr():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'

# test add protocol
def test_add_protocol():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 + c2).radius == 6
    assert (c2 + c1).radius == 6

# test multiplication protocol
def test_mul_protocal():
    c1 = Circle(5)
    assert (c1 * 3).radius == 15
    assert (3 * c1).radius == 15
    assert c1 * 3 == 3 * c1

# test equals comparison
def test_equal_comp():
    c1 = Circle(6)
    c2 = Circle(8)
    c3 = Circle(6)
    assert c1.radius != c2.radius
    assert c3.radius == c1.radius

# test lest than comparison
def test_lt_comp():
    c1 = Circle(6)
    c2 = Circle(8)
    assert c1.radius < c2.radius
    assert c2.radius > c1.radius

# test division operator
def test_tru_div():
    c1 = Circle(6)
    c2 = Circle(8)
    assert c1.radius / c2.radius == 6 / 8
    assert c2.radius / c1.radius == 8 / 6

# test augmented addition
def test_aug_add():
    c1 = Circle(6)
    c2 = Circle(8)
    c2 += c1
    assert c2.radius == 14


# test augmented multiplication
def test_aug_mul():
    c1 = Circle(6)
    c1 *= 2
    assert c1.radius == 12


# test power of operator
def test_pow():
    c1 = Circle(5)
    assert c1.radius ** 2 == 25


# test sphere str()
def test_sphere_str():
    c = Sphere(4)
    assert str(c) == "Sphere with radius: 4.000000"
    d = Sphere.from_diameter(5)
    assert str(d) == "Sphere with radius: 2.500000"


# test sphere repr()
def test_sphere_repr():
    c = Sphere(4)
    assert repr(c) == 'Sphere(4)'


# test volume property
def test_volume():
    c = Sphere(4)
    assert c.volume == 4 / 3 * math.pi * 4 ** 3
    d = Sphere(8)
    assert d.volume == 4 / 3 * math.pi * 8 ** 3


# test surface area property
def surface_area():
    c = Sphere(4)
    assert c.area == 4 * math.pi * 4 ** 2
