"""
test code for circle.py
"""

import io
import pytest
from circle import *
import math


def test_circle_init():
    """This only tests that it can be initialized with some content."""
    a_circle = Circle(100)
    assert a_circle.radius == 100
    b_circle = Circle(100.01)
    assert b_circle.radius == 100.01
    with pytest.raises(TypeError):
        not_circle = Circle("something")

    with pytest.raises(TypeError):
        not_circle = Circle([1, 2, 3])

    with pytest.raises(TypeError):
        not_circle = Circle((1, 2, 3))


def test_circle_radius():
    """This only tests the radius property."""
    a_circle = Circle(100)
    assert a_circle.radius == 100
    a_circle.radius = 100.01
    assert a_circle.radius == 100.01
    with pytest.raises(TypeError):
        a_circle.radius = '100.01'
    b_circle = Circle(100)
    with pytest.raises(ValueError):
        b_circle.radius = -0.000001


def test_circle_diameter():
    """This only tests the diameter property."""
    a_circle = Circle(100)
    assert a_circle.radius == 100
    a_circle.diameter = 100.01
    assert a_circle.radius == 100.01 / 2
    assert a_circle.diameter == 100.01
    with pytest.raises(TypeError):
        a_circle.diameter = '100.01'
    b_circle = Circle(100)
    with pytest.raises(ValueError):
        b_circle.diameter = -0.000001 * 2


def test_circle_area():
    """This only tests the area property."""
    a_circle = Circle(100)
    assert a_circle.area == 100 ** 2 * math.pi
    a_circle.diameter = 100.01
    a_circle.area == (100.01 / 2) ** 2 * math.pi
    with pytest.raises(AttributeError):
        a_circle.area = '100.01'


def test_circle_perimeter():
    """This only tests the perimeter property."""
    a_circle = Circle(100)
    assert a_circle.perimeter == 100 * 2 * math.pi
    a_circle.diameter = 100.01
    a_circle.perimeter == (100.01 / 2) * 2 * math.pi
    with pytest.raises(AttributeError):
        a_circle.perimeter = '100.01'


def test_circle_from_diameter():
    """This only tests the from diameter constructor."""
    a_circle = Circle.from_diameter(100)
    assert a_circle.radius == 50
    assert a_circle.diameter == 100
    with pytest.raises(ValueError):
        a_circle = Circle.from_diameter(-1.0)
    with pytest.raises(TypeError):
        a_circle = Circle.from_diameter([1.00])


def test_circle_str():
    """This only tests the __str__ magic method."""
    a_circle = Circle(100)
    b_circle = Circle.from_diameter(10.01)
    assert str(a_circle) == "Circle with radius: 100.000000"
    assert str(b_circle) == "Circle with radius: 5.005000"


def test_circle_repr():
    """This only tests the __repr__ magic method."""
    a_circle = Circle(100)
    b_circle = Circle.from_diameter(10.01)
    assert repr(a_circle) == "Circle(100)"
    assert repr(b_circle) == "Circle(5.005)"


def test_circle_numeric_add_and_sub():
    """This only tests the add, sub magic methods."""
    a_circle = Circle(100)
    b_circle = Circle.from_diameter(10.01)

    # add
    assert a_circle + b_circle == b_circle + a_circle
    res_circle = a_circle + b_circle
    assert res_circle.radius == 105.005
    with pytest.raises(TypeError):
        res_circle = a_circle + 100.0
    with pytest.raises(TypeError):
        res_circle = a_circle + [100.0]

    # subtract
    with pytest.raises(ValueError):
        assert a_circle - b_circle != b_circle - a_circle
    res_circle = a_circle - b_circle
    assert res_circle.radius == 94.995
    with pytest.raises(TypeError):
        res_circle = a_circle - 100.0
    with pytest.raises(TypeError):
        res_circle = a_circle - [100.0]
    with pytest.raises(ValueError):
        res_circle = b_circle - a_circle


def test_circle_numeric_mul():
    """This only tests the mul magic methods."""
    a_circle = Circle(100)
    b_circle = Circle.from_diameter(10.01)
    assert a_circle * 3 == 3 * a_circle
    assert (a_circle * 3.11).radius == 311
    assert (3 * b_circle).radius == 15.015
    with pytest.raises(TypeError):
        res_circle = a_circle * '100.1'
    with pytest.raises(TypeError):
        res_circle = '100.1' * a_circle


