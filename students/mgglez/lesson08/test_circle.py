#!/usr/bin/env python

# ------------------------------------------------------------------------------ #
# Title: Lesson08 - Circle Class Exercise
# Description: Assignment from Lesson08 - Circle Class Exercise
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,02-05-2021, Created Circle Class Unit Tests
# ------------------------------------------------------------------------------ #

import unittest
from circle import Circle
import pytest


class TestCircle(unittest.TestCase):

    def test_circle_initialization_str_repr_and_properties(self):
        c1 = Circle(10)
        c2 = Circle.from_diameter(40)
        assert type(c2) == Circle
        self.assertEqual(c1.radius, 10.0)
        self.assertEqual(c1.diameter, 20.0)
        self.assertEqual(c2.radius, 20.0)
        self.assertEqual(c2.diameter, 40.0)
        c1.radius = 30
        self.assertEqual(c1.diameter, 60.0)
        c2.diameter = 30
        self.assertEqual(c2.radius, 15.0)

        self.assertEqual(str(c1), "Circle with radius: 30.000")
        self.assertEqual(repr(c1), "Circle(30.0)")
        self.assertEqual(round(c1.area), 2827)
        with pytest.raises(AttributeError) as error:
            c1.area = 50
            assert "AttributeError: can't set attribute" in error

    def test_circle_comparison(self):
        c1 = Circle(10)
        c2 = Circle.from_diameter(40)
        assert c1 < c2
        assert c2 > c1
        assert c1 != c2
        c3 = eval(repr(c2))
        assert c3 == c2

    def test_circle_add(self):
        c1 = Circle(10)
        c2 = Circle.from_diameter(40)

        c3 = c1 + c2
        assert c3 == Circle(30.0)

        c3 = c1 + 40
        assert c3 == Circle(50.0)

        assert (c1 + 40) == (40 + c1)

        c1 += 40
        assert c1 == Circle(50.0)

    def test_circle_subtraction(self):
        c1 = Circle(10)
        c2 = Circle.from_diameter(40)

        c3 = c2 - c1
        assert c3 == Circle(10.0)

        c3 = c2 - 10
        assert c3 == Circle(10.0)

        assert (c2 - 10) == (30 - c2)

        c2 -= 10
        assert c2 == Circle(10.0)

    def test_circle_multiplication(self):
        c1 = Circle(10)
        c2 = Circle.from_diameter(40)

        c3 = c1 * c2
        assert c3 == Circle(200.0)

        c3 = c1 * 40
        assert c3 == Circle(400.0)

        assert (c1 * 40) == (40 * c1)

        c1 *= 40
        assert c1 == Circle(400.0)

    def test_circle_division(self):
        c1 = Circle(10)
        c2 = Circle.from_diameter(40)

        c3 = c2 / c1
        assert c3 == Circle(2.0)

        c3 = c2 / 10
        assert c3 == Circle(2.0)

        assert (c2 / 10) == (20 / c1)

        c2 /= 10
        assert c2 == Circle(2.0)

    def test_circle_sort(self):
        circle_list = [
            Circle(20),
            Circle(13),
            Circle(36),
            Circle(24),
            Circle(89),
            Circle(77)
        ]
        circle_list.sort()
        assert circle_list == [
            Circle(13),
            Circle(20),
            Circle(24),
            Circle(36),
            Circle(77),
            Circle(89)
        ]

        circle_list.sort(reverse=True)
        assert circle_list == [
            Circle(89),
            Circle(77),
            Circle(36),
            Circle(24),
            Circle(20),
            Circle(13)
        ]


if __name__ == "__main__":
    unittest.main()
