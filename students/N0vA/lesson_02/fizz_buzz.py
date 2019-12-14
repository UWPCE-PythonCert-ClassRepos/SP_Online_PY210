#### Fizz Buss Exercise #### 

# For numbers 1 to 100 print number or
# - multiplies of 3 print 'Fizz'
# - multiplies of 5 print 'Buzz'
# - multiplies of 3 and 5 print 'FizzBuzz'

def fizz_buzz():
    for i in range(1, 101):
        if i%3 == 0 and i%5 != 0:
            print('Fizz')
        elif i%5 == 0 and i%3 != 0:
            print('Buzz')
        elif i%3 == 0 and i%5 == 0:
            print('FizzBuzz')
        else:
            print(i)

# Run
fizz_buzz()