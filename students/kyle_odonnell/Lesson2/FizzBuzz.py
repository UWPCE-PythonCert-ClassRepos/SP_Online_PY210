# ------------------------------------------------------------------------ #
# Title: Fizz Buzz Exercise
# Description: Introduction to Python: Lesson 2 Exercise 2.3
# ChangeLog:
# KODonnell,10.17.2020,Created script
# ------------------------------------------------------------------------- #


def fizzbuzz():
 for x in range(1,101):
     if x%3==0 and x%5==0:
         print("FizzBuzz")
     elif x%3==0:
         print("Fizz")
     elif x%5==0:
         print("Buzz")
     else:
         print(x)

fizzbuzz()