#!/usr/bin/env python3

from pytest import mark, raises
from circle import Circle, Sphere


@mark.Circle
class CircleTests:

    @mark.radius
    @mark.parametrize("test_input, expected", [
        (10, 10),
        (1, 1),
        (100, 100),
        (0.1, 0.1)
    ])
    def test_radius(self, test_input, expected):
        c = Circle(test_input)
        assert c.radius == expected

    @mark.radius
    @mark.parametrize("test_input, expected", [
        (10, 20),
        (0.10, 0.20),
        (100, 200),
        (0.01, 0.02)
    ])
    def test_radius_diameter(self, test_input, expected):
        c = Circle(test_input)
        assert c.diameter == expected

    @mark.radius
    @mark.parametrize("test_input, expected", [
        (0, ValueError),
        (-10, ValueError),
        (-1, ValueError),
        (-0.99, ValueError)
    ])
    def test_radius_error(self, test_input, expected):
        with raises(expected):
            Circle(test_input)

    @mark.diameter
    @mark.parametrize("test_input, expected", [
        (10, 10),
        (1, 1),
        (100, 100),
        (0.1, 0.1)
    ])
    def test_diameter(self, test_input, expected):
        c = Circle.from_diameter(test_input)
        assert c.diameter == expected

    @mark.diameter
    @mark.parametrize("test_input, expected", [
        (10, 5),
        (1, 0.5),
        (100, 50),
        (0.1, 0.05)
    ])
    def test_diameter_radius(self, test_input, expected):
        c = Circle.from_diameter(test_input)
        assert c.radius == expected

    @mark.diameter
    @mark.parametrize("test_input, expected", [
        (0, ValueError),
        (-10, ValueError),
        (-1, ValueError),
        (-0.99, ValueError)
    ])
    def test_diameter_error(self, test_input, expected):
        with raises(expected):
            Circle.from_diameter(test_input)

    @mark.area
    @mark.parametrize("test_input, expected", [
        (10, 314.16),
        (1, 3.14),
        (100, 31415.93),
        (0.1, 0.03)
    ])
    def test_area_from_radius(self, test_input, expected):
        c = Circle(test_input)
        assert c.area == expected

    @mark.area
    @mark.parametrize("test_input, expected", [
        (20, 314.16),
        (2, 3.14),
        (200, 31415.93),
        (0.2, 0.03)
    ])
    def test_area_from_diameter(self, test_input, expected):
        c = Circle.from_diameter(test_input)
        assert c.area == expected

    @mark.area
    @mark.parametrize("test_input, expected", [
        (10, TypeError),
        (1, TypeError),
        (100, TypeError),
        (0.1, TypeError)
    ])
    def test_area_error(self, test_input, expected):
        with raises(expected):
            Circle.area(test_input)

    @mark.add
    @mark.parametrize("test_input, expected", [
        ([10.50, 11.01], 21.51),
        ([0.336, 0.11], 0.45),
        ([13, 27], 40),
        ([5, 17.99], 22.99)
    ])
    def test_add_radius(self, test_input, expected):
        c1 = Circle(test_input[0])
        c2 = Circle(test_input[1])
        c3 = c1 + c2
        assert c3.radius == expected

    @mark.add
    @mark.parametrize("test_input, expected", [
        ([21.00, 22.02], 21.51),
        ([0.672, 0.22], 0.45),
        ([26, 54], 40),
        ([10, 35.98], 22.99)
    ])
    def test_add_diameter(self, test_input, expected):
        c1 = Circle.from_diameter(test_input[0])
        c2 = Circle.from_diameter(test_input[1])
        c3 = c1 + c2
        assert c3.radius == expected

    @mark.add
    @mark.parametrize("test_input, expected", [
        ([10, 2.25], 12.25),
        ([0.25, 0.75], 1.00)
    ])
    def test_iadd(self, test_input, expected):
        c = Circle(test_input[0])
        c1 = Circle(test_input[1])
        c += c1
        assert c.radius == expected

    @mark.mult
    @mark.parametrize("test_input, expected", [
        ([12.0, 4.02], 48.24),
        ([10, 10], 100.00),
        ([0.99, 0.99], 0.98),
        ([5.0, 6], 30.00),
    ])
    def test_mult(self, test_input, expected):
        c = Circle(test_input[0]) * test_input[1]
        assert c.radius == expected

    @mark.mult
    @mark.parametrize("test_input, expected", [
        ([12.0, 4.02], 48.24),
        ([10, 10], 100.00),
        ([0.99, 0.99], 0.98),
        ([5.0, 6], 30.00),
    ])
    def test_mult_reversed(self, test_input, expected):
        c = test_input[1] * Circle(test_input[0])
        assert c.radius == expected

    @mark.mult
    @mark.parametrize("test_input, expected", [
        ([0.25, 0.25], 0.06),
        ([25, 25], 625)
    ])
    def test_imult(self, test_input, expected):
        c = Circle(test_input[0])
        c1 = Circle(test_input[1])
        c *= c1
        assert c.radius == expected

    @mark.comparison
    @mark.parametrize("test_input, expected", [
        ([20, 20.00], True),
        ([0.10, 0.1], True),
        ([0.10, 0.11], False),
        ([99, 98.99], False)
    ])
    def test_eq(self, test_input, expected):
        c1 = Circle(test_input[0])
        c2 = Circle(test_input[1])
        assert bool(c1 == c2) is expected

    @mark.comparison
    @mark.parametrize("test_input, expected", [
        ([20, 19.99], True),
        ([0.10, 0.11], True),
        ([0.10, 0.10], False),
        ([10, 10.00], False)
    ])
    def test_ne(self, test_input, expected):
        c1 = Circle(test_input[0])
        c2 = Circle(test_input[1])
        assert bool(c1 != c2) is expected

    @mark.comparison
    @mark.parametrize("test_input, expected", [
        ([20.01, 20.00], True),
        ([0.98, 0.9], True),
        ([0.10, 0.11], False),
        ([98.98, 98.99], False)
    ])
    def test_gt(self, test_input, expected):
        c1 = Circle(test_input[0])
        c2 = Circle(test_input[1])
        assert bool(c1 > c2) is expected

    @mark.comparison
    @mark.parametrize("test_input, expected", [
        ([19.99, 20.00], True),
        ([0.10, 0.11], True),
        ([0.11, 0.10], False),
        ([99, 98.99], False)
    ])
    def test_lt(self, test_input, expected):
        c1 = Circle(test_input[0])
        c2 = Circle(test_input[1])
        assert bool(c1 < c2) is expected

    @mark.comparison
    @mark.parametrize("test_input, expected", [
        ([20, 20.00], True),
        ([0.11, 0.10], True),
        ([0.10, 0.11], False),
        ([98.98, 98.99], False)
    ])
    def test_ge(self, test_input, expected):
        c1 = Circle(test_input[0])
        c2 = Circle(test_input[1])
        assert bool(c1 >= c2) is expected

    @mark.comparison
    @mark.parametrize("test_input, expected", [
        ([20, 20.00], True),
        ([0.10, 0.11], True),
        ([0.12, 0.11], False),
        ([99, 98.99], False)
    ])
    def test_le(self, test_input, expected):
        c1 = Circle(test_input[0])
        c2 = Circle(test_input[1])
        assert bool(c1 <= c2) is expected

    @mark.sort
    @mark.parametrize("test_input, expected", [
        ([Circle(2), Circle(2.1), Circle(2.34), Circle(2.3), Circle(2.21), Circle(3), Circle(2.98), Circle(2.99),
          Circle(2.5), Circle(2.54), Circle(2.2)], [Circle(2), Circle(2.1), Circle(2.2), Circle(2.21), Circle(2.3),
                                                    Circle(2.34), Circle(2.5), Circle(2.54), Circle(2.98), Circle(2.99),
                                                    Circle(3)])
    ])
    def test_sort(self, test_input, expected):
        circles = test_input
        circles.sort()
        assert circles == expected


