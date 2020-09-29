# fizzbuzz.py - Exercise 2.3



x = 1
while x < 101:
    three = x%3
    five = x%5
    if three == 0 and five == 0:
        print('FizzBuzz')
    elif three == 0:
        print('Fizz')
    elif five == 0:
        print('Buzz')
    else:
        print(x)
    x = x + 1



