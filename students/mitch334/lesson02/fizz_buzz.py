# Lesson 02 | Fizz Buzz Exercise
#
# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.

def fizz_buzz():
    for n in range(1,101):
        # print(n)
        if n%3 == 0 and n%5 == 0:
            print('FizzBuzz')
        elif n%3 == 0:
            print('Fizz')
        elif n%5 == 0:
            print('Buzz')
        else:
            print(n)
# fizz_buzz()
