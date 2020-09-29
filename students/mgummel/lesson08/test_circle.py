#!/usr/bin/env python3
import pytest

from circle import Circle, Sphere
from math import pi


def test_radius():
    """
    Verifies the radius gets set as expected when 
    initializing a Circle object.
    """
    c = Circle(23)
    d = Circle(3)

    assert c.radius == 23
    assert d.radius == 3

    c.radius = 11

    assert c.radius == 11
    assert d.radius == 3

    d.radius = 50
    assert d.radius == 50


def test_diameter():
    """
    Verifies the diameter gets set as expected when 
    initializing a Circle object.
    """
    c1 = Circle(10)
    c2 = Circle(4)

    assert c1.diameter == 20
    assert c2.diameter == 8

    c2.radius = 12
    c1.radius = 180
    assert c2.diameter == 24
    assert c1.diameter == 360


def test_set_diameter():
    """
    Tests the setter method for the Circle class
    property diameter. 
    """
    d1 = Circle(3)
    d2 = Circle(10)

    d1.diameter = 12
    assert d1.diameter == 12
    assert d1.radius == 6

    d2.diameter = 3
    assert d2.diameter == 3
    assert d2.radius == 1.5


def test_area():
    """
    Verifies the area is equivalent to pi time radius squared
    after initializing a Circle object.
    """
    c1 = Circle(1)
    assert round(c1.area, 5) == 3.14159

    c2 = Circle(7)
    assert round(c2.area, 5) == 153.93804


def test_from_diameter():
    """
    Verifies the radius and diameter gets set as expected when 
    initializing a Circle object using the class method from the
    diameter.
    """
    d1 = Circle.from_diameter(10)
    d2 = Circle.from_diameter(300)

    assert d1.diameter == 10
    assert d1.radius == 5
    assert d2.diameter == 300
    assert d2.radius == 150


def test__str__():
    """
    Verifies the built-in string method and built-in repr method
    gets set as expected when initializing a Circle object.
    """
    c2 = Circle(10)
    assert repr(c2) == "Circle(10)"
    assert c2.__str__() == "Circle with radius: 10.00000"


def test_add():
    """
    Verifies the addition of two Circles will equal the sum 
    of their radiuses.
    """
    c1 = Circle(12)
    c2 = Circle(4)
    c3 = Circle.from_diameter(10)
    c4 = c2 + c1
    c5 = c1 + c2 + c3
    assert repr(c4) == "Circle(16)"
    assert repr(c3 + c2) == "Circle(9)"
    assert repr(c5) == "Circle(21)"

    assert c4.radius == 16
    assert c4.area == pi * 16 ** 2
    assert c4.diameter == 32

    assert c5.radius == 21
    assert c5.area == pi * 21 ** 2
    assert c5.diameter == 42


def test_mul():
    """
    Verifies multiplying a Circle object by a scalar will result in the 
    product of the scalar and the radius.
    """
    c1 = Circle(7)
    d1 = Circle.from_diameter(4)

    assert repr(d1 * 2) == "Circle(4)"
    assert repr(3 * c1) == "Circle(21)"

    # tests rmul
    assert c1 * 3 == 3 * c1
    assert d1 * 4 == 4 * d1


def test_lt():
    """
    Verifies the comparison of two Circles using the less than
    function.
    """
    c1 = Circle(4)
    c2 = Circle(7)
    c3 = Circle(10)
    c4 = Circle(4)

    assert (c2 < c1) == False
    assert (c2 < c3) == True
    assert (c1 > c3) == False
    assert (c1 == c4) == True


