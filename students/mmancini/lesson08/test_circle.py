#!/usr/bin/env python3

import pytest
import circle


###################################


def test_circle_creation():
    i = 0
    cir = circle.Circle(4)
    assert cir.radius == 4


def test_circle_2():
    i = 0


###################################

# main, test funcs

if __name__ == "__main__":
    i = 0
    test_circle_creation()
    # test_circle_2()
