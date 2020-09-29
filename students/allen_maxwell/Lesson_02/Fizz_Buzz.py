# Allen Maxwell
# Python 210
# 10/27/2019
# 
# Fizz_Buzz.py
"""
* Write a program that prints the numbers from 1 to 100 inclusive.
* But for multiples of three print “Fizz” instead of the number.
* For the multiples of five print “Buzz” instead of the number.
* For numbers which are multiples of both three and five print “FizzBuzz” instead.
"""
def fizz_buzz():
    for i in range(1,101):
        result=''
        if i%3 == 0:
            result = 'Fizz'
        if i%5 == 0:
            result += 'Buzz'
        else: 
            result = i
        print(result)
