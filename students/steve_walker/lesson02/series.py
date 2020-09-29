def fibonacci(n):
	"""Return the nth term of the Fibonacci sequence"""
	fib_seq = []
	nth_term = 0
	
	for i in range(0,n+1):
		if i == 0:
			fib_seq.append(0)
		if i == 1:
			fib_seq.append(1)
		if i > 1:
			nth_term = fib_seq[-1] + fib_seq[-2]
			fib_seq.append(nth_term)
	
	print(fib_seq)
	print(fib_seq[n])
	return(fib_seq[n])

fibonacci(5)


def lucas(n):
	"""Return the nth term of the Lucas Numbers"""
	lucas_seq = []

	for i in range(0,n+1):
		if i == 0:
			lucas_seq.append(2)
		if i == 1:
			lucas_seq.append(1)
		if i > 1:
			nth_term = lucas_seq[-1] + lucas_seq[-2]
			lucas_seq.append(nth_term)
	
	print(lucas_seq)
	print(lucas_seq[n])
	return(lucas_seq[n])

lucas(5)


def sum_series(n, a=0, b=1):
	"""Return the nth term of a sequence s where n = s(n-1) + s(n-2)"""
	seq = []
	nth_term = 0
	
	for i in range(0,n+1):
		if i == 0:
			seq.append(a)
		if i == 1:
			seq.append(b)
		if i > 1:
			nth_term = seq[-1] + seq[-2]
			seq.append(nth_term)
	
	print(seq)
	print(seq[n])
	return(seq[n])

sum_series(0, 3, 2)


if __name__ == "__main__":
    # test select fibonacci and lucas outputs
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # test that sum_series matches fibonacci
    assert sum_series(77) == fibonacci(77)
    assert sum_series(7, b=1, a=0) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed. clear skies ahead.")
