#!/usr/bin/env python3

"""
a template for the series assignment
#updated with finished code 7/29/2019 T.S.
"""

def fibonacci(n):
    series = [0,1] #Define the base series values in a list
    while len(series) < n + 1: #add one so normalize lenth and index number
        series.append(sum(series[-2:])) #Add last two variables and append to list
    return series[n] #return the nth value


def lucas(n):
    series = [2,1] #Define the base series values in a list
    while len(series) < n + 1: #add one so normalize lenth and index number
        series.append(sum(series[-2:])) #Add the variables and append on to the list
    return series[n] #return the nth value

def sum_series(n, n0=0, n1=1): #default values are for fibonacci sequence
    series = [n0, n1] #Define the base series values in a list
    while len(series) < n + 1: #add one so normalize lenth and index number
        series.append(sum(series[-2:])) #Add the variables and append on to the list
    return series[n] #return the nth value


if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

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

