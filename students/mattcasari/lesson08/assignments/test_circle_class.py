from circle_class import *
import pytest
import random

########
# Step 1
########
def test_create_circle_with_radius():
    radius = 4
    circle = Circle(radius)

    assert radius == circle.radius

########
# Step 2 & 3
########
def test_create_circle_with_diameter():
    diameter = 2
    circle = Circle()
    circle.diameter = diameter

    assert diameter == circle.diameter
    assert diameter/2 == circle.radius

########
# Step 4
########
def test_circle_area():
    radius = 2
    c = Circle(2)

    assert 2*math.pi*radius == c.area

def test_circle_area_cannot_be_set():
    radius = 2
    c = Circle(radius)

    with pytest.raises(AttributeError):
        c.area = 42 

########
# Step 5
########
def test_alternate_constructor_from_diameter():
    diameter = 8
    c = Circle.from_diameter(diameter)

    assert diameter == c.diameter
    assert diameter/2 == c.radius

########
# Step 6
########
def test_updated_str_method():
    c = Circle(4)
    assert "Circle with radius: 4.000" in str(c)

def test_updated_repr_method():
    c = Circle(4)
    assert "Circle(4)" == repr(c)


########
# Step 7
########
def test_add_circles():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert 6 == c3.radius
    assert 12 == c3.diameter
    assert "Circle(6)" == repr(c3)
    assert "Circle with radius: 6" in str(c3)

def test_multiply_circles():
    c1 = Circle(2)
    c2 = c1 * 5
    assert 10 == c2.radius
    assert 20 == c2.diameter

def test_multiply_two_circles():
    c1 = Circle(4)
    c2 = Circle(6)
    c3 = c1 * c2
    assert 24 == c3.radius

def test_multiply_backwards():
    c1 = Circle(3)
    c2 = 3 * c1

    assert 9 == c2.radius
    assert 18 == c2.diameter

def test_greater_than():
    c1 = Circle(15)
    c2 = Circle(20)

    assert (c1 > c2) == False
    assert (c2 > c1) == True

def test_less_than():
    c1 = Circle(15)
    c2 = Circle(20)
    
    assert (c1 < c2) == True
    assert (c2 < c1) == False

def test_equal_to():
    c1 = Circle(250)
    c2 = Circle(250)

    assert c1 == c2

def test_sort_circles():
    circles = [Circle(7), Circle(5), Circle(8),
                Circle(9), Circle(6), Circle(2),
                Circle(4), Circle(0), Circle(3),
                Circle(1)]

    sorted_circles = [Circle(0), Circle(1), Circle(2),
                Circle(3), Circle(4), Circle(5),
                Circle(6), Circle(7), Circle(8),
                Circle(9)]

    circles.sort()
    assert sorted_circles == circles


########
# Step 8
########
def test_reflected():
    c = Circle(10)

    assert c * 3 == 3 * c

def test_augmented_assignment_add():
    c1 = Circle(10)
    c2 = Circle(13)
    c1 += c2
    assert 23 == c1

def test_augmented_assignment_add_int():
    c1 = Circle(33)
    c1 += 2

    assert 35 == c1

def test_augmented_assignment_multiply():
    c1 = Circle(10)
    c1 *= 3

    assert 30 == c1

########
# Step 9
########
def test_sphere_str_method():
    c1 = Sphere(5)

    assert "Sphere with radius: 5" == str(c1)

def test_sphere_repr_method():
    c1 = Sphere(4)
    
    assert "Sphere(4)" == repr(c1)

def test_sphere_volume():
    s1 = Sphere(3)
    volume = 4/3 * math.pi * (3**3)

    assert volume == s1.volume

def test_area_of_sphere_not_implemented():
    s1 = Sphere(22)

    with pytest.raises(NotImplementedError):
        s1.area