# ------------------------------------------------------------------------#
# !/usr/bin/env python3
# Title: Circle.py
# Desc: Create a class that represents a simple circle
# Tian Xie, 2020-05-11, Created File
# ------------------------------------------------------------------------#

import math

class Circle(object):
	"""
	A Circle object.
	"""
	def __init__(self, radius):
		self.radius = radius
	# print it out nicely
	def __str__(self):
		return f'Circle with radius: {self.radius}'

	def __repr__(self):
		return f'Circle({self.radius})'

	# numeric protocols
	def __eq__(self, other):
		return self.radius == other.radius

	def __lt__(self, other):
		return self.radius < other.radius

	def __le__(self, other):
		return self.radius <= other.radius

	def __ge__(self, other):
		return self.radius >= other.radius

	def __gt__(self, other):
		return self.radius > other.radius

	def __ne__(self, other):
		return self.radius != other.radius

	# numeric protocols
	def __add__(self, other):
		return Circle(self.radius + other.radius)

	# used in a numeric context on the left side of the multiplication operator
	def __mul__(self, other):
		return Circle(self.radius * other)

	# optional feature to reflect
	def __rmul__(self, other):
		return Circle(self.radius * other)

	# diameter property
	@property
	def diameter(self):
		return self.radius * 2

	# diameter setter
	@diameter.setter
	def diameter(self, diameter):
		self.radius = diameter / 2

	# area property
	@property
	def area(self):
		return math.pi * self.radius * self.radius

	# alternate constructor
	@classmethod
	def from_diameter(cls, diameter):
		return cls(diameter/2)

# Subclass
class Sphere(Circle):
	def __str__(self):
		return f'Sphere with radius: {self.radius}'

	def __repr__(self):
		return f'Sphere({self.radius})'

	# volume property
	@property
	def volume(self):
		return (4 / 3) * math.pi * self.radius ** 3

	# area property
	@property
	def area(self):
		return 4 * math.pi * self.radius ** 2









