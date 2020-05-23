#!/usr/bin/env python3
"""
Series assignment
"""
# Fibonacci series
def fibonacci(n):
	"""This function will return series of numbers with range(n) 
	through Fibonacci Series starting with the integers 0 and 1."""
	fn = 0
	sn = 1
	nn = 0
	for i in range(n):
		while nn < n:
			print(fn)
			nth = fn+sn
			fn = sn
			sn = nth
			nn += 1
# Lucas series 
def lucas(n):
	"""This function will return series of numbers with range(n)
	through Lucas Numbers starting with 2 and 1."""
	fn = 2
	sn = 1
	nn = 0
	for i in range(n):
		while nn < n:
			print(fn)
			nth = fn+sn
			fn = sn
			sn = nth
			nn += 1
# Sum Series
def sum_series(n, n0=0, n1=1):
	"""This function will return series of numbers with range(n)
	using optional numbers n0 and n1, by default n0 = 0 and n1 = 1."""
	fn = n0
	sn = n1
	nn = 0
	for i in range(n):
		while nn < n:
			print(fn)
			nth = fn+sn
			fn = sn
			sn = nth
			nn += 1

			
if __name__== "__main__":
	"""Testing code"""
	# test fibonacci numbers
	#assert fibonacci(0) == 
	assert fibonacci(1) == 0
	assert fibonacci(2) == 1
	assert fibonacci(3) == 1
	assert fibonacci(4) == 2
	assert fibonacci(5) == 3
	assert fibonacci(6) == 5
	assert fibonacci(7) == 8

	#assert lucas(0) == 
	assert lucas(1) == 2

	assert lucas(4) == 4

    # test that sum_series matches fibonacci
	assert sum_series(5) == fibonacci(5)
	assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
	assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
	#assert sum_series(0, 3, 2) == 3
	assert sum_series(1, 3, 2) == 3
	assert sum_series(2, 3, 2) == 2
	assert sum_series(3, 3, 2) == 5
	assert sum_series(4, 3, 2) == 7
	assert sum_series(5, 3, 2) == 12

	print("tests passed")