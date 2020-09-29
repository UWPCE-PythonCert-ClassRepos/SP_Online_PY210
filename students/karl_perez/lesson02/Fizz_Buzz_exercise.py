#FizzBuzz exercise 2.3

"""Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead."""

for a in range(0,101):
    if a % 3 == 0 and a % 5 == 0:
	    print("FizzBuzz")
    elif a % 3 == 0:
	    print("Fizz")
    elif a % 5 == 0:
	    print("Buzz")
    else:
        print(a)

