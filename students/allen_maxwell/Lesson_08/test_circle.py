#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 1/3/2020
# test_circle.py

import pytest
from circle import *


def test_init():

    # Test default value
    c = Circle()
    assert c.radius == 0

    # Test Positive value
    c = Circle(10)
    assert c.radius == 10

    # Test float value
    c = Circle(1.5)
    assert c.radius == 1.5

    # Test negative value
    try:
        c = Circle(-10)
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        c = Circle('10')
    except ValueError:
        pass
    else:
        assert False


def test_set_radius():

    c = Circle(5)

    # Test zero value
    c.radius = 0
    assert c.radius == 0

    # Test Positive value
    c.radius = 10
    assert c.radius == 10

    # Test float value
    c.radius = 5.5
    assert c.radius == 5.5

    # Test negative value
    try:
        c.radius = -10
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        c.radius = '10'
    except ValueError:
        pass
    else:
        assert False


def test_get_diameter():

    # Test default value
    c = Circle()
    assert c.diameter == 0

    # Test Positive value
    c = Circle(10)
    assert c.diameter == 20

    # Test float value
    c = Circle(1.75)
    assert c.diameter == 3.5


def test_set_diameter():

    c = Circle()

    # Test zero value
    c.diameter = 0
    assert c.radius == 0
    assert c.diameter == 0

    # Test Positive value
    c.diameter = 10
    assert c.radius == 5
    assert c.diameter == 10

    # Test float value
    c.diameter = 5.5
    assert c.radius == 2.75
    assert c.diameter == 5.5

    # Test negative value
    try:
        c.diameter = -10
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        c.diameter = '10'
    except ValueError:
        pass
    else:
        assert False


def test_area():

    # Test zero value
    c = Circle(0)
    assert c.area == 0

    # Test float value
    c = Circle(5)
    assert c.area == 10 * math.pi

    # Test set radius value
    c.radius = 10
    assert c.area == 20 * math.pi

    # Test diameter value
    c.diameter = 35
    assert c.area == 35 * math.pi


def test_set_area():

    c = Circle(5)

    # Test zero value
    try:
        c.area = 0
    except AttributeError:
        pass
    else:
        assert False

    # Test positive value
    try:
        c.area = 10
    except AttributeError:
        pass
    else:
        assert False

    # Test negative value
    try:
        c.area = -10
    except AttributeError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        c.area = '10'
    except AttributeError:
        pass
    else:
        assert False


def test_from_diameter():

    # initialization test
    c = Circle(5)
    assert c.radius == 5

    # Test zero value
    c = Circle.from_diameter(0)
    assert c.radius == 0

    # assert Circle values can be changed with from_diameter
    c = Circle.from_diameter(8)
    assert c.radius == 4

    # Test negative value
    try:
        c = Circle.from_diameter(-10)
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        c = Circle.from_diameter('10')
    except ValueError:
        pass
    else:
        assert False


def test_str():
    c = Circle(5)
    assert str(c) == 'Circle with radius: 5'


def test_repr():
    c = Circle(10)
    assert repr(c) == 'Circle(10)'


def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(c1 + c2) == 'Circle(6)'

    # Test c2 greater than c1
    try:
        c1 + -3
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        c1 + '10'
    except ValueError:
        pass
    else:
        assert False


def test_iadd():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(8)

    c3 += 2
    assert repr(c3) == 'Circle(10)'
    c2 += 1
    assert repr(c2) == 'Circle(5)'
    c2 += c1
    assert repr(c2) == 'Circle(7)'
    c3 += -1
    assert repr(c3) == 'Circle(9)'

    # Test value is greater than c1
    try:
        c1 += -3
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        c1 += '10'
    except ValueError:
        pass
    else:
        assert False


def test_sub():
    c1 = Circle(2)
    c2 = Circle(4)

    assert repr(c2 - c1) == 'Circle(2)'
    assert repr(c2 - 1) == 'Circle(3)'
    assert repr(c2 - -1) == 'Circle(5)'

    # Test c2 greater than c1
    try:
        repr(c1 - c2)
    except ValueError:
        pass
    else:
        assert False

    # Test value is greater than c1
    try:
        repr(c1 - 3)
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        repr(c1 - '10')
    except ValueError:
        pass
    else:
        assert False


def test_isub():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(8)

    c3 -= 2
    assert repr(c3) == 'Circle(6)'
    c2 -= 1
    assert repr(c2) == 'Circle(3)'
    c2 -= c1
    assert repr(c2) == 'Circle(1)'
    c3 -= -1
    assert repr(c3) == 'Circle(7)'

    # Test c2 greater than c1
    try:
        c2 -= c1
    except ValueError:
        pass
    else:
        assert False

    # Test value is greater than c1
    try:
        c1 -= 3
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        c1 -= '10'
    except ValueError:
        pass
    else:
        assert False


def test_mul():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(c1 * 4) == 'Circle(8)'
    assert repr(3 * c2) == 'Circle(12)'
    assert repr(c2 * c1) == 'Circle(8)'

    # Test value is greater than c1
    try:
        c1 * -3
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        c1 * '10'
    except ValueError:
        pass
    else:
        assert False


def test_rmul():
    c = Circle(2)

    assert repr(4 * c) == 'Circle(8)'

    # Test value is greater than c1
    try:
        -3 * c
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        '10' * c
    except ValueError:
        pass
    else:
        assert False


