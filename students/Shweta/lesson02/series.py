#!/usr/bin/env python3

""" a code to print Finonacci and Lucas series """

def fibonacci(n):
    """ returns the nth Fibonaci number , where
    n is the argument passed to this function"""
    m=0
    if (n<0):
        print("incorrect number")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        m=fibonacci(n-1)+fibonacci(n-2)
        return m

def lucas(n):
    """  returns the nth Lucas number, where
    n is the argument passed to this function"""
    l=0
    if (n<0):
        print("Incorrect value")
    elif n==0:
        return 2
    elif n==1:
        return 1
    else:
        l=lucas(n-1)+lucas(n-2)
        return l


def sum_series(a,b=0,c=1):
    if b==0 and c==1:
        return fibonacci(a)
    elif b==2 and c==1:
        return lucas(a)
    else:
        d=0
        for i in range(a):
            d=a**2
        return d

#print(sum_series(2,3,2))
if __name__=="__main__":
    #running test for the three functions
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21

    assert lucas(0) == 2
    assert lucas(3) == 4
    assert lucas(4) == 7

    # testing sum_series matching fibonacci function values
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7,0,1) == fibonacci(7)
    assert sum_series(5,2,1) == lucas(5)

    assert sum_series(3,3,2) == 9
    assert sum_series(5,3,2) == 25
