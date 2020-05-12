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

	def __str__(self):
		return f'The radius is {self.radius}'

	def __repr__(self):
		return f'Circle({self.radius})'

	@property
	def diameter(self):
		return self.radius * 2

	@diameter.setter
	def diameter(self, diameter):
		self.radius = diameter / 2

	@property
	def area(self):
		return math.pi * self.radius * self.radius

	@classmethod
	def from_diameter(cls, diameter):
		self = cls()
		self.radius = diameter / 2
		return self












