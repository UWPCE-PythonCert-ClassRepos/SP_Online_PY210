#/usr/bin/env python3
from math import pi
from io import StringIO
import contextlib

from circle import Circle, Sphere

# Circle tests

circle1 = Circle(2)
circle2 = Circle(3)

def test_radius():
	assert circle1.radius == 2
	assert circle2.radius == 3

def test_diameter():
	assert circle1.diameter == circle1.radius * 2
	assert circle2.diameter == circle2.radius * 2

def test_area():
	def area(radius):
		return pi * radius ** 2

	assert circle1.area == area(circle1.radius)
	assert circle2.area == area(circle2.radius)

def test_add():
	assert circle1 + circle2 == circle1.radius + circle2.radius

def test_mul():
	assert circle1 * circle2 == circle1.radius * circle2.radius

def test_lt():
	assert circle1 < circle2 

def test_le():
	assert circle1 <= circle2

def test_gt():
	assert circle2 > circle1

def test_ge():
	assert circle2 >= circle1

def test_eq():
	circle3 = Circle(2)
	assert circle1 == circle3

def test_ne():
	assert circle1 != circle2

def test_str():
	temp_stdout = StringIO()
	with contextlib.redirect_stdout(temp_stdout):
		print(circle2)
	output = temp_stdout.getvalue().strip()
	assert "Circle with radius: 3" in output

def test_repr():
	temp_stdout = StringIO()
	with contextlib.redirect_stdout(temp_stdout):
		print(repr(circle2))
	output = temp_stdout.getvalue().strip()
	assert "Circle(3)" in output
	
# Sphere tests

sphere1 = Sphere(2)
sphere2 = Sphere(3)

def test_volume():
	assert sphere1.volume == 33.510321638291124

def test_area():
	assert sphere1.surface_area == 50.26548245743669

def test_radius():
	assert sphere1.radius == 2

def test_diameter():
	assert sphere1.diameter == 4

def test_gt():
	assert sphere2 > sphere1

def test_add():
	assert sphere1 + sphere2 == sphere1.radius + sphere2.radius

def test_mul():
	assert sphere1 * sphere2 == sphere1.radius * sphere2.radius

def test_lt():
	assert sphere1 < sphere2 

def test_le():
	assert sphere1 <= sphere2

def test_gt():
	assert sphere2 > sphere1

def test_ge():
	assert sphere2 >= sphere1

def test_eq():
	circle3 = Circle(2)
	assert sphere1 == circle3

def test_ne():
	assert sphere1 != sphere2

def test_str():
	temp_stdout = StringIO()
	with contextlib.redirect_stdout(temp_stdout):
		print(sphere2)
	output = temp_stdout.getvalue().strip()
	assert "Sphere with radius: 3" in output

def test_repr():
	temp_stdout = StringIO()
	with contextlib.redirect_stdout(temp_stdout):
		print(repr(sphere2))
	output = temp_stdout.getvalue().strip()
	assert "Sphere(3)" in output