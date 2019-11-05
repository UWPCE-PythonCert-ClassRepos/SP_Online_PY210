#!/usr/bin/env python

"""Fibonacci Series Exercise

fibonacci(n) produces the Fibonacci series out to nth value.

lucas(n) produces the Lucas series out to nth value.

sum_series(n,b,c) produces the sum-series out to nth value.  Default is b=0 and
 c=1 to produce the Fibonacci series to nth value.
"""

print("""I had to write this without an internet connection on another machine,
 so rather than commits with messages to describe my thoughts and activities, I
included a log of my copied thoughts/activities as comments.
""")

def sum_series(n,b=0,c=1): #date: 28OCT19 time: 1738EST.  Idea is to produce
#something most general first, then have the specific functions call the
#general function with certain parameters
    """
    This is the general sequence forming function.

    Both fibonaci() and lucas() call this function.

    produces the sum series out to nth value
    """
    series=[b,c]
    newval=0
    for i in range(2,n+1):
        newval=series[i-1]+series[i-2]
        series.insert(i,newval)
    return series[n] #1741 now most general case has been attained and tested

def fibonacci(n): #1742 now will develop a fibonacci function that calls
#sum_series with certain parameters.
    """
    This is the specific case of the Fibonacci series.

    calls sum_series() with 0,1 as the starting values

    produces series to nth value
    """
    b=0
    c=1
    return sum_series(n,b,c) #1743 fibonacci() confirmed

def lucas(n): #1744 now will develop a lucas function that calls sum_series
#with a certain set of parameters.
    """
    This is the specific case of the Lucas series.

    calls sum_series() with 2,1 as the starting values

    produces series to nth value
    """
    b=2
    c=1
    return sum_series(n,b,c) #1745 lucas confirmed

#1746 now must add docstrings

#1750 docstrings added and more command line testing completed.  Now must
#research ASSERT statements...

if __name__ == "__main__":  #29OCT19 2300: had to adjust the functions to
                            #return the nth value in the series rather than
                            #print the series up to and including the nth value
    # run some tests
    assert fibonacci(0) == 0#these confirm that the first 8 fibonacci terms
    assert fibonacci(1) == 1#match
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2#these confirm that the first two and fifth lucas terms
    assert lucas(1) == 1#match

    assert lucas(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")

