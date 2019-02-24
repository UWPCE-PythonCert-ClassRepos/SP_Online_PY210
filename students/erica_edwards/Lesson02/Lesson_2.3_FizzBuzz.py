

for number in range(1, 1):
    if number % 3 == 0 and number % 5 == 0:
        print('Fizz Buzz')
        continue
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
