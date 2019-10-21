# This program prints from 1 to 100
# Multiples of 3 prints Fizz
# Multiples of 5 prints Buzz
# Multiples of 15 prints FizzBuzz

def fizz_buzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

fizz_buzz()
