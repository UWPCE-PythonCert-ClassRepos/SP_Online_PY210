'''
Print the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.
'''

for i in range(1,101):
    #Determine if the number is divisible by 3 or 5
    line = ''
    if i % 3 == 0:
        line += 'Fizz'
    if i % 5 == 0:
        line += 'Buzz'
    #Based on result of test either print line or the number
    if line:
        print(line)
    else:
        print(i)