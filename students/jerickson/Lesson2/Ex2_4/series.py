# TODO turn to zero index
def fibonacci(n):
    """Return n-th value of fib series"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n = fibonacci(n - 1) + fibonacci(n - 2)
    return n


def lucas(n):
    """Return n-th value of lucas series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        n = lucas(n - 1) + lucas(n - 2)
    return n


def sum_series(n, zeroth=0, first=1):
    """Return n-th value of a sum-series of fibonacci structure
    
    zeroth/first are the intial 2 values of the sum-series.
    """
    if n == 0:
        return zeroth
    elif n == 1:
        return first
    else:
        n = sum_series(n - 1, zeroth=zeroth, first=first) + sum_series(
            n - 2, zeroth=zeroth, first=first
        )
    return n


if __name__ == "__main__":
    print("fib")
    for i in range(0, 10):
        n = fibonacci(i)
        print(f"{n}, ", end="")

    print("\nlucas")
    for i in range(0, 10):
        n = lucas(i)
        print(f"{n}, ", end="")

    print("\ngeneral")
    for i in range(0, 10):
        n = sum_series(i, 0, 1)
        print(f"{n}, ", end="")
