"""
GOAL:
Write a program that prints the numbers from 1 to 100 inclusive
But for multiples of three print 'Fizz' instead of the number
For the multiples of five print 'Buzz' instead of the number.
For numbers which are multiples of both three and five print 'FizzBuzz' instead.
"""
x = 'Fizz'
y = 'Buzz'
z = 'FizzBuzz'



def start_fizz_buzz():
    # Setup start and end counter
    start = 1
    end = 100

    # Start the while loop
    while start <= end:
        # check if disivisable by 3 and 5 and no remainder then print z variable
        if start % 3 == 0 and start % 5 == 0:
            print(z)
        # else check if disivisable by 3 and no remainder then print x variable
        elif start % 3 == 0:
            print(x,)
        # else check if disivisable by 5 and no remainder then print y variable
        elif start % 5 == 0:
            print(y)

        else:
            print(start)

        start = start + 1

start_fizz_buzz()