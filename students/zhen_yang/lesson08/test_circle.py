# Test the circle.py


import io
#import circle as cir
from circle import *
from math import pi
from contextlib import redirect_stdout


def test_init():
    # test different initialize parameters
    circle = Circle(3)# radius
    assert circle.radius == 3
    assert circle.diameter == 6

def test_set_diameter():
    circle = Circle()
    circle.diameter = 8 # test the diameter property can be set
    #circle.radius = 3 # test the radius property is read only
    assert circle.diameter == 8
    assert circle.radius == 4

def test_area():
    radius = 5
    circle = Circle(radius)
    assert circle.radius == 5
    assert circle.area == pi * (radius ** 2)
    #circle.area = 5 # test the area property is read only

def test_alternate_constructor():
    circle_1 = Circle(4)# __init__ constructor
    circle_2 = Circle.from_diameter(8) # alternate constructor
    assert circle_1.radius == circle_2.radius
    assert circle_1.diameter == circle_2.diameter
    assert circle_1.area == circle_2.area

def test_nice_print_out():
    circle_1 = Circle(4.0)
    with io.StringIO() as buf, redirect_stdout(buf):
        print(circle_1)
        file_contents = buf.getvalue().strip()
    assert ("Circle with radius: 4.0") in file_contents
    file_contents = repr(circle_1)
    assert ("Circle(4.0)") in file_contents
    circle_2 = eval(repr(circle_1))
    assert circle_1.radius == circle_2.radius

def test_numeric_prptocol():
    circle_1 = Circle(4)
    circle_2 = Circle(5)
    circle_3 = circle_1 + circle_2
    assert circle_3.radius == 9
    circle_4 = circle_3 * 2
    assert circle_4.radius == 18
    circle_5 = circle_1 * circle_2
    assert circle_5.radius == 20

def test_compare_circles():
    circle_1 = Circle(4)
    circle_2 = Circle(5)
    circle_3 = Circle(5.0)
    assert (circle_1 < circle_2) is True
    assert (circle_1 == circle_2) is False
    assert (circle_2 == circle_3) is True

def test_sort_circles():
    list_cirs = [Circle(8), Circle(2), Circle(3), Circle(5), Circle(1)]
    assert list_cirs[0].radius == 8
    assert list_cirs[1].radius == 2
    assert list_cirs[2].radius == 3
    assert list_cirs[3].radius == 5
    assert list_cirs[4].radius == 1
    list_cirs.sort()
    assert list_cirs[0].radius == 1
    assert list_cirs[1].radius == 2
    assert list_cirs[2].radius == 3
    assert list_cirs[3].radius == 5
    assert list_cirs[4].radius == 8

def test_optioal_feature():
    circle_1 = Circle(4)
    circle_2 = Circle(5)
    circle_3 = Circle(8)

    circle_1 += circle_2
    assert circle_1.radius == 9

    circle_3 *= 2
    assert circle_3.radius == 16

    assert circle_1 * 2 == 2 * circle_1

def test_sphere():
    sp_1 = Sphere(2)
    assert sp_1.radius == 2
    assert sp_1.diameter == 4

    area = sp_1.area # 4 pi r**2
    volume = sp_1.volume # 3/4 pi r**3
    assert area == 4 * pi * (sp_1.radius ** 2)
    assert volume == (3 / 4) * pi * (sp_1.radius ** 3)

    with io.StringIO() as buf, redirect_stdout(buf):
        print(sp_1)
        file_contents = buf.getvalue().strip()
    assert ("Sphere with radius: 2") in file_contents
    file_contents = repr(sp_1)
    assert ("Sphere(2)") in file_contents
    sp_2 = eval(repr(sp_1))
    assert sp_1.radius == sp_2.radius
    # test alternate constructor for sphere
    sp_1 = Sphere(4)
    sp_2 = Sphere.from_diameter(8) # alternate constructor
    assert sp_1.radius == sp_2.radius
    assert sp_1.diameter == sp_2.diameter
    assert sp_1.volume == sp_2.volume
    assert sp_1.area == sp_2.area
