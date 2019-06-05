number = 1

while number < 101:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        number += 1
    elif number % 3 == 0:
        print("Fizz")
        number += 1
    elif number % 5 == 0:
        print("Buzz")
        number += 1
    else:
        print(number)
        number += 1