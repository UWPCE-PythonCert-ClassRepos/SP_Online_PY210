# Module for Fibonacci series and Lucas numbers

def fibonacci(n):
    """ Return the nth number in the Fibonacci series (starting from zero index)

    Parameters:

    n : integer
        Number in the Fibonacci series to compute

    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """ Return the nth Lucas number (starting from zero index)

    Parameters:

    n : integer
        Lucas number to compute

    """
    # Base cases
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

if __name__ == "__main__":
    # Run tests on fibonacci function
    print('Printing the first 10 numbers in the fibonacci series')
    for n in range(10):
        print(fibonacci(n))
    # Run tests on Lucas numbers
    print('Printing the first 10 Lucas numbers')
    for n in range(10):
        print(lucas(n))
