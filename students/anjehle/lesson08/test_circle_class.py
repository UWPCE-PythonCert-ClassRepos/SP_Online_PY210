from circle_class import *
from math import pi


def test_circle_radius():
    c = Circle(2)
    print(c.radius)
    assert c.radius == 2


def test_circle_diameter():
    c = Circle(2)
    print(c.dia)
    assert c.dia == 4


def test_circle_diameter_set():
    c = Circle(4)
    print(c.dia)
    assert c.dia == 8
    c.dia = 10
    print(c.dia)
    assert c.dia == 10
    assert c.radius == 5


def test_area():
    c = Circle(2)
    print(c.area)
    assert c.area == 12.566370614359172


def test_circle_from_dia():
    c = Circle.from_dia(8)
    print(f"Diameter:  + {c.dia}")
    print(f"Radius:  + {c.radius}")
    assert c.dia == 8
    assert c.radius == 4


def test_str_method():
    c = Circle(3)
    s = Sphere(3)
    print(str(c))
    print(str(s))
    assert str(c) == 'Circle with radius: 3.00'
    assert str(s) == 'Sphere with radius: 3.00'


def test_repr_method():
    c = Circle(5)
    s = Sphere(5)
    print(repr(c))
    print(repr(s))
    assert repr(c) == 'Circle(5)'
    assert repr(s) == 'Sphere(5)'


def test_add_circle():
    c1 = Circle(2)
    c2 = Circle(4)
    print(c1 + c2)
    assert c1 + c2 == Circle(6)


def test_mult_circle():
    c1 = Circle(5)
    print(c1 * 3)
    assert c1 * 3 == Circle(15)


def test_mult_circle_reverse():
    c1 = Circle(5)
    print(3 * c1)
    assert 3 * c1 == Circle(15)


def test_equal():
    c1 = Circle(2)
    c2 = Circle(2)
    assert c1 == c2


def test_not_equal():
    c1 = Circle(2)
    c2 = Circle(3)
    assert not c1 == c2


def test_lt_gt():
    c1 = Circle(2)
    c2 = Circle(3)
    assert c1 < c2
    assert not c2 < c1
    assert c2 > c1
    assert not c1 > c2


def test_circles_sort():
    circles = [Circle(1), Circle(3), Circle(2), Circle(2.5), Circle(4)]
    circles.sort()
    print(circles)
    assert circles == [Circle(1), Circle(2), Circle(2.5), Circle(3), Circle(4)]


def test_volume():
    s = Sphere(2)
    print(s.volume)
    print(32/3*pi)
    assert s.volume == 32/3*pi


def test_surface_area():
    s = Sphere(2)
    print(s.area)
    print(16*pi)
    assert s.area == 16*pi


def test_sphere_from_dia():
    s = Sphere.from_dia(8)
    print(f"Diameter:  + {s.dia}")
    print(f"Radius:  + {s.radius}")
    assert s.dia == 8
    assert s.radius == 4
