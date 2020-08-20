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


if __name__ == "__main__":
    print("fib")
    for i in range(0, 10):
        n = fibonacci(i)
        print(f"{i}:{n}")

    print("\nlucas")
    for i in range(0, 10):
        n = lucas(i)
        print(f"{i}:{n}")
