#!/usr/bin/env python3

"""
Lesson 2: The Classic Fizz Buzz Problem
Course: UW PY210
Author: Jason Jenkins
"""


def print_Fizz_Buzz():
    """
    Prints the numbers from 1 to 100 inclusive.
    For multiples of three print “Fizz” instead.
    For multiples of five print “Buzz” instead.
    For multiples of both three and five print “FizzBuzz” instead.
    """

    for x in range(100):
        tmpNum = x + 1
        if(tmpNum % 3 == 0 and tmpNum % 5 == 0):
            print("FizzBuzz")
        elif(tmpNum % 3 == 0):
            print("Fizz")
        elif(tmpNum % 5 == 0):
            print("Buzz")
        else:
            print(tmpNum)


if __name__ == "__main__":
    # tests print_Fizz_Buzz
    print_Fizz_Buzz()
