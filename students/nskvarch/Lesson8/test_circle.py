#!usr/bin/env python3
# Circle Class exercise test file for Lesson 8, created by Niels Skvarch

import math
import unittest
import pytest
from circle import *


class TestCaseOne(unittest.TestCase):
    def test_init(self):
        r = 5
        c = Circle(r)
        assert c.radius == 5

    def test_diameter(self):
        r = 10
        c = Circle(r)
        assert c.diameter == 20

    def test_area(self):
        r = 2
        c = Circle(r)
        print(c.area)
        assert c.area == pytest.approx(12.56637)

    def test_set_diameter(self):
        r = 10
        c = Circle(r)
        assert c.diameter == 20
        c.diameter = 10
        assert c.radius == 5

    def test_str(self):
        c = Circle(5)
        print(str(c))
        assert str(c) == "A circle with a radius of: 5"

    def test_repr(self):
        c = Circle(6)
        print(repr(c))
        assert repr(c) == "Circle(6)"

    def test_circle_math(self):
        c1 = Circle(5)
        c2 = Circle(10)
        c3 = Circle(5)
        assert c1 + c2 == Circle(15)
        assert c1 * 2 == Circle(10)
        assert 2 * c2 == Circle(20)
        assert c1 * 5 == 5 * c1
        assert (c2 // 2) == Circle(5)
        assert (c1 > c2) is False
        assert (c1 < c2) is True
        assert (c1 == c2) is False
        assert (c1 == c3) is True


class TestCaseTwo(unittest.TestCase):
    def test_sphere_init(self):
        r = 5
        s = Sphere(r)
        assert s.radius == 5

    def test_sphere_area(self):
        r = 5
        s = Sphere(r)
        print(s.area)
        assert s.area == pytest.approx(314.1592)

    def test_sphere_volume(self):
        r = 5
        s = Sphere(r)
        print(s.volume)
        assert s.volume == pytest.approx(523.5987)


# main program name-space
if __name__ == "__main__":
    unittest.main()

