# TODO turn to zero index
def fibonacci(n):
    """Return n-th value of fib series"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        n = fibonacci(n - 1) + fibonacci(n - 2)
    print(f"{n} ", end=" ")
    return n


def lucas(n):
    """Return n-th value of lucas series"""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        n = lucas(n - 1) + lucas(n - 2)
    print(f"{n} ", end=" ")
    return n


if __name__ == "__main__":
    print("fib")
    for i in range(1, 10):
        n = fibonacci(i)
        print(f"{i}:{n}")

    print("\nlucas")
    for i in range(1, 10):
        n = lucas(i)
        print(f"{i}:{n}")
