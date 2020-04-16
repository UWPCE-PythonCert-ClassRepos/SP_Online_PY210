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

