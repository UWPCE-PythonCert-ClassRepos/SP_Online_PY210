#!/usr/bin/env python3


def main():
    fizz_buzz()


def fizz_buzz():
    '''
    write a program that prints the numbers from 1 to 100 inclusive
    But for multiples of three print “Fizz” instead of the number
    For the multiples of five print “Buzz” instead of the number
    For numbers which are multiples of both three and five print “FizzBuzz” instead
    '''
    fizz = "Fizz"
    buzz = "Buzz"

    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("%s" % (fizz + buzz))
        elif x % 3 == 0:
            print("%s" % fizz)
        elif x % 5 == 0:
            print("%s" % buzz)
        else:
            print("%s" % x)
    return None


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running %s as imported module", __file__)