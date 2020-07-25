#!/usr/bin/env python3

# Dominic Divakaruni
# SP_Online_PY210
# Lesson 02 - FizzBuzz Exercise


for i in range (1, 101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)