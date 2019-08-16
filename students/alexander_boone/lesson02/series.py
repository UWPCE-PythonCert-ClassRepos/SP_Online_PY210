def fibonacci(n):
    """Return nth integer in the Fibonacci series starting from index 0."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """Return nth integer in the Lucas series starting from index 0."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)