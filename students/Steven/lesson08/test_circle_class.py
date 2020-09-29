"""
test code for html_render.py

"""
from circle_class import *
import pytest

# Step 1

def test_init():
    cir = Circle(8)

    # Test Circle class with a given radius
    assert cir.radius == 8


# Step 2

def test_diameter():
    cir = Circle(5)

    # Testing the property of the circle
    assert cir.get_diameter == 10


# Step 3
def test_set_diameter():
    cir = Circle(8)

    # Set the diameter of the Circle and test for both Radius and Diameter
    cir.get_diameter = 3
    assert cir.get_diameter == 3
    assert cir.radius == 1.5


# Step 4
def test_area():
    cir = Circle(6)
    # Calculating the area of a circle with a given radius
    assert cir.get_area == 113.09733552923255
    cir = Circle(7)
    assert round(cir.get_area) == 154

    # Test exception if you try to set the area property to a value
    with pytest.raises(Exception):
        cir.get_area = 42


# Step 5
def test_from_diameter():
    # Creating a Circle with a diameter instead of a radius
    cir = Circle.from_diameter(8)
    assert cir.radius == 4
    assert cir.get_diameter == 8


# Step 6
def test_str():
    cir = Circle(4.25)
    assert str(cir) == "Circle with a radius of: 4.25, Diameter of: 8.5"

def test_repr():
    cir = Circle(2)
    assert repr(cir) == "Circle(2)"


# Step 7
def test_add():
    c1 = Circle(1)
    c2 = Circle(2)
    assert (c1 + c2) == Circle(3)

def test_multiply():
    cir = Circle(4)
    assert cir * 3 == Circle(12)


# Step 8
def test_compare():
    c1 = Circle(8)
    c2 = Circle(6)

    assert (c1 > c2) is True
    assert (c1 >= c2) is True
    assert (c1 < c2) is False
    assert (c1 <= c2) is False
    assert (c1 != c2) is True
    assert (c1 == c2) is False

def test_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4),
               Circle(0), Circle(2), Circle(3), Circle(5),
               Circle(9), Circle(1)]

    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3),
                       Circle(4), Circle(5), Circle(6), Circle(7),
                       Circle(8), Circle(9)]


# Step 9
def test_sphere():
    ball = Sphere(3)
    crate = [Sphere(8), Sphere(3), Sphere(7), Sphere(6)]
    spalding = Sphere(14.5)
    baden = Sphere(14)
    wilson = Sphere.from_diameter(13)

    assert ball.radius == 3
    assert ball.get_diameter == 6
    assert round(ball.volume) == 113
    assert str(ball) == "Sphere with a radius of: 3, Diameter of: 6"
    assert repr(ball) == "Sphere(3)"
    crate.sort()
    assert crate == [Sphere(3), Sphere(6), Sphere(7), Sphere(8)]
    assert (spalding > baden) is True
    assert (spalding != baden) is True
    assert (spalding < baden) is False
    assert (spalding + baden) == Sphere(28.5)
    assert baden * 3 == Sphere(42)
    assert wilson.radius == 6.5
    assert wilson.get_diameter == 13