@mark.Sphere
class SphereTests:

    @mark.radius
    @mark.parametrize("test_input, expected", [
        (10, 10),
        (1, 1),
        (100, 100),
        (0.1, 0.1)
    ])
    def test_sphere_radius(self, test_input, expected):
        s = Sphere(test_input)
        assert s.radius == expected

    @mark.radius
    @mark.parametrize("test_input, expected", [
        (10, 20),
        (0.10, 0.20),
        (100, 200),
        (0.01, 0.02)
    ])
    def test_sphere_radius_diameter(self, test_input, expected):
        s = Sphere(test_input)
        assert s.diameter == expected

    @mark.diameter
    @mark.parametrize("test_input, expected", [
        (10, 10),
        (1, 1),
        (100, 100),
        (0.1, 0.1)
    ])
    def test_sphere_diameter(self, test_input, expected):
        s = Sphere.from_diameter(test_input)
        assert s.diameter == expected

    @mark.diameter
    @mark.parametrize("test_input, expected", [
        (10, 5),
        (1, 0.5),
        (100, 50),
        (0.1, 0.05)
    ])
    def test_sphere_diameter_radius(self, test_input, expected):
        s = Sphere.from_diameter(test_input)
        assert s.radius == expected

    @mark.volume
    @mark.parametrize("test_input, expected", [
        (10, 4188.79),
        (1, 4.19),
        (100, 4188790.2),
        (0.1, 0.0)
    ])
    def test_sphere_volume_from_radius(self, test_input, expected):
        s = Sphere(test_input)
        assert s.volume == expected

    @mark.volume
    @mark.parametrize("test_input, expected", [
        (20, 4188.79),
        (2, 4.19),
        (200, 4188790.2),
        (0.2, 0.0)
    ])
    def test_sphere_volume_from_diameter(self, test_input, expected):
        s = Sphere.from_diameter(test_input)
        assert s.volume == expected

    @mark.area
    @mark.parametrize("test_input, expected", [
        (10, 1256.64),
        (1, 12.56),
        (100, 125663.72),
        (0.1, 0.12)
    ])
    def test_sphere_area_from_radius(self, test_input, expected):
        s = Sphere(test_input)
        assert s.area == expected

    @mark.area
    @mark.parametrize("test_input, expected", [
        (20, 1256.64),
        (2, 12.56),
        (200, 125663.72),
        (0.2, 0.12)
    ])
    def test_sphere_area_from_diameter(self, test_input, expected):
        s = Sphere.from_diameter(test_input)
        assert s.area == expected
