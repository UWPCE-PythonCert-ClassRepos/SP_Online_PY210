# Loop thru each number from 1 to 100
for number in range(1, 101):
    # Print "FizzBuzz" for multiples of both three and five
    if (number % 3 == 0) and (number % 5 == 0):
        print('FizzBuzz')
    # Print "Fizz" for multiples of three
    elif number % 3 == 0:
        print('Fizz')
    # Print "Buzz" for multiples of five
    elif number % 5 == 0:
        print('Buzz')
    # Print number otherwise
    else:
        print(number)
    