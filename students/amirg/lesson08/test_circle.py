'''Tests the circle.py code'''
import unittest
import pytest
import math as m
import circle as c

'''Unittest class'''
class test_circle(unittest.TestCase):
    #tests circle initialization
    def test_Circle_init(self):
        ci = c.Circle(4)
        self.assertEqual(ci.radius, 4)

    #tests diameter property
    def test_diameter_property(self):
        ci = c.Circle(4)
        self.assertEqual(ci.diameter, 8)

    #tests diameter setter
    def test_diameter_setter(self):
        ci = c.Circle(4)
        ci.diameter = 4
        self.assertEqual(ci.radius, 2)
        self.assertEqual(ci.diameter, 4)    

    #tests area property
    def test_area_property(self):
        ci = c.Circle(4)
        self.assertEqual(ci.area, 16 * m.pi)

    #tests area setter (raises exception)
    def test_area_setter(self):
        ci = c.Circle(4)
        with pytest.raises(AttributeError):
            ci.area = 4

    #tests diameter initialization
    def test_from_diameter(self):
        ci = c.Circle.from_diameter(8)
        self.assertEqual(ci.radius, 4)
        self.assertEqual(ci.diameter, 8)

    #tests circle string property
    def test_str(self):
        ci = c.Circle(4)
        self.assertEqual(str(ci), 'Circle with radius: 4')

    #tests circle repr property
    def test_repr(self):
        ci = c.Circle(4)
        self.assertEqual(repr(ci), 'Circle(4)')

    #tests adding of Circle properties
    def test_add(self):
        ci = c.Circle(4)
        cl = c.Circle(2)
        self.assertEqual(ci + cl, c.Circle(6))

    #tests multiplying of Circle properties
    def test_mul(self):
        ci = c.Circle(4)
        self.assertEqual(3 * cl, c.Circle(12))

    #tests reverse multipying of Circle properties
    def test_rmul(self):
        ci = c.Circle(4)
        self.assertEqual(ci * 3, c.Circle(12))

    #tests comparisions
    def test_lt_gt_eq(self):
        ci = c.Circle(4)
        cl = c.Circle(2)
        cj = c.Circle(1)
        ck = c.Circle(1)
        self.assertTrue(ci > cj)
        self.assertTrue(cj < cl)
        self.assertFalse(cj > ci)
        self.assertFalse(cl < cj)
        self.assertTrue(cj == ck)
        self.assertFalse(ci == cj)

    #tests sphere string property
    def test_sphere_str(self):
        ci = c.Sphere(4)
        self.assertEqual(str(ci), 'Sphere with radius: 4')

    #tests sphere repr property
    def test_sphere_repr(self):
        ci = c.Sphere(4)
        self.assertEqual(repr(ci), 'Sphere(4)')

    #tests sphere volume
    def test_volume(self):
        ci = c.Sphere(4)
        self.assertEqual(ci.volume, (256/3)*m.pi)

    #tests sphere area
    def test_sphere_area(self):
        ci = c.Sphere(4)
        self.assertEqual(ci.area, 64*m.pi)

    #tests if type is sphere if initialized from diameter
    def test_sphere_from_diameter(self):
        ci = c.Sphere.from_diameter(8)
        assert type(ci) is c.Sphere