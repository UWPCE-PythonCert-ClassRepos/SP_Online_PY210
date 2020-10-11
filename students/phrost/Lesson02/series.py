# Fibonacci series
def fibonacci(n):
    """Calculates the nth position of the Fibonacci sequence """
    seq = [0,1]
    length = len(seq)
    while length < n + 1:
        length = len(seq)
        out = seq[length-1] + seq[length-2]
        seq.append(out)
    return seq[n]

# Fibonacci series
def lucas(n):
    """ Calculates the nth position of the Lucas sequence. code carries over from above with
        the exception of the starting values (2,1 lucas vs 0,1 in fib)"""
    seq = [2,1]
    length = len(seq)
    while length < n + 1:
        length = len(seq)
        out = seq[length-1] + seq[length-2]
        seq.append(out)
    return seq[n]


def sum_series(n, n0=0, n1=1):
    """Produces generalized fibonacci and lucas positions,
       initial fibonacci positions with the default values of 0 and 1,
       produces lucas positions with 2 and 1 used for n0 and n1 respectivley. """

    seq = [n0,n1]
    length = len(seq)
    while length < n + 1:
        length = len(seq)
        out = seq[length-1] + seq[length-2]
        seq.append(out)
    return seq[n]

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
