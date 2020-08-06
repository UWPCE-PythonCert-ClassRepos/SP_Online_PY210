def fibonacci(n):
	"""Takes input n and returns the fibonacci series to the nth values
	the first 2 values are pre defined in the function"""
	x = []
	for i in range(n+1):
		x.append(i)
	for i in range(n+1):
		if i == 0:
			x[0] = 0
		elif i == 1:
			x[1] = 1
		else:
			x[i] = x[(i-1)] + x[(i-2)]
	return x[n]

def lucas(n):
	"""Takes input n and returns the lucas series to the nth values
	the first 2 values are pre defined in the function"""
	x = []
	for i in range(n+1):
		x.append(i)
	for i in range(n+1):
		if i == 0:
			x[0] = 2
		elif i == 1:
			x[1] = 1
		else:
			x[i] = x[(i-1)] + x[(i-2)]
	return x[n]

def sum_series(n, g=0, h=1):
	"""Takes input n and returns the fibonacci series to the nth values.
	arguments #2 and #3 are optional with default values of 0 and 1 for 
	fibonacci series."""
	x = []
	for i in range(n+1):
		x.append(i)
	for i in range(n+1):
		if i == 0:
			x[0] = g
		elif i == 1:
			x[1] = h
		else:
			x[i] = x[(i-1)] + x[(i-2)]
	return x[n]

if __name__ == "__main__":
    # run some tests for fibonacci and lucas
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)
    assert sum_series(0) == fibonacci(0)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)
    assert sum_series(0, 2, 1) == lucas(0)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 5, 2) == 2
    assert sum_series(2, 5, 4) == 9
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")