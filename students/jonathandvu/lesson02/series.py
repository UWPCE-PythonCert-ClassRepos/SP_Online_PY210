#!/usr/bin/env python
# PY210 Lesson 2 Fibonocci Series
# Jonathan Vu 08/24/19
#

def fibonocci(n):
	"""fibonocci function will return the nth value in the fibonocci series"""
	"""Input: The nth value to be grabbed in a fibonocci series"""

	# Assign Starting Variables
	int1 = 0
	int2 = 1
	value = n
	
	# Loop through fibonocci until last value
	for i in range(0, value-1):
		# Fibonocci equation
		newInt = int1 + int2
		# Assign first number start to second number
		int2 = int1
		# assign first number to new number
		int1 = newInt
	pass

	print(newInt)

def lucas(n):
	"""lucas series will return the nth value in a lucas series"""
	"""lucas series starts with 2 & 1 instead of 1 & 0"""
	"""Input: The nth value to be grabbed in a lucas series"""

	#Assign Starting Variables
	int1 = 1
	int2 = 2
	value = n
	for i in range(0,value-2):
		newInt = int1 + int2
		int2 = int1
		int1 = newInt
	pass

	print(newInt)

# END CODE