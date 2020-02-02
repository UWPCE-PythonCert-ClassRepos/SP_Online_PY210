from Circle_class_exercise import Circle, Sphere
import random


def test_radius():
    c = Circle(4)
    print(c.radius)
    assert c.radius == 4


def test_diameter():
    c = Circle(4)
    print(c.diameter)
    assert c.diameter == 8


def test_setter_diameter():
    c = Circle(4)
    c.diameter = 2
    print(c.diameter, "and", c.radius)
    assert c.radius == 1


def test_area():
    c = Circle(2)
    assert round(c.area,5) == 12.566370


def test_area_Setter():
    c = Circle(2)
    try:
        c.area = 42
    except AttributeError:
        assert True


def test_from_diameter():
    c = Circle.from_diameter(8)
    print(c.radius)
    assert c.radius == 4
    assert c.diameter == 8


def test_str():
    c = Circle(4)
    assert print(Circle(4)) == "Circle with radius: 4"



def test_repr():
    c = Circle(4)
    d = eval(repr(c))
    assert repr(c) == 'Circle(4)'
    assert d == Circle(4)


def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c = c1 + c2
    assert c == Circle(6)


def test_multiplication():
    c = Circle(1)
    assert 3*c == Circle(3)
    assert c*3 == Circle(3)


def test_inequalities():
    c1=Circle(3)
    c2=Circle(4)
    assert c1 < c2
    assert c2 > c1
    assert c1 <= c2
    assert c2 >= c1
    c3 = Circle(4)
    assert c2 == c3


def test_circle_sorting():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]


def test_sphere_repr():
    c = Sphere(4)
    d = eval(repr(c))
    assert repr(c) == 'Sphere(4)'
    assert d == Sphere(4)


def test_sphere_str():
    c = Sphere(4)
    assert print(Sphere(4)) == "Sphere with radius: 4"


def test_volume():
    c = Sphere(4)
    assert round(c.volume,5) ==268.08257

def test_surface_area():
    c = Sphere(4)
    assert round(c.area,5) == 201.06193

def test_surface_area_Setter():
    c = Sphere(2)
    try:
        c.area = 42
    except AttributeError:
        assert True