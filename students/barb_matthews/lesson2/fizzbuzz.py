## Lesson 2, Exercise 2, FizzBuzz
## By: B. Matthews
## 9/10/2020
## fizzbuzz() prints numbers from 1 to 100, for multiples of 3 prints "Fizz" instead of number,
## for multiples of 5 prints "Buzz" instead of number, and for multiples of 3 and 5 prints both


def fizzbuzz():

    for i in range(100):

        count = i + 1

        if ((count % 3 == 0) and (count % 5 == 0)):
            print("FizzBuzz")
        elif ((count % 3) == 0):
            print("Fizz")
        elif ((count % 5) == 0):
            print("Buzz")
        else:
            print(count)

fizzbuzz()