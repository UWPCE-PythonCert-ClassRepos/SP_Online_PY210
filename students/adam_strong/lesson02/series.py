'''Fibonacci Series Exercise 2.4

functions:
  fibonacci(n) - Fibonacci sequence (starts with 0,1)
  lucas(n) - Lucas sequence (starts with 2,1)
  sum_series(n,n0,n1) - generalized


'''

def fibonacci(n):
    '''This calculates the nth value in the Fibonacci sequence'''
    seq = [0,1]
    length = len(seq)
    while length < n + 1:
        length = len(seq)
        new = seq[length-1] + seq[length-2]
        seq.append(new)
    return seq[n]


def lucas(n):
    '''This calculates the nth value in the Lucas sequence, only
    difference between this and fibonacci(n) is the starting set'''
    seq = [2,1]
    length = len(seq)
    while length < n + 1:
        length = len(seq)
        new = seq[length-1] + seq[length-2]
        seq.append(new)
    return seq[n]

def sum_series(n, n0=0, n1=1):
    '''This calculates the nth value in a generalized starting set of two
    numbers, defualt n0 and n1 values create the Fibanacci sequence'''
    seq = [n0,n1]
    length = len(seq)
    while length < n + 1:
        length = len(seq)
        new = seq[length-1] + seq[length-2]
        seq.append(new)
    return seq[n]


if __name__ == "__main__":
    # These tests test the accuracy of the fibonacci function
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # These tests test the accuracy of the lucas function
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    # These tests test the accuracy of the sum_series function

    # Compared to fibonacci function
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

   # Compared to the lucas function
    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)
    assert sum_series(8, 2, 1) == lucas(8)

    # Tests the generality of the sum_series function
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")
