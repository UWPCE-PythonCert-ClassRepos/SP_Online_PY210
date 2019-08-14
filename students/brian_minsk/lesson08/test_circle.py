# Author: Brian Minsk

from circle import Circle, Sphere
from math import pi

def test_create_circle():
    """ Test basic circle initiation.
    """
    my_circle = Circle(5)

    assert my_circle.radius == 5
    assert my_circle.diameter == 10

    try:
        your_circle = Circle(-0.5)
    except ValueError:
        pass
    else:
        assert False
        
    try:
        another_circle = Circle("5")
    except ValueError:
        pass
    else:
        assert False

def test_diameter_setter():
    """ Test setting the diameter property. Radius will also get set to half
    the radius value.
    """
    my_circle = Circle(5)

    my_circle.diameter = 8

    assert my_circle.radius == 4
    assert my_circle.diameter == 8

    try:
        my_circle.diameter = -8
    except ValueError:
        pass
    else:
        assert False
        
    try:
        my_circle.diameter = "8"
    except ValueError:
        pass
    else:
        assert False

def test_area():
    my_circle = Circle(5)

    assert my_circle.area == (pi * 5 ** 2)

    # Area should not be able to be set
    try:
        my_circle.area = 10
    except AttributeError:
        pass
    else:
        assert False

def test_constructor_from_diameter():
    my_circle = Circle.from_diameter(10)

    assert my_circle.diameter == 10
    assert my_circle.radius == 5
    assert my_circle.area == (pi * 5 ** 2)

    try:
        your_circle = Circle.from_diameter(-0.5)
    except ValueError:
        pass
    else:
        assert False
        
    try:
        another_circle = Circle.from_diameter("5")
    except ValueError:
        pass
    else:
        assert False

def test_str():
    c = Circle(4)

    assert str(c) == "Circle with radius: 4.000000"

def test_repr():
    c = Circle(4)

    repr_c = repr(c)

    assert repr_c == "Circle(4)"

    d = eval(repr_c)

    assert isinstance(d, Circle)
    assert d.radius == 4

def test_add():
    c = Circle(4) + Circle(2)
    assert c.radius == 6

    c1 = Circle(1) + Circle(2) + Circle(5)
    assert c1.radius == 8

    # test that the 2nd argument must be a Circle (or subclass)
    try:
        c2 = Circle(4) + 2
    except TypeError:
        pass
    else:
        assert False

def test_multiply():
    c = Circle(2) * 3
    assert c.radius == 6

    # reverse order test
    c1 = 5 * Circle(3)
    assert c1.radius == 15

    # test that the 2nd argument must be a number
    try:
        c2 = Circle(2) * Circle(3)
    except TypeError:
        pass
    else:
        assert False

    c3 = 3 * Circle(2) * 4
    assert c3.radius == 24

def test_comparison():
    c1 = Circle(1)
    c2 = Circle(2)
    c1a = Circle(1)

    assert c1 < c2
    assert c1 <= c2
    assert c1 <= c1a
    assert c1 == c1a
    assert c1 >= c1a
    assert c2 >= c1
    assert c2 > c1
    assert c2 != c1

def test_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
               Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),
                       Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

def test_iadd():
    c1 = Circle(1)
    c2 = Circle(2)

    c1 += Circle(2)

    assert c1 == Circle(3)

    # test that the 2nd argument must be a Circle (or subclass)
    try:
        c1 += 2
    except TypeError:
        pass
    else:
        assert False

def test_imul():
    c = Circle(2)
    c *= 3

    assert c == Circle(6)

    # test that the 2nd argument must be a number
    try:
        c2 = Circle(2) * Circle(3)
    except TypeError:
        pass
    else:
        assert False

def test_sphere_str():
    s = Sphere(4)

    assert str(s) == "Sphere with radius: 4.000000"

def test_sphere_repr():
    s = Sphere(4)

    repr_s = repr(s)

    assert repr_s == "Sphere(4)"

    d = eval(repr_d)

    assert isinstance(d, Sphere)
    assert s.radius == 4

def test_sphere_volume():
    s = Sphere(3)

    assert s.volume == 4 / 3 * pi * (3 ** 3)

    # Volume should not be able to be set
    try:
        s.volume = 10
    except AttributeError:
        pass
    else:
        assert False

def test_sphere_area:
    s = Sphere(3)

    assert s.area == 4 * pi * (3 ** 2)

    # Suface area should not be able to be set
    try:
        s.area = 10
    except AttributeError:
        pass
    else:
        assert False
