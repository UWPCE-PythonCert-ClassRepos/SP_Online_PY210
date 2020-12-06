""" 
test code for circle.py
"""

from circle import *
import io
from math import pi
import pytest
from unittest import mock
from unittest import TestCase

class Test_Radius(TestCase):
    @mock.patch('circle.input', create=True)
    
    def test_init(self, mocked_input):
        """
        This tests that the circle class is initialized correctly.
        """
        mocked_input.side_effect = ['No']
        c = Circle(4)
        assert c.radius == 4 

class Test_Diameter(TestCase):
    @mock.patch('circle.input', create=True)

    def test_diamater(self, mocked_input):
        mocked_input.side_effect = ['Yes', '10']
        c = Circle(4)
        assert c.diameter == 10 
        assert c.radius == 5

class Test_Area(TestCase):
    @mock.patch('circle.input', create=True)

    def test_area(self, mocked_input):
        mocked_input.side_effect = ['No']
        c = Circle(4)
        c.calculate_area()
        assert c.area > 50 and c.area < 51

class Test_Alt_Construct(TestCase):
    @mock.patch('circle.input', create=True)

    def test_alt_construct(self, mocked_input):
        mocked_input.side_effect =['No']
        c = Circle.from_diameter(10)
        assert c.diameter == 10
        assert c.radius == 5

class Test_Print(TestCase):
    @mock.patch('circle.input', create=True)

    def test_print(self, mocked_input):
        mocked_input.side_effect =['No']
        c = Circle(4)
        assert c.__str__() == "Circle(radius=4, diamter=8, area=50.26548245743669)"
        assert c.__repr__() == {'area': 50.26548245743669, 'diameter': 8, 'radius': 4}

class Test_Add_Circles(TestCase):
    @mock.patch('circle.input', create=True)

    def test_add_circles(self, mocked_input):
        mocked_input.side_effect =['No', 'No', 'No']
        c1 = Circle(4)
        c2 = Circle(2)
        c3 = c1.add_circles(c2)
        assert c3.radius == 6

class Test_Multiply_Circle(TestCase):
    @mock.patch('circle.input', create=True)

    def test_multiply_circle(self, mocked_input):
        mocked_input.side_effect =['No', 'No']
        c1 = Circle(4)
        c2 = c1.multiply_circle(2)
        assert c2.radius == 8

class Test_Compare_Circles(TestCase):
    @mock.patch('circle.input', create=True)

    def test_compare_circles(self, mocked_input):
        mocked_input.side_effect =['No', 'No', 'No']
        c1 = Circle(4)
        c2 = c1.multiply_circle(2)
        c3 = Circle(4)
        assert c1.equal_circle(c3) == True
        assert c1.greater_circle(c2) == False
        assert c1.less_circle(c2) == True

class Test_Sort_Circles(TestCase):
    @mock.patch('circle.input', create=True)

    def test_sort_circles(self, mocked_input):
        mocked_input.side_effect =['No', 'No', 'No', 'No', 'No']
        circle1 = Circle(1)
        circles = [circle1, Circle(6), Circle(0), Circle(10), Circle(5)]
        sorted_circles = circle1.sort_cirles(circles)
        correct_values = [0, 1, 5, 6, 10]
        i=0 
        for circle in sorted_circles:
            assert circle.radius == correct_values[i]
            i += 1

    class Test_Sphere_Radius(TestCase):
        @mock.patch('circle.input', create=True)
    
        def test_init(self, mocked_input):
            """
            This tests that the circle class is initialized correctly.
            """
            mocked_input.side_effect = ['No']
            s = Sphere(4)
            assert s.radius == 4 

class Test_Sphere_Diameter(TestCase):
    @mock.patch('circle.input', create=True)

    def test_diamater(self, mocked_input):
        mocked_input.side_effect = ['Yes', '10']
        s = Sphere(4)
        assert s.diameter == 10 
        assert s.radius == 5

class Test_Sphere_Surface_Area(TestCase):
    @mock.patch('circle.input', create=True)

    def test_area(self, mocked_input):
        mocked_input.side_effect = ['No']
        s = Sphere(4)
        s.calculate_area()
        assert s.area > 201 and s.area < 202

class Test_Sphere_Volume(TestCase):
    @mock.patch('circle.input', create=True)

    def test_area(self, mocked_input):
        mocked_input.side_effect = ['No']
        s = Sphere(4)
        s.calculate_volume()
        assert s.volume > 268 and s.volume < 269

class Test_Sphere_Alt_Construct(TestCase):
    @mock.patch('circle.input', create=True)

    def test_alt_construct(self, mocked_input):
        mocked_input.side_effect =['No']
        s = Sphere.from_diameter(10)
        assert s.diameter == 10
        assert s.radius == 5

class Test_Sphere_Print(TestCase):
    @mock.patch('circle.input', create=True)

    def test_print(self, mocked_input):
        mocked_input.side_effect =['No']
        s = Sphere(4)
        assert s.__str__() == "Sphere(radius=4, diamter=8, area=201.06192982974676, volume=268.082573106329)"
        assert s.__repr__() == {'radius': 4, 'diameter': 8, 'area': 201.06192982974676, 'volume': 268.082573106329}