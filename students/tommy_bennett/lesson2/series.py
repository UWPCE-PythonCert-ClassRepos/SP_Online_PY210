def fibonacci(n):
    """Calculate the fibonacci series"""
    if n <= 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def lucas(n):
    """Calculate the lucas numbers series"""
    if n <= 0:
        return 2
    elif  n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)

