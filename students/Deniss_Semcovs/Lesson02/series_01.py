# Fibonacci series
def fibonacci(n):
    """This function will return series of numbers with range(n) 
    through Fibonacci Series starting with the integers 0 and 1."""
    fn = 0
    sn = 1
    nn = 0
    for i in range(n):
        while nn < n:
            print(fn)
            nth = fn+sn
            fn = sn
            sn = nth
            nn += 1
# Lucas series 
def lucas(n):
    """This function will return series of numbers with range(n)
    through Lucas Numbers starting with 2 and 1."""
    fn = 2
    sn = 1
    nn = 0
    for i in range(n):
        while nn < n:
            print(fn)
            nth = fn+sn
            fn = sn
            sn = nth
            nn += 1
# Sum Series
def sum_series(n, n0=0, n1=1):
    """This function will return series of numbers with range(n)
    using optional numbers n0 and n1, by default n0 = 0 and n1 = 1."""
    fn = n0
    sn = n1
    nn = 0
    for i in range(n):
        while nn < n:
            print(fn)
            nth = fn+sn
            fn = sn
            sn = nth
            nn += 1
