# ------------------------------------------------------------------------ #
# Title: Fizz Buzz Exercise
# Description: Introduction to Python: Lesson 2 Exercise 2.3
# ChangeLog:
# KODonnell,10.17.2020,Created script
# ------------------------------------------------------------------------- #


def FizzBuzz():
    """
    Print numbers 1-100 inclusive with:
    "FizzBuzz" in place of numbers divisible by 3 and 5,
    "Fizz" in place of numbers divisible by 3, and
    "Buzz" in place of numbers divisible by 5.
    :return: nothing
    """

    for x in range(1,101): # Iterate over numbers in range 1-100
        if x%3==0 and x%5==0: # Print "FizzBuzz" if divisible by 3 and 5
            print("FizzBuzz")
        elif x%3==0: # Print "Fizz" if divisible by 3
            print("Fizz")
        elif x%5==0: # Print "Buzz" if Divisible by 5
            print("Buzz")
        else:
            print(x) # Print integers not divisible by 5 or 3

FizzBuzz()