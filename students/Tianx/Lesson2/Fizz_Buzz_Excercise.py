# ------------------------------------------#
# Title: Fizz_Buzz_Excercise.py
# Desc: Fizz Buzz is a classic simple problem in computer science..
# Tian Xie, 2020-04-04, Created File
# ------------------------------------------#

def fizzbuzz():
    number = 0
    for number in range(1,101):
        number != 1
        if number %3 ==0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0 and number % 5 != 0:
            print("Fizz")
        elif number % 5 == 0 and number % 3 != 0:
            print('Buzz')
        else:
            print(number)

if (__name__ == '__main__'):
    fizzbuzz()