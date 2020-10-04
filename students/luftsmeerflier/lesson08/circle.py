#/usr/bin/env python3
from math import pi


class Circle:
	def __init__(self, radius):
		self.radius = radius 

	@property
	def diameter(self):
		diameter = self.radius * 2
		return diameter

	@diameter.setter 
	def diameter(self, diameter):
		self.radius = diameter / 2

	@property
	def area(self):
		return pi * self.radius ** 2

	@classmethod
	def from_diameter(class_object, diameter):
		radius = diameter / 2
		return class_object(radius)

	def __repr__(self):
		return 'Circle({})'.format(self.radius)

	def __str__(self):
		return 'Circle with radius: {}'.format(self.radius)

	def __add__(self, other):
		return self.radius + other.radius

	def __mul__(self, other):
		return self.radius * other.radius

	def __lt__(self, other):
		return self.radius < other.radius

	def __le__(self, other):
		return self.radius <= other.radius

	def __gt__(self, other):
		return self.radius > other.radius

	def __ge__(self, other):
		return self.radius >= other.radius

	def __eq__(self, other):
		return self.radius == other.radius

	def __ne__(self, other):
		return self.radius != other.radius

class Sphere(Circle):
	def __init__(self, radius):
		self.radius = radius

	@property
	def volume(self):
		volume = (4/3) * pi * self.radius **3
		return volume

	@property
	def diameter(self):
		diameter = self.radius * 2
		return diameter

	@diameter.setter 
	def diameter(self, diameter):
		self.radius = diameter / 2

	@property
	def surface_area(self):
		return pi * self.radius ** 2

	@property
	def surface_area(self):
		return 4 * pi * self.radius ** 2

	def __repr__(self):
		return 'Sphere({})'.format(self.radius)

	def __str__(self):
		return 'Sphere with radius: {}'.format(self.radius)

# sphere1 = Sphere(2)
# print(repr(sphere1))

s = Sphere.from_diameter(4)
print(s.diameter)
