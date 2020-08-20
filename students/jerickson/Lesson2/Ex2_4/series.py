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


if __name__ == "__main__":
    for i in range(1, 10):
        n = fibonacci(i)
        print(f"{i}:{n}")
