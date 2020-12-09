import pytest
from circle import *


# STEP 1 #
def test_init():
    c = Circle(5)
    assert c.radius == 5
    assert c.diameter == 10


def test_setdiameter():
    c = Circle(5)
    c.diameter = 50
    print(c.diameter)
    print(c.radius)
    assert c.radius == 25


def test_area():
    c = Circle(4)
    assert round(c.area, 2) == 50.27


def test_setarea():
    c = Circle(4)
    with pytest.raises(AttributeError):
        c.area = 80


def test_alternate_constructor():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


def test_str():
    c = Circle(5)
    string = str(c)
    assert string == 'Circle with radius: 5'
    string2 = repr(c)
    assert string2 == "Circle(5)"


def test_add():
    c = Circle(4)
    b = Circle(5)
    z = c + b
    assert str(z) == "Circle with radius: 9"


def test_mult():
    c = Circle(4)
    z = 3 * c
    assert str(z) == "Circle with radius: 12"


def test_lt():
    c = Circle(4)
    b = Circle(5)
    assert c < b
    assert not b < c


def test_gt():
    c = Circle(4)
    b = Circle(5)
    assert not c > b
    assert b > c


def test_et():
    c = Circle(4)
    b = Circle(5)
    assert not c == b
    a = Circle(4)
    f = Circle(4)
    assert a == f


def test_sort():
    c = Circle(5)
    b = Circle(4)
    a = Circle(3)
    f = Circle(10)
    circle_list = [a, b, c, f]
    circle_list.sort()
    assert circle_list == [Circle(3), Circle(4), Circle(5), Circle(10)]


def test_reflect():
    a = Circle(3)
    z = a * 3
    y = 3 * a
    assert y == z


def test_imath():
    c = Circle(5)
    a = Circle(3)
    c += a
    assert c.radius == 8


def test_sphere_str():
    c = Sphere(5)
    string = str(c)
    assert string == 'Sphere with radius: 5'
    string2 = repr(c)
    assert string2 == "Sphere(5)"


def test_sphere_volume():
    c = Sphere(4)
    assert round(c.volume, 2) == 268.08


def test_sphere_area():
    c = Sphere(4)
    assert round(c.area, 2) == 201.06


def test_sphere_other():
    c = Sphere(5)
    b = Sphere(20)
    a = Sphere(3)
    f = Sphere(10)
    z = c + b
    assert z.radius == 25
    z = a * 3
    y = 3 * a
    assert y == z
    c += a
    assert c.radius == 8
    sphere_list = [a, b, c, f]
    sphere_list.sort()
    assert sphere_list == [Sphere(3), Sphere(8), Sphere(10), Sphere(20)]


def test_sphere_alternate_constructor():
    c = Sphere.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4