### Python Programming Lesson 02
### Creating Fionacci, Lucas, and Sum series test
### 06/21/19 Jinee Han

# 1. Fionacci Series

''' Create function counting fibonacci
    : starting with 0,1'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


# 2.  Lucas Numbers

''' Create function counting Lucas
    : Starting with 2,1'''

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

# 3. Generalizing

def sum_series(n, n0=0, n1=1):
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-2,n0,n1) +sum_series(n-1,n0,n1)

# 4. Test

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
    assert sum_series(4, 2, 1) == lucas(4)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")