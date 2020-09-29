#the Fibonacci Exercise for lesson2 created by Niels Skvarch

def fibonacci(n):
    """Takes an input to calculate a place in the fibonacci scale and return the numerical value of that place"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-2) + fibonacci(n-1)

#x = int(input("What number in the fibonacci sequence do you seek?: "))
#print(fibonacci(x))


def lucas(n):
    """Takes a user input to calculate a place in the lucas scale and return the numerical value of that place"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return lucas(n-2) + lucas(n-1)

#x = int(input("What number in the lucas sequence do you seek?: "))
#print(lucas(x))

def sum_series(n, n0=0, n1=1):
    """Takes inputs to calculate a number scale based on the fibonacci scale 
    and return the numerical value of the specified place on the scale 
    indicated by the input given"""
    if n == 0:
        return n0
    elif n == 1:
        return n1
    elif n > 1:
        return sum_series(n-2, n0, n1) + sum_series(n-1, n0, n1)

#x = int(input("What number in the sequence do you seek?: "))
#y = 2
#z = 1
#print(sum_series(x, y, z))


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
