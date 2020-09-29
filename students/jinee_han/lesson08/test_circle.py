'''
Test code for the circle and sphere classes
'''

import pytest

from circle import *

######
# Circle Unit Tests
######

def test_circle_radius_constructor():
    '''
    Test the circle class initialize for a given radius
    :return: nothing
    '''

    expected_radius = 2
    c = Circle(expected_radius)
    assert (c.radius == expected_radius)


def test_circle_diameter():
    '''
    Test the diameter property
    :return: nothing
    '''

    expected_radius = 2
    c = Circle(expected_radius)
    assert (c.diameter == expected_radius * 2)


def test_circle_diameter_setter():
    '''
    Test that the diameter setter
    :return:
    '''

    expected_radius_one = 2
    c = Circle(expected_radius_one)
    assert (c.diameter == expected_radius_one * 2)

    expected_radius_two = 5
    c.diameter = expected_radius_two * 2
    assert (c.radius == expected_radius_two)

def test_circle_area():
    '''
    Test the area calculation
    :return: nothing
    '''

    expected_radius = 2
    c = Circle(expected_radius)
    expected_area = round(pi * expected_radius ** 2, 3)
    actual_area = round(c.area, 3)
    assert (actual_area == expected_area)


def test_circle_diameter_constructor():
    '''
    Test the diameter constructor for a given diameter
    :return: nothing
    '''

    expected_diameter = 10
    c = Circle.from_diameter(expected_diameter)
    assert (c.diameter == expected_diameter)
    assert (c.radius == expected_diameter / 2)


def test_circle_string_override():
    '''
    Tests the string override method
    :return: nothing
    '''

    expected_radius = 2
    c = Circle(expected_radius)
    assert (str(c).startswith("Circle with radius:"))


def test_circle_representation_override():
    '''
    Tests the representation override method
    :return: nothing
    '''

    c = Circle(2)
    expected_representation = "Circle(2)"
    assert (expected_representation == repr(c))


def test_circle_addition():
    '''
    Test the addition override method
    :return: nothing
    '''

    c1 = Circle(2)
    c2 = Circle(3)
    expected_circle = Circle(5)
    new_circle = c1 + c2
    assert (new_circle.radius == expected_circle.radius)


def test_circle_multiplication():
    '''
    Test the multiplication override method
    :return: nothing
    '''

    c = Circle(2)
    c_new = c * 3
    expected_circle = Circle(6)
    assert (c_new.radius == expected_circle.radius)


def test_circle_greater_than_method():
    '''
    Tests the greater than override method
    :return:
    '''

    c1 = Circle(2)
    c2 = Circle(3)
    assert (c1 < c2)


def test_circle_greater_than_or_equal_method():
    '''
    Tests the greater than or equal override method
    :return: nothing
    '''
    c1 = Circle(2)
    c2 = Circle(2)
    assert (c1 >= c2)


def test_circle_less_than_or_equal_method():
    '''
    Tests the less than or equal override method
    :return: nothing
    '''

    c1 = Circle(2)
    c2 = Circle(2)
    assert (c1 <= c2)


def test_circle_sorting():
    '''
    Tests sorting various circles
    :return: nothing
    '''

    circle_list = [Circle(6), Circle(3), Circle(2), Circle(8), Circle(1)]
    circle_list.sort()
    expected_circle_list = [Circle(1), Circle(2), Circle(3), Circle(6), Circle(8)]
    assert (circle_list == expected_circle_list)


######
# Sphere Unit Tests
######

def test_sphere_constructor():
    '''
    Tests the sphere constructor
    :return: nothing
    '''

    expected_radius = 2
    s = Sphere(expected_radius)
    assert (s.radius == expected_radius)


def test_sphere_string_override():
    '''
    Tests the string override method
    :return: nothing
    '''

    expected_radius = 2
    s = Sphere(expected_radius)
    assert (str(s).startswith("Sphere with radius:"))


def test_sphere_representation_override():
    '''
    Tests the representation override method
    :return: nothing
    '''

    s = Sphere(2)
    expected_representation = "Sphere(2)"
    assert (expected_representation == repr(s))


def test_sphere_volume_calculation():
    '''
    Tests the sphere volume calculation
    :return: nothing
    '''

    expected_radius = 2
    s = Sphere(expected_radius)
    expected_volume = round(4 / 3 * pi * expected_radius ** 3, 3)
    actual_volume = round(s.volume, 3)
    assert (actual_volume == expected_volume)


def test_sphere_area_calculation():
    '''
    Test the sphere area calculation returns the surface area
    :return: nothing
    '''

    expected_radius = 2
    s = Sphere(expected_radius)
    expected_surface_area = round(4 * pi * expected_radius ** 2, 3)
    actual_surface_area = round(s.area, 3)
    assert (actual_surface_area == expected_surface_area)


def test_sphere_diameter_constructor():
    '''
    Test the sphere diameter constructor for a given diameter
    :return: nothing
    '''

    expected_diameter = 10
    s = Sphere.from_diameter(expected_diameter)
    assert (s.diameter == expected_diameter)
    assert (s.radius == expected_diameter / 2)


def test_sphere_addition():
    '''
    Test the addition override method
    :return: nothing
    '''

    s1 = Sphere(2)
    s2 = Sphere(3)
    expected_sphere = Sphere(5)
    new_sphere = s1 + s2
    assert (new_sphere.radius == expected_sphere.radius)


def test_sphere_multiplication():
    '''
    Test the multiplication override method
    :return: nothing
    '''

    s = Sphere(2)
    s_new = s * 3
    expected_sphere = Sphere(6)
    assert (s_new.radius == expected_sphere.radius)
