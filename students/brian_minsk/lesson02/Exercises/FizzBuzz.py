# To use, invoke on the command line with "python FizzBuzz.py"
# Author: Brian Minsk

def FizzBuzz():
    """Print the numbers from 1 to 100 but for multiples of 3 print "Fizz" instead of the number,
    multiples of 5 print "Buzz" instead of the number, and for multiples of 3 *and* 5 print "FizzBuzz"
    instead of the number.
    """
    for i in range (1, 101):
        print_this = "" 
        if i % 3 == 0:
            print_this = "Fizz"
        if i % 5 == 0:
            print_this += "Buzz" #if a multiple of 3 is found the string will already be "Fizz". If not it will be an empty string. So just concatenate "Buzz"
        if print_this == "": #if the string is still empty then a multiple of 3 or 5 was not found
            print_this = i
        print(print_this)

if __name__ == "__main__":
    FizzBuzz()