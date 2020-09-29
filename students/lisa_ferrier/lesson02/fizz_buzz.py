# fizz_buzz.py
# Lisa Ferrier, Python 201, Lesson 02
'''prints numbers from 1 to 100 inclusive
    multiples of three print "Fizz"
    multiples of five print "Buzz"
    numbers that are multiples of three and five print "FizzBuzz" instead.'''

for i in range(1,101):
    if i % 3==0 and i % 5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)