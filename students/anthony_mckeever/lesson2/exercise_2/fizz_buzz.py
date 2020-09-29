"""
Programming In Python - Lesson 2 Exercise 2: Fizz Buzz
Code Poet: Anthony McKeever
Start Date: 07/23/2019
End Date: 07/23/2019
"""

def fizz_buzz(endRange = 100):
    """
    Print integers to the console from 1 to endRange.  If the integer is
    a multiple of 3 print "Fizz" instead, if multiple of 5 print "Buzz"
    instead.

    :param endRange:    The inclusive max number of Fizzes to Buzz.  (Default = 100)
    """
    # Range uses inclusive start and exclusive end.  To ensure we're inclusive to the caller add 1 to the endRange value.
    for i in range(1, endRange + 1):
        multiple5 = i % 5 == 0
        multiple3 = i % 3 == 0

        if multiple3 and multiple5:
            print("FizzBuzz")
        elif multiple3:
            print("Fizz")
        elif multiple5:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizz_buzz()
