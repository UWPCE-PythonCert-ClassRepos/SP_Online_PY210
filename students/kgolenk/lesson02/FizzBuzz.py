# ---------------------------------------------------------------------------- #
# Title: Lesson 02
# Description: A function that prints numbers and strings
# ChangeLog (Who,When,What):
# Kate Golenkova, 10/08/2020, Created script
# ---------------------------------------------------------------------------- #

# Data ----------------------------------------------------------------------- #
# Declare variables
a = "Fizz"
b = "Buzz"
c = "FizzBuzz"

# Functions ------------------------------------------------------------------ #
def fizz_buzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print(c)
        elif i % 5 == 0:
            print(b)
        elif i % 3 == 0:
            print(a)
        else:
            print(i)

fizz_buzz()
