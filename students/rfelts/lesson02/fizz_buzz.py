# Russell Felts
# Assignment 2 - Fizz Buzz
# Write a program that prints the numbers from 1 to 100 inclusive.
# For multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.

def fizz_buzz():
    """Print 1-100, print "fizz buzz" for x3&5 "fizz" for x3 and "buzz" for x5"""
    for loop in range(1,101):
        if(loop % 3 == 0 and loop % 5 == 0):
            print("fizz buzz")
        elif(loop % 3 == 0):
            print("fizz")
        elif(loop % 5 == 0):
            print("buzz")
        else:
            print(loop)

fizz_buzz()
