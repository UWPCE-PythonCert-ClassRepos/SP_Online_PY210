#!/usr/bin/env python3

import pytest
import circle_class

class TestCircle():

    def test_radius(self):
        c = circle_class.Circle(4)
        assert c.radius == 4

    def test_diameter(self):
        c = circle_class.Circle(4)
        assert c.diameter == 8

    def test_set_diameter(self):
        c = circle_class.Circle(4)
        c.diameter = 2
        assert c.radius == 1
    
    def test_set_radius(self):
        c = circle_class.Circle(4)
        c.radius = 3
        assert c.diameter == 6

    def test_area(self):
        c = circle_class.Circle(1)
        assert str(c.area).startswith("3.14")
    
    def test_cannot_set_area(self):
        c = circle_class.Circle(1)
        with pytest.raises(AttributeError):
            c.area = 5

    def test_circle_from_diameter(self):
        c = circle_class.Circle.from_diameter(8)
        assert c.diameter == 8
        assert c.radius == 4
    
    def test_str(self):
        c = circle_class.Circle(4)
        assert str(c) == "Circle with radius: 4"

    def test_repr(self):
        c = circle_class.Circle(4)
        assert repr(c) == "Circle(4)"

    def test_add_circle(self):
        c1 = circle_class.Circle(4)
        c2 = circle_class.Circle(2)
        assert c1 + c2 == "Circle(6)"

    def test_sub_circle(self):
        c1 = circle_class.Circle(4)
        c2 = circle_class.Circle(2)
        assert c1 - c2 == "Circle(2)"

    def test_mul_circle(self):
        c1 = circle_class.Circle(4)
        c2 = circle_class.Circle(2)
        assert c1 * c2 == "Circle(8)"

    def test_div_circle(self):
        c1 = circle_class.Circle(4)
        c2 = circle_class.Circle(2)
        assert c1 / c2 == "Circle(2.0)"
    
    def test_comparison(self):
        c1 = circle_class.Circle(4)
        c2 = circle_class.Circle(2)
        assert (c1 == c2) == False
        assert (c1 < c2) == False
        assert (c1 <= c2) == False
        assert (c1 >= c2) == True
        assert (c1 > c2) == True
        assert (c1 != c2) == True
        
    def test_sort(self):
        lst = [circle_class.Circle(5), circle_class.Circle(1), circle_class.Circle(3), circle_class.Circle(2), circle_class.Circle(4)]
        lst.sort()
        assert lst[0] == circle_class.Circle(1)

    def test_sphere(self):
        c = circle_class.Sphere(1)
        assert c.radius ==  1
        assert c.diameter == 2

    # def test_volum(self):
    #     c = circle_class.Sphere(1)
    #     assert str(c.volum).startswith("3.14")

    def test_volum(self):
        c = circle_class.Sphere(2)
        print(c.radius)
        assert str(c.volum).startswith("33.51")

    def test_make_sphere_from_diameter(self):
        c = circle_class.Sphere.from_diameter(8)
        assert c.diameter == 8
        assert c.radius == 4

    def test_area_sphere(self):
        c = circle_class.Sphere(2)
        assert str(c.area).startswith("50.26")

    def test_str_sphere(self):
        c = circle_class.Sphere(4)
        assert str(c) == "Sphere with radius: 4"

    def test_repr_sphere(self):
        c = circle_class.Sphere(4)
        assert repr(c) == "Sphere(4)"

