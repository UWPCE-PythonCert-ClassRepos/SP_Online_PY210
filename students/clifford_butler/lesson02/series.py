def fibonacci(n):
    """Computes the fibonacci series starting with zero"""
    nth = 0
    b = 1
    for i in range(0, n):
        print(nth)
        
        a = nth
        nth = b
        b = a + b
    return nth
        
fibonacci(25)


