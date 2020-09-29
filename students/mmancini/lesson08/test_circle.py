#!/usr/bin/env python3

import math
import pytest
import circle


CONST_TEST_RADIUS = 5
CONST_TEST_DIAMETER = 8

###################################


def test_circle_creation():
    cir = circle.Circle(CONST_TEST_RADIUS)
    assert cir.radius == CONST_TEST_RADIUS
    msg = ""
    msg += f"Circle with radius {cir.radius}"
    print(msg)


def test_circle_property_diameter():
    cir = circle.Circle(CONST_TEST_RADIUS)
    assert cir.diameter == CONST_TEST_RADIUS * 2
    msg = ""
    msg += f"Circle diameter with radius {cir.radius} is {cir.diameter}"
    print(msg)


def test_circle_set_diameter():
    cir = circle.Circle(CONST_TEST_RADIUS)
    cir.diameter = CONST_TEST_DIAMETER
    assert cir.diameter == CONST_TEST_DIAMETER
    assert cir.radius == CONST_TEST_DIAMETER / 2
    msg = ""
    msg += f"Circle with new diameter {cir.diameter} has radius {cir.radius}"
    print(msg)


def test_circle_area():
    cir = circle.Circle(CONST_TEST_RADIUS)
    expected_area = math.pi * (CONST_TEST_RADIUS**2)
    assert cir.area == expected_area
    msg = ""
    msg += f"Circle with radius {cir.radius} has area {cir.area}"
    print(msg)


def test_cls_method():
    cir = circle.Circle.from_diameter(CONST_TEST_DIAMETER)
    assert cir.diameter == CONST_TEST_DIAMETER
    assert cir.radius == CONST_TEST_DIAMETER / 2
    msg = ""
    msg += f"Circle FROM diameter {cir.diameter} has radius {cir.radius}"
    print(msg)


def test_circle_str():
    cir = circle.Circle(CONST_TEST_RADIUS)
    expected_str = f'circle.Circle with radius: {CONST_TEST_RADIUS}'
    assert str(cir) == expected_str
    msg = ""
    msg += f"circle.Circle str is {cir}"
    print(msg)


def test_circle_repr():
    cir_a = circle.Circle(CONST_TEST_RADIUS)
    cir_b = repr(cir_a)
    expected_str = f'circle.Circle({CONST_TEST_RADIUS})'
    assert str(cir_b) == expected_str
    msg = ""
    msg += f"Circle repr is {cir_b}"
    print(msg)


def test_circle_add():
    cir_a = circle.Circle(CONST_TEST_RADIUS)
    cir_b = circle.Circle(CONST_TEST_RADIUS+1)
    cir_c = cir_a + cir_b
    expected_cir = circle.Circle(CONST_TEST_RADIUS + (CONST_TEST_RADIUS+1))
    assert str(cir_c) == str(expected_cir)
    msg = ""
    msg += f"Add {cir_a} + {cir_b} == {expected_cir}"
    print(msg)


def test_circle_mult():
    a = circle.Circle(CONST_TEST_RADIUS)
    b = CONST_TEST_RADIUS
    c = a * b
    expected_cir = circle.Circle(CONST_TEST_RADIUS * CONST_TEST_RADIUS)
    assert str(c) == str(expected_cir)
    msg = ""
    msg += f"Mult {a} * {b} == {expected_cir}"
    print(msg)


def test_comparison_operators():
    cir_1 = circle.Circle(1)
    cir_2 = circle.Circle(2)
    cir_3 = circle.Circle(3)
    cir_4 = circle.Circle(4)
    cir_5 = circle.Circle(5)
    assert str(cir_1) == str(cir_1)
    assert str(cir_1) <= str(cir_2)
    assert str(cir_2) >= str(cir_1)
    ary_cir = []
    ary_cir.append(cir_2)
    ary_cir.append(cir_1)
    ary_cir.append(cir_5)
    ary_cir.append(cir_4)
    ary_cir.append(cir_3)
    print(f"unsorted circles {ary_cir}")
    ary_cir.sort()
    print(f"sorted circles {ary_cir}")


def test_sphere_volume():
    sph = circle.Sphere(CONST_TEST_RADIUS)
    expected_vol = (4/3) * math.pi * (CONST_TEST_RADIUS**3)
    assert str(sph.volume) == str(expected_vol)
    msg = ""
    msg += f"Sphere with radius {sph.radius} has volume {sph.volume}"
    print(msg)


def test_sphere_area():
    sph = circle.Sphere(CONST_TEST_RADIUS)
    expected_area = (4 * math.pi * (CONST_TEST_RADIUS**2))
    assert str(sph.area) == str(expected_area)
    msg = ""
    msg += f"Sphere with radius {sph.radius} has area {sph.area}"
    print(msg)


def test_sphere_add():
    sph_a = circle.Sphere(CONST_TEST_RADIUS)
    sph_b = circle.Sphere(CONST_TEST_RADIUS+1)
    sph_c = sph_a + sph_b
    expected_radius = (CONST_TEST_RADIUS + (CONST_TEST_RADIUS+1))
    assert sph_c.radius == expected_radius
    msg = ""
    msg += f"Add {sph_a} + {sph_b} == Sphere with radius: {expected_radius}"
    print(msg)


def test_sphere_comparison_operators():
    sph_1 = circle.Sphere(1)
    sph_2 = circle.Sphere(2)
    sph_3 = circle.Sphere(3)
    assert str(sph_1) == str(sph_1)
    assert str(sph_1) <= str(sph_2)
    assert str(sph_3) >= str(sph_1)
    ary_sph = []
    ary_sph.append(sph_2)
    ary_sph.append(sph_3)
    ary_sph.append(sph_1)
    print(f"unsorted spheres {ary_sph}")
    ary_sph.sort()
    print(f"sorted spheres {ary_sph}")


###################################

# main, test funcs

if __name__ == "__main__":
    i = 0
    test_circle_creation()
    test_circle_property_diameter()
    test_circle_set_diameter()
    test_circle_area()
    test_cls_method()
    test_circle_str()
    test_circle_repr()
    test_circle_add()
    test_circle_mult()
    test_comparison_operators()
    test_sphere_volume()
    test_sphere_area()
    test_sphere_add()
    test_sphere_comparison_operators()
