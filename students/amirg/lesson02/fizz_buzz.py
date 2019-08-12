
i = 1
while i < 101:
    x = i % 15
    y = i % 5
    z = i % 3
    if x == 0:
        print('FizzBuzz')
    elif y == 0:
        print('Buzz')
    elif z == 0:
        print('Fizz')
    else:
        print(i)
    i += 1