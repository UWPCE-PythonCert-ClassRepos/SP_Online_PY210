#!/usr/bin/env python3
# ---------------------------------------------------------------------------- #
# Title: test circle class
# Description: This is test code for circle_class.py
#
# <07/25/2020>, Created Script
#
# ---------------------------------------------------------------------------- #

import io
import pytest
from circle_class import Circle as Cir, Sphere


def test_circle_init():
    """This will test the circles radius and diameter(x2) on __init__ create"""
    circle = Cir(12)
    assert circle.rad == 12
    assert circle.dia == 24


def test_diameter_update():
    """This will test after the circles radius has been initial created to see if modifying the diameter
     will then update the radius correctly"""
    circle = Cir(12)
    circle.dia = 20
    assert circle.rad == 10
    assert circle.dia == 20


def test_circle_area():
    """This will test the area of a circle (pi x r2) and
    tests to make sure the user can't create circle directly with area"""
    circle = Cir(12)
    assert circle.area == 452.3893421169302
    try:
        circle.area = 12  # property area can't be set first
    except AttributeError:
        pass
    else:
        assert False


def test_from_diameter():  # @classmethod
    """This will test that a circle can be created directly from diameter using a constructor"""
    circle = Cir.from_diameter(24)
    assert circle.dia == 24
    assert circle.rad == 12
    assert circle.area == 452.3893421169302


def test_str():
    """This will test that the string will print correctly"""
    circle = Cir(12)
    assert str(circle) == "Circle with the radius: 12 and area: 452.3893421169302."


def test_repr():
    """This will test that the representation of this object will print correctly"""
    circle = Cir(12)
    assert repr(circle) == "Circle(12)"


def test_add():
    """This will test that two circles radii will add together"""
    circle1 = Cir(12)
    circle2 = Cir(12)
    assert circle1 + circle2, Cir(24)


# def test_multiply_Cir(): *Not used I initially read the instructions wrong*
#     """This will test that two circles radii will multiplied together"""
#     circle3 = Cir(12)
#     circle4 = Cir(12)
#     assert circle3 * circle4, Cir(144)

def test_multiply():
    """This will test that a circle can be multiplied"""
    circle2 = Cir(12)
    assert circle2 * 3, Cir(36)  # left operand "__mul__"
    assert 3 * circle2, Cir(36)  # right operand "__rmul__"


def test_compare():
    """This will test comparision of circles"""
    circle1 = Cir(12)
    circle2 = Cir(20)
    circle3 = Cir(20)
    assert circle1 > circle2
    assert circle1 < circle2
    assert circle1 != circle2
    assert circle3 == circle2
    # extra
    assert circle1 <= circle2
    assert circle2 >= circle3
    assert circle2 <= circle3


def test_sort():
    """This will test the sorting of circles"""
    all_circles = [Cir(6), Cir(7), Cir(8), Cir(4), Cir(0), Cir(2), Cir(3), Cir(5), Cir(9), Cir(1)]
    all_circles.sort()
    assert all_circles == [Cir(0), Cir(1), Cir(2), Cir(3), Cir(4), Cir(5), Cir(6), Cir(7), Cir(8), Cir(9)]


########################
# testing for sphere
########################

def test_sphere_init():
    """This will test the create of sphere including radius, area, and volume"""
    sphere = Sphere(12)
    assert sphere.rad == 12
    assert sphere.volume == 7238.229473870882
    assert sphere.area == 1809.5573684677208


def test_sphere_str():
    """This will test that the string will print correctly"""
    sphere = Sphere(12)
    assert str(sphere) == "Sphere with the radius 12, volume 7238.229473870882, and surface area 1809.5573684677208."


def test_sphere_repr():
    """This will test that the representation of this object will print correctly"""
    sphere = Sphere(12)
    assert repr(sphere) == "Sphere(12)"


def test_add_sphere():
    """This will test that two spheres radii will add together"""
    sphere1 = Sphere(12)
    sphere2 = Sphere(12)
    assert sphere1 + sphere2, Sphere(24)


def test_multiply_sphere():
    """This will test that a sphere can be multiplied"""
    sphere2 = Sphere(12)
    assert sphere2 * 3, Sphere(36)  # left operand "__mul__"
    assert 3 * sphere2, Sphere(36)  # right operand "__rmul__"


def test_compare_sphere():
    """This will test comparision of spheres"""
    sphere1 = Sphere(12)
    sphere2 = Sphere(20)
    sphere3 = Sphere(20)
    assert sphere1 > sphere2
    assert sphere1 < sphere2
    assert sphere1 != sphere2
    assert sphere3 == sphere2
    # extra
    assert sphere1 <= sphere2
    assert sphere2 >= sphere3
    assert sphere2 <= sphere3


def test_sort_sphere():
    """This will test the sorting of spheres"""
    all_sphere = [Sphere(6), Sphere(7), Sphere(8), Sphere(4), Sphere(0), Sphere(2), Sphere(3), Sphere(5), Sphere(9), Sphere(1)]
    all_sphere.sort()
    assert all_sphere == [Sphere(0), Sphere(1), Sphere(2), Sphere(3), Sphere(4), Sphere(5), Sphere(6), Sphere(7), Sphere(8), Sphere(9)]