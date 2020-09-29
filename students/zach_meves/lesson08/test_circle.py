"""
Test circle.py
"""

import unittest
import os
from circle import *
import math


class TestCircle(unittest.TestCase):
    """Tests the Circle class."""

    def setUp(self) -> None:
        self.c1 = Circle(1)
        self.c2 = Circle(1.5)

    def test_init(self):
        """Test constructor."""
        c = Circle(3)
        self.assertEqual(c.radius, 3)

        with self.assertRaises(TypeError):
            c = Circle()
        with self.assertRaises(TypeError):
            c = Circle(3, 2)

    def test_get_radius(self):
        self.assertEqual(self.c1.radius, 1)
        self.assertEqual(self.c2.radius, 1.5)

    def test_set_radius(self):
        self.c1.radius = 3.2
        self.assertEqual(self.c1.radius, 3.2)
        self.assertEqual(self.c1.diameter, 6.4)

        self.c2.radius = 1
        self.assertEqual(self.c2.radius, 1)
        self.assertEqual(self.c2.diameter, 2)

        with self.assertRaises(ValueError):
            self.c2.radius = -1

    def test_get_diameter(self):
        self.assertEqual(self.c1.diameter, 2*self.c1.radius)
        self.assertEqual(self.c2.diameter, 2*self.c2.radius)

    def test_set_diameter(self):
        self.c1.diameter = .2
        self.assertEqual(self.c1.radius, .1)
        self.assertEqual(self.c1.diameter, .2)

        self.c2.diameter = 0
        self.assertEqual(self.c2.radius, 0)

        with self.assertRaises(ValueError):
            self.c1.diameter = -.2

    def test_area(self):
        self.assertEqual(self.c1.area, math.pi * self.c1.radius ** 2)
        self.assertEqual(self.c2.area, math.pi * self.c2.radius ** 2)
        with self.assertRaises(AttributeError):
            self.c1.area = 3.2

    def test_from_diameter(self):
        c = Circle.from_diameter(3)
        self.assertEqual(c.diameter, 3)
        self.assertEqual(c.radius, 1.5)

        with self.assertRaises(TypeError):
            c = Circle.from_diameter(3, 2)
        with self.assertRaises(TypeError):
            c = Circle.from_diameter()

    def test_repr(self):
        self.assertEqual(repr(self.c1), "Circle(1)")
        self.assertEqual(repr(self.c2), "Circle(1.5)")

        c1 = eval(repr(self.c1))
        self.assertEqual(c1.radius, self.c1.radius)
        c2 = eval(repr(self.c2))
        self.assertEqual(self.c2.radius, c2.radius)

    def test_str(self):
        self.assertEqual(str(self.c1), "Circle with radius: 1.000000")
        self.assertEqual(str(self.c2), "Circle with radius: 1.500000")

    def test_add_sub(self):
        c3 = self.c1 + self.c2
        self.assertEqual(c3.radius, 2.5)
        self.assertEqual(self.c1.radius, 1)

        c4 = self.c2 - self.c1
        self.assertEqual(c4.radius, .5)

        with self.assertRaises(ValueError):
            c5 = self.c1 - self.c2
        with self.assertRaises(TypeError):
            c5 = self.c1 + 4

        with self.assertRaises(TypeError):
            c5 = self.c1 - .2

        self.assertEqual(self.c1 + self.c2, self.c2 + self.c1)

    def test_multiply_divide(self):
        c3 = 3 * self.c1
        self.assertEqual(c3.radius, 3 * self.c1.radius)
        self.assertEqual(self.c1.radius, 1)

        c3 = self.c1 *43
        self.assertEqual(c3.radius, 43 * self.c1.radius)

        c4 = self.c1 / 2
        self.assertEqual(c4.radius, self.c1.radius / 2)

        with self.assertRaises(TypeError):
            x = 2 / self.c1

        with self.assertRaises(TypeError):
            x = self.c1 * self.c2

        with self.assertRaises(TypeError):
            x = self.c1 / self.c2

        self.assertEqual(2 * self.c2, self.c2 * 2)

    def test_inplace(self):
        self.c1 += self.c2
        self.assertEqual(self.c1.radius, 2.5)

        self.c2 *= 3
        self.assertEqual(self.c2, Circle(1.5 * 3))

        c = Circle(5.2)
        c -= Circle(2.2)
        self.assertEqual(c.radius, 3)

        c = Circle(8)
        c /= 2
        self.assertEqual(c.radius, 4)

    def test_compare(self):
        self.assertTrue(self.c1 < self.c2)
        self.assertTrue(self.c1 <= self.c2)
        self.assertTrue(self.c1 <= Circle(1))

        self.assertFalse(self.c2 < self.c1)
        self.assertFalse(self.c2 <= self.c1)

        self.assertTrue(self.c2 > self.c1)
        self.assertTrue(self.c2 >= self.c2)
        self.assertTrue(self.c2 >= Circle(1.5))

        self.assertFalse(self.c1 > self.c2)
        self.assertFalse(self.c1 >= self.c2)

        self.assertTrue(self.c1 == Circle(1))
        self.assertFalse(self.c1 == self.c2)
        self.assertTrue(self.c1 != self.c2)
        self.assertFalse(self.c1 != Circle(1))

    def test_sort(self):
        lst = [0, 1, 5, 3, 9, 6, 2.2, 1.2]
        circles = []
        for radius in lst:
            circles.append(Circle(radius))

        circles.sort()
        self.assertEqual([c.radius for c in circles], sorted(lst))

    def test_pow(self):
        self.assertEqual(self.c1 ** 1, self.c1)
        self.assertEqual(self.c1 ** 2, Circle(self.c1.radius ** 2))
        self.assertEqual(self.c2 ** .2, Circle(self.c2.radius ** .2))

        with self.assertRaises(TypeError):
            self.c1 ** self.c2