def test_circle_numeric_truediv_floordiv():
    """This only tests the truediv and floordiv magic methods."""
    a_circle = Circle(100)
    b_circle = Circle.from_diameter(10.01)

    # truediv (/)
    assert pytest.approx((a_circle / 3.11).radius, 0.0001) == 32.1542
    assert pytest.approx((3 / b_circle).diameter, 0.00001) == 1.19880
    with pytest.raises(TypeError):
        res_circle = a_circle / '100.1'
    with pytest.raises(TypeError):
        res_circle = '100.1' / a_circle

    # floordiv (//)
    assert (a_circle // 3.11).radius == 32
    assert (3 // b_circle).diameter == 0
    with pytest.raises(TypeError):
        res_circle = a_circle // '100.1'
    with pytest.raises(TypeError):
        res_circle = '100.1' // a_circle


def test_circle_numeric_comparators_lt_le():
    """This tests the less than and lees than and equal to comparator magic methods."""
    a_circle = Circle(100)
    b_circle = Circle.from_diameter(10.01)

    # less than (<)
    assert b_circle < a_circle
    assert not(a_circle < b_circle)
    with pytest.raises(TypeError):
        res_circle = a_circle < '100.1'
    with pytest.raises(TypeError):
        res_circle = '100.1' < a_circle

    # less than and equal to (<=)
    assert b_circle <= a_circle
    assert not(a_circle <= b_circle)
    b_circle.diameter = a_circle.diameter
    assert a_circle <= b_circle
    with pytest.raises(TypeError):
        res_circle = a_circle <= '100.1'
    with pytest.raises(TypeError):
        res_circle = '100.1' <= a_circle


def test_circle_numeric_comparators_gt_ge():
    """This tests the grater than and grater than and equal to comparator magic methods."""
    a_circle = Circle(100)
    b_circle = Circle.from_diameter(10.01)

    # less than (>)
    assert a_circle > b_circle
    assert not(b_circle > a_circle)
    with pytest.raises(TypeError):
        res_circle = a_circle > '100.1'
    with pytest.raises(TypeError):
        res_circle = '100.1' > a_circle

    # less than and equal to (>=)
    assert a_circle >= b_circle
    assert not(b_circle >= a_circle)
    b_circle.diameter = a_circle.diameter
    assert a_circle >= b_circle
    with pytest.raises(TypeError):
        res_circle = a_circle >= '100.1'
    with pytest.raises(TypeError):
        res_circle = '100.1' >= a_circle


def test_circle_numeric_comparators_eq_ne():
    """This tests the grater than and grater than and equal to comparator magic methods."""
    a_circle = Circle(100)
    b_circle = Circle.from_diameter(10.01)
    c_circle = Circle(100.0)
    # less than (==)
    assert a_circle == c_circle
    assert not(a_circle == b_circle)
    with pytest.raises(TypeError):
        res_circle = a_circle == '100.1'
    with pytest.raises(TypeError):
        res_circle = '100.1' == a_circle

    # less than and equal to (!=)
    assert a_circle != b_circle
    assert not(c_circle != a_circle)
    b_circle.diameter = a_circle.diameter
    assert not(a_circle != b_circle)
    with pytest.raises(TypeError):
        res_circle = a_circle != '100.1'
    with pytest.raises(TypeError):
        res_circle = '100.1' != a_circle


def test_circle_numeric_i_operators():
    """This tests the i operator magic methods."""
    a_circle = Circle(100)
    b_circle = Circle.from_diameter(10.01)
    c_circle = Circle(100.0)

    # +=
    a_circle += c_circle
    assert a_circle.diameter == 400
    with pytest.raises(TypeError):
        a_circle += '100.1'

    # -=
    a_circle -= c_circle
    assert a_circle.diameter == 200
    with pytest.raises(TypeError):
        a_circle -= '100.1'

    # *=
    a_circle *= 2.0
    assert a_circle.diameter == 400
    with pytest.raises(TypeError):
        a_circle *= '100.1'
    with pytest.raises(TypeError):
        a_circle *= b_circle

    # /=
    a_circle /= 2.0
    assert a_circle.diameter == 200
    with pytest.raises(TypeError):
        a_circle /= '100.1'
    with pytest.raises(TypeError):
        a_circle /= b_circle

    # //=
    a_circle //= 2.0
    assert a_circle.diameter == 100
    with pytest.raises(TypeError):
        a_circle //= '100.1'
    with pytest.raises(TypeError):
        a_circle //= b_circle


def test_sphere_init():
    """This only tests that it can be initialized with some content."""
    a_sphere = Sphere(100)
    assert a_sphere.radius == 100
    b_sphere = Sphere(100.01)
    assert b_sphere.radius == 100.01
    with pytest.raises(TypeError):
        not_sphere = Sphere("something")

    with pytest.raises(TypeError):
        not_sphere = Sphere([1, 2, 3])

    with pytest.raises(TypeError):
        not_sphere = Sphere((1, 2, 3))


def test_sphere_radius():
    """This only tests the radius property."""
    a_sphere = Sphere(100)
    assert a_sphere.radius == 100
    a_sphere.radius = 100.01
    assert a_sphere.radius == 100.01
    with pytest.raises(TypeError):
        a_sphere.radius = '100.01'
    b_sphere = Sphere(100)
    with pytest.raises(ValueError):
        b_sphere.radius = -0.000001


def test_sphere_diameter():
    """This only tests the diameter property."""
    a_sphere = Sphere(100)
    assert a_sphere.radius == 100
    a_sphere.diameter = 100.01
    assert a_sphere.radius == 100.01 / 2
    assert a_sphere.diameter == 100.01
    with pytest.raises(TypeError):
        a_sphere.diameter = '100.01'
    b_sphere = Sphere(100)
    with pytest.raises(ValueError):
        b_sphere.diameter = -0.000001 * 2


def test_sphere_area():
    """This only tests the area property."""
    a_sphere = Sphere(100)
    assert a_sphere.area == 100 ** 2 * math.pi * 4
    a_sphere.diameter = 100.01
    assert a_sphere.area == (100.01 / 2) ** 2 * math.pi * 4
    with pytest.raises(AttributeError):
        a_sphere.area = '100.01'


def test_sphere_volume():
    """This only tests the volume property."""
    a_sphere = Sphere(100)
    assert a_sphere.volume == 100 ** 3 * math.pi * 4 / 3
    a_sphere.diameter = 100.01
    assert a_sphere.volume == (100.01 / 2) ** 3 * math.pi * 4 /3
    with pytest.raises(AttributeError):
        a_sphere.volume = '100.01'


def test_sphere_from_diameter():
    """This only tests the from diameter constructor."""
    a_sphere = Sphere.from_diameter(100)
    assert a_sphere.radius == 50
    assert a_sphere.diameter == 100
    with pytest.raises(ValueError):
        a_sphere = Sphere.from_diameter(-1.0)
    with pytest.raises(TypeError):
        a_sphere = Sphere.from_diameter([1.00])


def test_sphere_str():
    """This only tests the __str__ magic method."""
    a_sphere = Sphere(100)
    b_sphere = Sphere.from_diameter(10.01)
    assert str(a_sphere) == "Sphere with radius: 100.000000"
    assert str(b_sphere) == "Sphere with radius: 5.005000"


def test_sphere_repr():
    """This only tests the __repr__ magic method."""
    a_sphere = Sphere(100)
    b_sphere = Sphere.from_diameter(10.01)
    assert repr(a_sphere) == "Sphere(100)"
    assert repr(b_sphere) == "Sphere(5.005)"


def test_sphere_numeric_add_and_sub():
    """This only tests the add, sub magic methods."""
    a_sphere = Sphere(100)
    b_sphere = Sphere.from_diameter(10.01)

    # add
    assert a_sphere + b_sphere == b_sphere + a_sphere
    res_sphere = a_sphere + b_sphere
    assert res_sphere.radius == 105.005
    with pytest.raises(TypeError):
        res_sphere = a_sphere + 100.0
    with pytest.raises(TypeError):
        res_sphere = a_sphere + [100.0]

    # subtract
    with pytest.raises(ValueError):
        assert a_sphere - b_sphere != b_sphere - a_sphere
    res_sphere = a_sphere - b_sphere
    assert res_sphere.radius == 94.995
    with pytest.raises(TypeError):
        res_sphere = a_sphere - 100.0
    with pytest.raises(TypeError):
        res_sphere = a_sphere - [100.0]
    with pytest.raises(ValueError):
        res_sphere = b_sphere - a_sphere


def test_sphere_numeric_mul():
    """This only tests the mul magic methods."""
    a_sphere = Sphere(100)
    b_sphere = Sphere.from_diameter(10.01)
    assert a_sphere * 3 == 3 * a_sphere
    assert (a_sphere * 3.11).radius == 311
    assert (3 * b_sphere).radius == 15.015
    with pytest.raises(TypeError):
        res_sphere = a_sphere * '100.1'
    with pytest.raises(TypeError):
        res_sphere = '100.1' * a_sphere


def test_sphere_numeric_truediv_floordiv():
    """This only tests the truediv and floordiv magic methods."""
    a_sphere = Sphere(100)
    b_sphere = Sphere.from_diameter(10.01)

    # truediv (/)
    assert pytest.approx((a_sphere / 3.11).radius, 0.0001) == 32.1542
    assert pytest.approx((3 / b_sphere).diameter, 0.00001) == 1.19880
    with pytest.raises(TypeError):
        res_sphere = a_sphere / '100.1'
    with pytest.raises(TypeError):
        res_sphere = '100.1' / a_sphere

    # floordiv (//)
    assert (a_sphere // 3.11).radius == 32
    assert (3 // b_sphere).diameter == 0
    with pytest.raises(TypeError):
        res_sphere = a_sphere // '100.1'
    with pytest.raises(TypeError):
        res_sphere = '100.1' // a_sphere


def test_sphere_numeric_comparators_lt_le():
    """This tests the less than and lees than and equal to comparator magic methods."""
    a_sphere = Sphere(100)
    b_sphere = Sphere.from_diameter(10.01)

    # less than (<)
    assert b_sphere < a_sphere
    assert not(a_sphere < b_sphere)
    with pytest.raises(TypeError):
        res_sphere = a_sphere < '100.1'
    with pytest.raises(TypeError):
        res_sphere = '100.1' < a_sphere

    # less than and equal to (<=)
    assert b_sphere <= a_sphere
    assert not(a_sphere <= b_sphere)
    b_sphere.diameter = a_sphere.diameter
    assert a_sphere <= b_sphere
    with pytest.raises(TypeError):
        res_sphere = a_sphere <= '100.1'
    with pytest.raises(TypeError):
        res_sphere = '100.1' <= a_sphere


def test_sphere_numeric_comparators_gt_ge():
    """This tests the grater than and grater than and equal to comparator magic methods."""
    a_sphere = Sphere(100)
    b_sphere = Sphere.from_diameter(10.01)

    # less than (>)
    assert a_sphere > b_sphere
    assert not(b_sphere > a_sphere)
    with pytest.raises(TypeError):
        res_sphere = a_sphere > '100.1'
    with pytest.raises(TypeError):
        res_sphere = '100.1' > a_sphere

    # less than and equal to (>=)
    assert a_sphere >= b_sphere
    assert not(b_sphere >= a_sphere)
    b_sphere.diameter = a_sphere.diameter
    assert a_sphere >= a_sphere
    with pytest.raises(TypeError):
        res_sphere = a_sphere >= '100.1'
    with pytest.raises(TypeError):
        res_sphere = '100.1' >= a_sphere


def test_sphere_numeric_comparators_eq_ne():
    """This tests the grater than and grater than and equal to comparator magic methods."""
    a_sphere = Sphere(100)
    b_sphere = Sphere.from_diameter(10.01)
    c_sphere = Sphere(100.0)
    # less than (==)
    assert a_sphere == c_sphere
    assert not(a_sphere == b_sphere)
    with pytest.raises(TypeError):
        res_sphere = a_sphere == '100.1'
    with pytest.raises(TypeError):
        res_sphere = '100.1' == a_sphere

    # less than and equal to (!=)
    assert a_sphere != b_sphere
    assert not(c_sphere != a_sphere)
    b_sphere.diameter = a_sphere.diameter
    assert not(a_sphere != b_sphere)
    with pytest.raises(TypeError):
        res_sphere = a_sphere != '100.1'
    with pytest.raises(TypeError):
        res_sphere = '100.1' != a_sphere


def test_sphere_numeric_i_operators():
    """This tests the i operator magic methods."""
    a_sphere = Sphere(100)
    b_sphere = Sphere.from_diameter(10.01)
    c_sphere = Sphere(100.0)

    # +=
    a_sphere += c_sphere
    assert a_sphere.diameter == 400
    with pytest.raises(TypeError):
        a_sphere += '100.1'

    # -=
    a_sphere -= c_sphere
    assert a_sphere.diameter == 200
    with pytest.raises(TypeError):
        a_sphere -= '100.1'

    # *=
    a_sphere *= 2.0
    assert a_sphere.diameter == 400
    with pytest.raises(TypeError):
        a_sphere *= '100.1'
    with pytest.raises(TypeError):
        a_sphere *= b_sphere

    # /=
    a_sphere /= 2.0
    assert a_sphere.diameter == 200
    with pytest.raises(TypeError):
        a_sphere /= '100.1'
    with pytest.raises(TypeError):
        a_sphere /= b_sphere

    # //=
    a_sphere //= 2.0
    assert a_sphere.diameter == 100
    with pytest.raises(TypeError):
        a_sphere //= '100.1'
    with pytest.raises(TypeError):
        a_sphere //= b_sphere
