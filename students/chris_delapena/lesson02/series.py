"""
Name: Chris Dela Pena
Date: 4/13/20
Class: UW PCE PY210
Assignment: Lesson 2 Exercise 3 "Fibonacci"
File name: series.py
File summary: Defines functions fibonacci, lucas and sum_series
Descripton of functions:
    fibonacci: returns nth number in Fibonacci sequence, where fib(n)=fib(n-1)+fib(n-2), n(0)=0 and n(1)=1
    lucas: returns nth number in Lucas sequence, where luc(n)=luc(n-1)+luc(n-2), n(0)=0 and n(1)=1
    sum_series: similar to fibonacci and lucas, except allows user to input optional values for n(0) and n(1)
"""
def sum_series(n, newPrevious=0, newNext=1): #specify default values for optional args
    result = 0
    previous = newPrevious
    next = newNext
    for i in range(n):
        if i == 0:
            result = previous;
        elif i == 1:
            result = next;
        else:
            result = previous + next;
            previous = next;
            next = result;
    return result #return result, not print result

def fibonacci(n):
    result = 0
    previous = 0
    next = 1
    for i in range(n):
        if i == 0:
            result = previous;
        elif i == 1:
            result = next;
        else:
            result = previous + next;
            previous = next;
            next = result;
    return result #return result, not print result

def lucas(n):
    result = 0
    previous = 2
    next = 1
    for i in range(n):
        if i == 0:
            result = previous;
        elif i == 1:
            result = next;
        else:
            result = previous + next;
            previous = next;
            next = result;
    return result
