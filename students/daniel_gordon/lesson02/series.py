def fibonacci(n):
    """Calculates the nth value of the fibonacci sequence"""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
    """Calculates the nth lucas number"""
    if n == 1 or n == 2:
        return n
    return lucas(n-2) + lucas(n-1)
