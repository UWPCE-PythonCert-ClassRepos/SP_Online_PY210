from circle import *

# Tests for Circle class #
#############################

def test_circle_attr():
    c1 = Circle(2)
    c2 = Circle(8)
    assert c1.radius == 2
    assert c2.radius == 8
    assert c1.diameter == 4
    assert c2.diameter == 16

def test_area():
    c1 = Circle(2)
    c2 = Circle(8)
    assert c1.area == 12.5664
    assert c2.area == 201.0619

def test_from_diameter():
    c1 = Circle.from_diameter(2)
    c2 = Circle.from_diameter(8)
    assert c1.radius == 1
    assert c2.radius == 4
    assert c1.diameter == 2
    assert c2.diameter == 8

def test_magic_methods():
    c1 = Circle(2)
    c2 = Circle(8)
    assert c1 + c2 == "Circle(10)"
    assert c1 * 2 == "Circle(4)"
    assert 2 * c2 == "Circle(16)"
    assert (c1 < c2) is True
    assert (c1 > c2) is False
    assert (c1 == c2) is False
    assert c2 / 2 == "Circle(4.0)"
    assert 2 / c2 == "You cannot divide an integer by a Circle."

# Tests for Sphere subclass #
#############################

def test_sphere_attr():
    s1 = Sphere(2)
    s2 = Sphere(8)
    assert s1.radius == 2
    assert s2.radius == 8
    assert s1.diameter == 4
    assert s2.diameter == 16

def test_sphere_area():
    s1 = Sphere(2)
    s2 = Sphere(8)
    assert s1.area == 50.2655
    assert s2.area == 804.2477

def test_sphere_volume():
    s1 = Sphere(2)
    s2 = Sphere(8)
    assert s1.volume == 33.5103
    assert s2.volume == 2144.6606

