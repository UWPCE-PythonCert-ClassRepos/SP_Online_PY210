#!/usr/bin/env python3

def fibonacci(n):
    """ compute the nth Fibonacci number """
    if n<0:
        return None
    elif 0<=n<=1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
    """ compute the nth Lucas number """
    if n<0:
        return None
    elif n==0:
        return 2
    elif n==1:
        return 1
    else:
        return(lucas(n-1) + lucas(n-2))


#test print for some n values
print("Fibonacci(5): computing 5th Fibonacci number...\n")
print(fibonacci(5))
print()

print("Lucas(5): computing 5th Lucas number...\n")
print(lucas(5))
print()


if __name__ == "__main__":
    # Fibonacci(n) asserts
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    # Lucas(n) asserts
    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    print("tests passed")