from circle import Circle
import pytest
import math

def test_radius():
	c = Circle(4)
	assert c.radius == 4

def test_diameter():
	c = Circle(5)
	assert c.diameter == 10

def test_setDiameter():
	c = Circle(6)
	c.diameter = 3
	assert c.diameter == 3
	assert c.radius == 1.5

def test_area():
	c = Circle(3)
	assert c.area == 28.274333882308138