def test_imul():
    c1 = Circle(2)
    c2 = Circle(4)
    c1 *= 2
    assert repr(c1) == 'Circle(4)'

    # Test value is greater than c1
    try:
        -3 * c2
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        '10' * c2
    except ValueError:
        pass
    else:
        assert False


def test_div():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(5)
    c4 = Circle(6)
    assert repr(c2 / 2) == 'Circle(2.0)'
    assert repr(c3 / 2) == 'Circle(2.5)'
    assert repr(c4 / 1.5) == 'Circle(4.0)'

    # Test zero denominator value
    try:
        repr(c1 / 0)
    except ValueError:
        pass
    else:
        assert False

    # Test negative value
    try:
        repr(c1 / -1)
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        repr(c2 / '10')
    except ValueError:
        pass
    else:
        assert False


def test_idiv():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(5)
    c4 = Circle(6)

    c2 /= 2
    assert repr(c2) == 'Circle(2.0)'
    c3 /= 2
    assert repr(c3) == 'Circle(2.5)'
    c4 /= 1.5
    assert repr(c4) == 'Circle(4.0)'

    # Test zero denominator value
    try:
        c1 /= 0
    except ValueError:
        pass
    else:
        assert False

    # Test negative value
    try:
        c1 /= -1
    except ValueError:
        pass
    else:
        assert False

    # Test non-numeric value
    try:
        c2 /= '10'
    except ValueError:
        pass
    else:
        assert False


def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 > c2) == False
    assert (c2 > c1) == True
    assert (c1 < c2) == True
    assert (c2 < c1) == False
    assert (c1 == c2) == False
    c3 = Circle(4)
    assert (c2 == c3) == True


def test_sorted_list():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]


def test_reflected():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + 1 == 1 + c1
    assert c2 * 3 == 3 * c2


def test_sphere_str():
    s = Sphere(5)
    assert str(s) == 'Sphere with radius: 5'


def test_sphere_repr():
    s = Sphere(10)
    assert repr(s) == 'Sphere(10)'


def test_sphere_area():
    s = Sphere(10)
    assert s.area == 4 * math.pi * 10 ** 2


def test_sphere_volume():
    s = Sphere(10)
    assert s.volume == (4/3) * math.pi * 10 ** 3


def test_sphere_add():
    s1 = Sphere(2)
    s2 = Sphere(4)
    assert repr(s1 + s2) == 'Sphere(6)'
    assert repr(s2 + 3) == 'Sphere(7)'
    assert repr(5 + s2) == 'Sphere(9)'
    s2 += s1
    assert repr(s2) == 'Sphere(6)'
    s1 += 3
    assert repr(s1) == 'Sphere(5)'


def test_sphere_sub():
    s1 = Sphere(2)
    s2 = Sphere(4)
    assert repr(s2 - s1) == 'Sphere(2)'
    assert repr(s2 - 3) == 'Sphere(1)'
    s2 -= s1
    assert repr(s2) == 'Sphere(2)'
    s2 -= 1
    assert repr(s2) == 'Sphere(1)'


def test_sphere_mul():
    s1 = Sphere(2)
    s2 = Sphere(4)
    assert repr(s1 * 4) == 'Sphere(8)'
    assert repr(3 * s2) == 'Sphere(12)'
    assert repr(s2 * s1) == 'Sphere(8)'
    s2 *= s1
    assert repr(s2) == 'Sphere(8)'
    s1 *= 3
    assert repr(s1) == 'Sphere(6)'


def test_sphere_div():
    s1 = Sphere(2)
    s2 = Sphere(4)
    assert repr(s2 / 2) == 'Sphere(2.0)'
    assert repr(s2 / s1) == 'Sphere(2.0)'
    s2 /= s1
    assert repr(s2) == 'Sphere(2.0)'
    s2 /= 0.5
    assert repr(s2) == 'Sphere(4.0)'


def test_sphere_compare():
    s1 = Sphere(2)
    s2 = Sphere(4)
    assert (s1 > s2) == False
    assert (s2 > s1) == True
    assert (s1 < s2) == True
    assert (s2 < s1) == False
    assert (s1 == s2) == False
    s3 = Sphere(4)
    assert (s2 == s3) == True


def test_sphere_sorted_list():
    spheres = [Sphere(6), Sphere(7), Sphere(8), Sphere(4), Sphere(0), Sphere(2), Sphere(3), Sphere(5), Sphere(9), Sphere(1)]
    spheres.sort()
    assert spheres == [Sphere(0), Sphere(1), Sphere(2), Sphere(3), Sphere(4), Sphere(5), Sphere(6), Sphere(7), Sphere(8), Sphere(9)]


def test_sphere_from_diameter():
    s = Sphere(5)

    # Test zero value
    s = Sphere.from_diameter(0)
    assert s.radius == 0
    assert s.volume == 0
    assert s.area == 0

    # assert Circle values can be changed with from_diameter
    s = Sphere.from_diameter(8)
    assert s.radius == 4
    assert s.volume == (4/3) * math.pi * 4 ** 3
    assert s.area == 4 * math.pi * 4 ** 2


def test_Sphere_set_area():
    s = Sphere(5)

    # Test zero value
    try:
        s.area = 100
    except AttributeError:
        pass
    else:
        assert False
