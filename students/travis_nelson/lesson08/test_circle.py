"""
test code for circle.py

The goal is to create a class that represents a simple circle.

A Circle can be defined by either specifying the radius or the diameter,
and the user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area.
Print the circle and get something nice.
Be able to add two circles together.
Be able to compare two circles to see which is bigger.
Be able to compare to see if they are are equal.
(follows from above) be able to put them in a list and sort them.

"""

import pytest
from random import shuffle
from circle import *


def test_init():
    """
    This tests that a circle can be created
    with proper str and repr methods
    """
    c = Circle(5)
    assert c.__str__().startswith("Circle with radius:")
    assert c.__repr__().startswith("Circle")


def test_radius():
    """
    This tests that an instance of Circle gets created with a radius attribute
    """
    c = Circle(10)
    assert c.radius == 10


def test_diameter():
    """
    This tests a Circle instance diameter property
    """
    c = Circle(10)
    assert c.diameter == 20
    c.diameter = 40
    assert c.diameter == 40
    assert c.radius == 20


def test_area():
    """
    This tests a Circle instance area property
    """
    c = Circle(2)
    assert str(c.area).startswith("12.566")
    with pytest.raises(AttributeError):
        c.area = 45


def test_alernate_constructor():
    """
    This tests that a Circle instance can be created
    from a class method
    """
    c = Circle.from_diameter(8)
    print(c)
    assert c.diameter == 8
    assert c.radius == 4


def test_addition():
    """
    This tests that Circle instances
    can be added
    """
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = c1 + c2
    assert c3.diameter == 6
    c4 = Circle.from_diameter(10)
    c5 = c4 + c1
    assert c5.diameter == 12


def test_subtraction():
    """
    This tests that Circle instances
    can be subtracted
    """
    c1 = Circle(2)
    c2 = Circle(5)
    c3 = c2 - c1
    assert c3.diameter == 6
    c4 = Circle.from_diameter(10)
    c5 = c4 - c1
    assert c5.radius == 3


def test_multiplication():
    """
    This tests that Circle instances
    can be multiplied
    """
    c1 = Circle(5)
    c2 = c1 * 5
    assert c2.radius == 25
    c3 = 6 * c1
    assert c3.radius == 30


def test_comparisons():
    """
    This tests that circles
    can be compared
    """
    c1 = Circle(2)
    c2 = Circle(2)
    assert c2 == c1
    c3 = Circle(3)
    assert c3 > c2
    assert c3 != c2


def test_sort():
    """
    This tests to ensure that everything has been
    implemented correctly so far and we can sort
    a list of circles
    """
    circles = [Circle(i) for i in range(1, 10)]
    shuffle(circles)
    circles.sort()
    assert circles[1] < circles[2]
    assert circles[0].diameter == 2


def test_reflected():
    """
    This tests to ensure that 'reflected'
    numbers do the 'right thing'
    """
    c1 = Circle(5)
    assert c1 * 3 == 3 * c1


def test_valid_operand():
    """
    This tests to ensure that none-valid operands
    are being appropriately caught and flagged
    """
    c1 = Circle(2)
    assert c1.__add__(3) == NotImplemented


def test_augmented_assignments():
    """
    Tests that augmented assignments have
    been properly implemented
    """
    c1 = Circle(2)
    c2 = Circle(3)
    assert c1.radius == 2
    c1 += c2
    assert c1.radius == 5
    assert c2.radius == 3
    c2 *= 5
    assert c2.radius == 15


def test_sphere():
    """
    Additional tests for new subclassed sphere
    properties
    """
    s1 = Sphere(4)
    assert s1.__str__().startswith("Sphere with radius:")
    assert s1.__repr__().startswith("Sphere")
    s2 = Sphere.from_diameter(13)
    assert s2.radius == 6.5
    assert str(s1.volume).startswith("268")
    assert str(s2.volume).startswith("1150")
    assert str(s1.area).startswith("201")
    assert str(s2.area).startswith("530")
    spheres = [Sphere(i) for i in range(1, 10)]
    shuffle(spheres)
    spheres.sort()
    assert spheres[3] < spheres[4]
    assert spheres[1].diameter == 4
