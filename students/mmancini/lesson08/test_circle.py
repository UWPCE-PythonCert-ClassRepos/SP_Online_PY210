#!/usr/bin/env python3

import pytest
import circle


CONST_TEST_RADIUS = 5

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



###################################

# main, test funcs

if __name__ == "__main__":
    i = 0
    test_circle_creation()
    test_circle_property_diameter()
