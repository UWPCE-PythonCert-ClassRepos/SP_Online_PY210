def sum_series(n, x=0, y=1):
	""""
	Return a value of the nth position of a summation series
	:param x = 0: optional parameter of the value of zeroth element in the series
	:param y = 1: optional parameter of the value of first element in the series
	"""
	z = 0
	if (n == 0):
		z = x
		return z
	if (n == 1):
		z = y
		return z
	for i in range(2,n+1):
		z = x + y
		x = y
		y = z
	return z
def fibonacci(n):
	""""
	Return a value of the nth position of a fibonacci series
	"""
	z = sum_series(n,0,1)
	return z
def lucas(n):
	""""
	Return a value of the nth position of a lucas series
	"""
	z = sum_series(n,2,1)
	return z

if __name__ == "__main__":
    # run some tests
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

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

print("tests passed")