class TestSphere(unittest.TestCase):
    """Test the Sphere class."""

    def setUp(self) -> None:
        self.c1 = Sphere(1)
        self.c2 = Sphere(1.5)

    def test_init(self):
        """Test constructor."""
        c = Sphere(3)
        self.assertEqual(c.radius, 3)

        with self.assertRaises(TypeError):
            c = Sphere()
        with self.assertRaises(TypeError):
            c = Sphere(3, 2)

    def test_get_radius(self):
        self.assertEqual(self.c1.radius, 1)
        self.assertEqual(self.c2.radius, 1.5)

    def test_set_radius(self):
        self.c1.radius = 3.2
        self.assertEqual(self.c1.radius, 3.2)
        self.assertEqual(self.c1.diameter, 6.4)

        self.c2.radius = 1
        self.assertEqual(self.c2.radius, 1)
        self.assertEqual(self.c2.diameter, 2)

        with self.assertRaises(ValueError):
            self.c2.radius = -1

    def test_get_diameter(self):
        self.assertEqual(self.c1.diameter, 2*self.c1.radius)
        self.assertEqual(self.c2.diameter, 2*self.c2.radius)

    def test_set_diameter(self):
        self.c1.diameter = .2
        self.assertEqual(self.c1.radius, .1)
        self.assertEqual(self.c1.diameter, .2)

        self.c2.diameter = 0
        self.assertEqual(self.c2.radius, 0)

        with self.assertRaises(ValueError):
            self.c1.diameter = -.2

    def test_area(self):
        self.assertEqual(self.c1.area, 4 * math.pi * self.c1.radius ** 2)
        self.assertEqual(self.c2.area, 4 * math.pi * self.c2.radius ** 2)
        with self.assertRaises(AttributeError):
            self.c1.area = 3.2

    def test_volume(self):
        self.assertEqual(self.c1.volume, 4/3 * math.pi * self.c1.radius ** 3)
        self.assertEqual(self.c2.volume, 4 / 3 * math.pi * self.c2.radius ** 3)
        with self.assertRaises(AttributeError):
            self.c1.volume = 3

    def test_from_diameter(self):
        c = Sphere.from_diameter(3)
        self.assertEqual(c.diameter, 3)
        self.assertEqual(c.radius, 1.5)

        with self.assertRaises(TypeError):
            c = Sphere.from_diameter(3, 2)
        with self.assertRaises(TypeError):
            c = Sphere.from_diameter()

    def test_repr(self):
        self.assertEqual(repr(self.c1), "Sphere(1)")
        self.assertEqual(repr(self.c2), "Sphere(1.5)")

        c1 = eval(repr(self.c1))
        self.assertEqual(c1.radius, self.c1.radius)
        c2 = eval(repr(self.c2))
        self.assertEqual(self.c2.radius, c2.radius)

    def test_str(self):
        self.assertEqual(str(self.c1), "Sphere with radius: 1.000000")
        self.assertEqual(str(self.c2), "Sphere with radius: 1.500000")

    def test_add_sub(self):
        c3 = self.c1 + self.c2
        self.assertEqual(c3.radius, 2.5)
        self.assertEqual(self.c1.radius, 1)

        c4 = self.c2 - self.c1
        self.assertEqual(c4.radius, .5)

        with self.assertRaises(ValueError):
            c5 = self.c1 - self.c2
        with self.assertRaises(TypeError):
            c5 = self.c1 + 4

        with self.assertRaises(TypeError):
            c5 = self.c1 - .2

        self.assertEqual(self.c1 + self.c2, self.c2 + self.c1)

    def test_multiply_divide(self):
        c3 = 3 * self.c1
        self.assertEqual(c3.radius, 3 * self.c1.radius)
        self.assertEqual(self.c1.radius, 1)

        c3 = self.c1 *43
        self.assertEqual(c3.radius, 43 * self.c1.radius)

        c4 = self.c1 / 2
        self.assertEqual(c4.radius, self.c1.radius / 2)

        with self.assertRaises(TypeError):
            x = 2 / self.c1

        with self.assertRaises(TypeError):
            x = self.c1 * self.c2

        with self.assertRaises(TypeError):
            x = self.c1 / self.c2

        self.assertEqual(2 * self.c2, self.c2 * 2)

    def test_inplace(self):
        self.c1 += self.c2
        self.assertEqual(self.c1.radius, 2.5)

        self.c2 *= 3
        self.assertEqual(self.c2, Sphere(1.5 * 3))

        c = Sphere(5.2)
        c -= Sphere(2.2)
        self.assertEqual(c.radius, 3)

        c = Sphere(8)
        c /= 2
        self.assertEqual(c.radius, 4)

    def test_compare(self):
        self.assertTrue(self.c1 < self.c2)
        self.assertTrue(self.c1 <= self.c2)
        self.assertTrue(self.c1 <= Sphere(1))

        self.assertFalse(self.c2 < self.c1)
        self.assertFalse(self.c2 <= self.c1)

        self.assertTrue(self.c2 > self.c1)
        self.assertTrue(self.c2 >= self.c2)
        self.assertTrue(self.c2 >= Sphere(1.5))

        self.assertFalse(self.c1 > self.c2)
        self.assertFalse(self.c1 >= self.c2)

        self.assertTrue(self.c1 == Sphere(1))
        self.assertFalse(self.c1 == self.c2)
        self.assertTrue(self.c1 != self.c2)
        self.assertFalse(self.c1 != Sphere(1))

    def test_sort(self):
        lst = [0, 1, 5, 3, 9, 6, 2.2, 1.2]
        spheres = []
        for radius in lst:
            spheres.append(Sphere(radius))

        spheres.sort()
        self.assertEqual([c.radius for c in spheres], sorted(lst))

    def test_pow(self):
        self.assertEqual(self.c1 ** 1, self.c1)
        self.assertEqual(self.c1 ** 2, Sphere(self.c1.radius ** 2))
        self.assertEqual(self.c2 ** .2, Sphere(self.c2.radius ** .2))

        with self.assertRaises(TypeError):
            self.c1 ** self.c2


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    unittest.main()
