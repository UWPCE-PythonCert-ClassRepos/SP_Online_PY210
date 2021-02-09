#!/usr/bin/env python

# ------------------------------------------------------------------------------ #
# Title: Lesson08 - Circle Class Exercise
# Description: Assignment from Lesson08 - Circle Class Exercise
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,02-05-2021, Created Sphere Class Unit Tests
# ------------------------------------------------------------------------------ #

import unittest
from sphere import Sphere
import pytest

class TestSphere(unittest.TestCase):

    def test_circle_initialization_str_repr_and_properties(self):
        s1 = Sphere(10)
        s2 = Sphere.from_diameter(40)
        assert type(s2) == Sphere
        self.assertEqual(s1.radius, 10.0)
        self.assertEqual(s1.diameter, 20.0)
        self.assertEqual(s2.radius, 20.0)
        self.assertEqual(s2.diameter, 40.0)
        s1.radius = 30
        self.assertEqual(s1.diameter, 60.0)
        s2.diameter = 30
        self.assertEqual(s2.radius, 15.0)

        self.assertEqual(str(s1), "Sphere with radius: 30.000")
        self.assertEqual(repr(s1), "Sphere(30.0)")
        self.assertEqual(round(s1.area), 11310)
        with pytest.raises(AttributeError) as error:
            s1.area = 50
            assert "AttributeError: can't set attribute" in error

        self.assertEqual(round(s1.volume), 113097)
        with pytest.raises(AttributeError) as error:
            s1.volume = 50
            assert "AttributeError: can't set attribute" in error

    def test_circle_comparison(self):
        s1 = Sphere(10)
        s2 = Sphere.from_diameter(40)
        assert s1 < s2
        assert s2 > s1
        assert s1 != s2
        s3 = eval(repr(s2))
        assert s3 == s2


    def test_circle_add(self):
        s1 = Sphere(10)
        s2 = Sphere.from_diameter(40)

        s3 = s1 + s2
        assert s3 == Sphere(30.0)

        s3 = s1 + 40
        assert s3 == Sphere(50.0)

        assert (s1 + 40) == (40 + s1)

        s1 += 40
        assert s1 == Sphere(50.0)

    def test_circle_subtraction(self):
        s1 = Sphere(10)
        s2 = Sphere.from_diameter(40)

        s3 = s2 - s1
        assert s3 == Sphere(10.0)

        s3 = s2 - 10
        assert s3 == Sphere(10.0)

        assert (s2 - 10) == (30 - s2)

        s2 -= 10
        assert s2 == Sphere(10.0)

    def test_circle_multiplication(self):
        s1 = Sphere(10)
        s2 = Sphere.from_diameter(40)

        s3 = s1 * s2
        assert s3 == Sphere(200.0)

        s3 = s1 * 40
        assert s3 == Sphere(400.0)

        assert (s1 * 40) == (40 * s1)

        s1 *= 40
        assert s1 == Sphere(400.0)

    def test_circle_division(self):
        s1 = Sphere(10)
        s2 = Sphere.from_diameter(40)

        s3 = s2 / s1
        assert s3 == Sphere(2.0)

        s3 = s2 / 10
        assert s3 == Sphere(2.0)

        assert (s2 / 10) == (20 / s1)

        s2 /= 10
        assert s2 == Sphere(2.0)

    def test_circle_sort(self):
        sphere_list = [
            Sphere(20),
            Sphere(13),
            Sphere(36),
            Sphere(24),
            Sphere(89),
            Sphere(77)
        ]

        sphere_list.sort()
        assert sphere_list == [
            Sphere(13),
            Sphere(20),
            Sphere(24),
            Sphere(36),
            Sphere(77),
            Sphere(89)
        ]

        sphere_list.sort(reverse=True)
        assert sphere_list == [
            Sphere(89),
            Sphere(77),
            Sphere(36),
            Sphere(24),
            Sphere(20),
            Sphere(13)
        ]

if __name__ == "__main__":
    unittest.main()