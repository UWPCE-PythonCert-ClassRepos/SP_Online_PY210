def fibonacci(n): 
	"""
	Returns the nth value within the Fibonacci series, starting with zero index. 

	Fibonacci formula: F(n) = F(n-1) + F(n-2).
	n: the nth number/location in the series
	results/series: 0, 1, 1, 2, 3, 5, 8, 13, ...
	"""
	if n == 0: 
		return 0
	elif n == 1: 
		return 1
	else: 
		return fibonacci(n-1)+fibonacci(n-2) 
	pass			


def lucas(n):
	"""
	Returns the nth value within the Lucas series, starting with zero index.

	The Lucas formula is identical to the Fibonacci formula; however the first two numbers for the Lucas series are 2,1.

	Lucas formula: L(n) = L(n-1) + L(n-2).
	n: the nth number/location in the series
	2, 1, 3, 4, 7, 11, 18, 29, ...
	"""
	if n == 0:
		return 2
	elif n == 1:
		return 1
	else: 
		return lucas(n-1)+lucas(n-2)   
	pass

def sum_series(n, n0=0, n1=1):
	"""
	Returns the nth value within a summation series, starting with zero index.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series
	
	The sum_series function uses the Fibonacci/Lucas function with the option for the user to select the first and second number of the series.
	The formula will default to the Fibonacci formula if the optional parameters are not used.

	The sum_series function has one required parameter and two optional parameters. The required parameter will determine which element in the series to print. 
	The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

	Sum_series formula: S(n) = S(n-1, n0, n1) + S(n-2, n0, n1).
	n: the nth number/location in the series
	n0: first number of the series
	n1: second number of the series
	"""
	if n == 0:
		return n0
	elif n == 1:
		return n1
	else: 
		return sum_series(n-1,n0,n1)+sum_series(n-2,n0,n1) 
	pass


if __name__ == "__main__":
	#fibonacci tests
	assert fibonacci(0) == 0
	assert fibonacci(1) == 1
	assert fibonacci(12) == 144
	assert fibonacci(17) == 1597
	assert fibonacci(29) == 514229

	#lucas tests
	assert lucas(0) == 2
	assert lucas(1) == 1
	assert lucas(8) == 47	
	assert lucas(19) == 9349			
	assert lucas(26) == 271443		

	#test if sum_series works for arbitrary initial values
	assert sum_series(0, 5, 3) == 5
	assert sum_series(1, 5, 3) == 3
	assert sum_series(2, 5, 3) == 8
	assert sum_series(3, 5, 3) == 11
	assert sum_series(4, 5, 3) == 19
	
	#test that sum_series matches fibonacci
	assert sum_series(5) == fibonacci(5)
	assert sum_series(9, 0, 1) == fibonacci(9)

	#test if sum_series matched lucas
	assert sum_series(5, 2, 1) == lucas(5)
	assert sum_series(22, 2, 1) == lucas(22)

	print("tests passed")