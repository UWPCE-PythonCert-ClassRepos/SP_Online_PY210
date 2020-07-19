# Lesson 1: Computing the Fibonacci and Lucas Series
# Course: UW PY210
# Author: Jason Jenkins


def print_Fizz_Buzz():
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
