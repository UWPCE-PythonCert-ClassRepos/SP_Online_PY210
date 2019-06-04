for number in range(1,101):
    if number % 3 is 0:
        print("Fizz")
    elif number % 5 is 0:
        print("Buzz")
    elif number % 3 is 0 and number % 5 is 0:
        print("FizzBuzz")
    else:
        print(number)
