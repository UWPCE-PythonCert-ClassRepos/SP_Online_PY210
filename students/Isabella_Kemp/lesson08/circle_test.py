from circle import *


def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_circle_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_setter_diameter():
    c = Circle(8)
    c.diameter = 4
    assert c.diameter == 4
    assert c.radius == 2

def test_circle_area():
    c = Circle(2)
    assert round(c.area, 5) == 12.566370

def test_class_method():
    c = Circle.from_diameter(8)
    assert c.radius == 4
    assert c.diameter == 8

def test_str():
    c = Circle(4)
    assert str(Circle(4)) == "Circle with radius of 4"

def test__repr():
    c = Circle(4)
    d = eval(repr(c))
    assert repr(c) == "Circle(4)"
    assert d == Circle(4)

#Here we test the basic adding and multiplication of the circles
def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c = c1 + c2
    assert c == Circle(6)

def test_multiplication():
    c1 = Circle(2)
    c2 = Circle(4)
    c = c2 * c1
    assert c == Circle(8)

#comparing and sorting circles
def test_comparing(): 
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    c4 = Circle(5)
    assert (c1 < c2) is True
    assert (c2 != c4) is True
    assert (c4 > c1) is True

    circles = [c4, c2, c1]
    circles.sort()
    assert circles == [Circle(2), Circle(4), Circle(5)]

# Testing sphere class

def test_sphere_radius():
    s1 = Sphere(2)
    s2 = Sphere(4)
    assert s1.radius == 2
    assert s2.radius == 4

def test_sphere_diameter():
    s1 = Sphere(2)
    s2 = Sphere(4)
    assert s1.diameter == 4
    assert s2.diameter == 8

def test_sphere_repr():
    c = Sphere(4)
    d = eval(repr(c))
    assert repr(c) == 'Sphere(4)'
    assert d == Sphere(4)

def test_sphere_str():
    c = Sphere(4)
    assert str(Sphere(4)) == "Sphere with radius of 4"

def test_sphere_volume():
    c = Sphere(4)
    assert round(c.volume, 5) == 268.08257

def test_area():
    c = Sphere(4)
    assert round(c.area, 5) == 201.06193

def test_area_setter():
    c = Sphere(2)
    try:
        c.area = 42
    except AttributeError:
        assert True    