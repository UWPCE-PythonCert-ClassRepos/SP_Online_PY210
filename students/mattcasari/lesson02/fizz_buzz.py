#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 2, Excercise 2

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/fizz_buzz.html

* Write a program that prints the numbers from 1 to 100 inclusive.
* But for multiples of three print “Fizz” instead of the number.
* For the multiples of five print “Buzz” instead of the number.
* For numbers which are multiples of both three and five print “FizzBuzz” instead.

"""

def fizz_buzz():
    """ Print the Fizz Buzz output

    For the range of 1 to 100, prints "Fizz" for multiples of 3, "Buzz" for
    multiples of 5, and the index for all others.

    Args: 
        None

    Returns:
        None
    """
        
    for i in range(1, 101):
        if i % 3 != 0 and i % 5 != 0:
            print(i, end="")
        else:
            if i % 3 == 0:
                print("Fizz", end="")
            if i % 5 == 0:
                print("Buzz", end="")
        print("")
        
if __name__ == "__main__":
    fizz_buzz()