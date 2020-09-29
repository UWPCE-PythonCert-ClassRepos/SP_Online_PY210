#! python

#-------------------------------------------------------------------
# Lesson 2 - Fizz Buzz Exercise
#
# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print
# “FizzBuzz” instead.
#-------------------------------------------------------------------

for i in range(1, 101):
    w = ""
    if i % 3 == 0:
      w = "Fizz"
    if i % 5 == 0:
      w = w + "Buzz"
    if len(w) > 0:
      print(w)
    else:
      print(i)
