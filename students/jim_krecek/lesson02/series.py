def fibonacci(n):
	""" compute the nth Fibonacci number """
	if n == 0:
		return n
	elif n == 1:
		return n
	else:
		return (fibonacci(n-2) + fibonacci(n-1))
			
def lucas(n):
	""" compute the nth Lucas number """
	if n == 0:
		return 2
	elif n == 1:
		return n
	else:
		return (lucas(n-2) + lucas(n-1))

def sum_series(n, x=0, y=1):
	"""
	compute the nth value of a summation series.

	:param n0=0: value of zeroth element in the series
	:param n1=1: value of first element in the series

	This function should generalize the fibonacci() and the lucas(),
	so that this function works for any first two numbers for a sum series.

	Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
	And sum_series(n, 2, 1) should be equivalent to lucas(n).
	"""
	if n == 0:
		return x
	elif n == 1:
		return y
	else:
		return (sum_series(n-2,x,y) + sum_series(n-1,x,y))
		
	# test block of code 
	
if __name__ == "__main__":
	#tests fib function
	assert fibonacci(0) == 0
	assert fibonacci(1) == 1
	assert fibonacci(5) == 5
	assert fibonacci(10) == 55

	#tests lucas function
	assert lucas(0) == 2
	assert lucas(1) == 1
	assert lucas(5) == 11
	assert lucas(10) == 123

	#tests if sum_series matches fib
	assert sum_series(0) == fibonacci(0)
	assert sum_series(1) == fibonacci(1)
	assert sum_series(5) == fibonacci(5)
	assert sum_series(10) == fibonacci(10)

	# test if sum_series matches lucas
	assert sum_series(0, 2, 1) == lucas(0)
	assert sum_series(1, 2, 1) == lucas(1)
	assert sum_series(5, 2, 1) == lucas(5)
	assert sum_series(10, 2, 1) == lucas(10)

	print("all tests passed")