def test_sort():
    """
    Tests the builtin sort method for lists will sort all Circle objects
    based on the test ordering in place in the class.
    """
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(
        0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]

    sorted_circles = [Circle(0), Circle(1), Circle(2), Circle(3), Circle(
        4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
    circles.sort()

    assert circles == sorted_circles


def test_iadd():
    """
    Tests the builtin += method syntax works for circles.
    """
    c1 = Circle(14)
    c2 = Circle(3)
    c3 = Circle.from_diameter(20)

    c1 += c2
    c2 += c3
    assert c1.radius == 17
    assert c2.radius == 13
    
    c1 = Circle(14)
    c1 += c3
    assert c1.radius == 24

    c2 += c2
    assert c2.radius == 26

    c4 = Circle(4)
    c2 += c4
    assert c2.radius == 30


def test_imul():
    """
    Tests the builtin *= method syntax works for circles.
    """
    c1 = Circle(5)
    c2 = Circle(8)

    c1 *= 4
    c2 *= 1
    assert c1.radius == 20
    assert c2.radius == 8

    c2 *= 7
    assert c2.radius == 56


def test_sphere():
    """
    Verifies the radius gets set as expected when 
    initializing a Sphere object.
    """
    s1 = Sphere(3)
    s2 = Sphere(4)
    s3 = Sphere.from_diameter(12)

    assert s1.radius == 3
    assert s2.radius == 4
    assert s3.radius == 6


def test_sphere_diameter():
    """
    Verifies the diameter gets set as expected when 
    initializing a Sphere object.
    """
    s1 = Sphere(3)
    s2 = Sphere(4)
    s3 = Sphere.from_diameter(12)

    assert s1.diameter == 6
    assert s2.diameter == 8
    assert s3.diameter == 12


def test_sphere_set_diameter():
    """
    Tests the setter method for the Sphere class
    property diameter. 
    """
    s1 = Sphere(3)
    s2 = Sphere(10)

    s1.diameter = 6
    assert s1.diameter == 6
    assert s1.radius == 3
    assert s2.radius == 10
    assert s2.diameter == 20

    s2.diameter = 3
    assert s2.diameter == 3
    assert s2.radius == 1.5


def test_sphere_area():
    """
    Verifies the surface area is equivalent to 4 times pi times radius squared
    after initializing a Sphere object.
    """
    s1 = Sphere(1)
    assert s1.area == 4 * pi

    s2 = Sphere(7)
    assert s2.area == 49 * 4 * pi


def test_sphere_from_diameter():
    """
    Verifies the radius and diameter gets set as expected when 
    initializing a Sphere object using the class method from the
    diameter.
    """
    s1 = Sphere.from_diameter(100)
    s2 = Sphere.from_diameter(30)

    assert s1.diameter == 100
    assert s1.radius == 50
    assert s2.diameter == 30
    assert s2.radius == 15


def test_sphere__str__():
    """
    Verifies the built-in string method and built-in repr method
    gets set as expected when initializing a Sphere object.
    """
    s2 = Sphere(10)
    assert repr(s2) == "Sphere(10)"
    assert s2.__str__() == "Sphere with radius: 10.00000"


def test_sphere_add():
    """
    Verifies the addition of two Spheres will equal the sum 
    of their radiuses.
    """
    s1 = Sphere(12)
    s2 = Sphere(4)
    s3 = Sphere.from_diameter(10)
    s4 = s2 + s1
    s5 = s1 + s2 + s3
    assert repr(s3 + s2) == "Sphere(9)"
    assert repr(s4) == "Sphere(16)"
    assert repr(s5) == "Sphere(21)"

    assert s4.radius == 16
    assert s4.area == 4 * pi * 16 ** 2
    assert s4.diameter == 32

    assert s5.radius == 21
    assert s5.area == 4 * pi * 21 ** 2
    assert s5.diameter == 42


def test_sphere_mul():
    """
    Verifies multiplying a Sphere object by a scalar will result in the 
    product of the scalar and the radius.
    """
    s1 = Sphere(10)
    s2 = Sphere.from_diameter(8)
    # Verify that the representation of the Sphere objects is equal to 
    # the scalar times the radius
    assert repr(s1 * 2) == "Sphere(20)"
    assert repr(3 * s2) == "Sphere(12)"

    # tests rmul
    assert s1 * 3 == 3 * s1
    assert s2 * 4 == 4 * s2


def test_sphere_lt():
    """
    Verifies the comparison of two Sphere using the less than
    function.
    """
    s1 = Sphere(4)
    s2 = Sphere(7)
    s3 = Sphere(10)
    s4 = Sphere(4)

    assert (s2 < s1) == False
    assert (s2 < s3) == True
    assert (s1 > s3) == False
    assert (s1 == s4) == True


def test_sphere_sort():
    """
    Tests the builtin sort method for lists will sort all Sphere objects
    based on the test ordering in place in the class.
    """
    sphere_list = [Sphere(6), Sphere(7), Sphere(8), Sphere(4), Sphere(
        0), Sphere(2), Sphere(3), Sphere(5), Sphere(9), Sphere(1)]

    sorted_circles = [Sphere(0), Sphere(1), Sphere(2), Sphere(3), Sphere(
        4), Sphere(5), Sphere(6), Sphere(7), Sphere(8), Sphere(9)]
    sphere_list.sort()

    assert sphere_list == sorted_circles


def test_sphere_iadd():
    """
    Tests the builtin += method syntax works for circles.
    """
    s1 = Sphere(2)
    s2 = Sphere(10)
    s3 = Sphere.from_diameter(20)

    s1 += s2
    s2 += s3
    assert s1.radius == 12
    assert s2.radius == 20
    
    s1 = Sphere(14)
    s1 += s3
    assert s1.radius == 24

    s2 += s2
    assert s2.radius == 40

    s4 = Sphere(4)
    s2 += s4
    assert s2.radius == 44


def test_sphere_imul():
    """
    Tests the builtin *= method syntax works for circles.
    """
    s1 = Sphere(3)
    s2 = Sphere(4)

    s1 *= 4
    s2 *= 1
    assert s1.radius == 12
    assert s2.radius == 4

    s2 *= 7
    assert s2.radius == 28