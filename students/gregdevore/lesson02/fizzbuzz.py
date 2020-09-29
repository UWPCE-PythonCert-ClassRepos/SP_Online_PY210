# Print numbers from 1 to 100 (inclusive)
#   For multiples of 3, print Fizz
#   For multiples of 5, print Buzz
#   For multiples of 3 and 5, print FizzBuzz

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0: # Check for multiples of 3 and 5 first
        print('FizzBuzz')
    elif i % 3 == 0: # Multiples of 3
        print('Fizz')
    elif i % 5 == 0: # Multiples of 5
        print('Buzz')
    else: # Any other number
        print('%i' % i)
