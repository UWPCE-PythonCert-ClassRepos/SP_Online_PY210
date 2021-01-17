#!/usr/bin/env python

# ---------------------------------------------------------------------------- #
# Title: Lesson 2
# Description: Exercise 2.2 - Fizz Buzz
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-02-2020, Created Fizz Buzz Function
# ---------------------------------------------------------------------------- #

def fizz_buzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':

    fizz_buzz()
