
def fizzBuzz1(fizzUntil=100):
    """Prints fizzBuzz from 1 through user-input integer"""
    for i in range(1,fizzUntil+1):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else: 
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def fizzBuzz2(fizzUntil=100):
    """Also prints fizzbuzzes. I wanted to use more functions"""
    def isFizz(i):
        """Returns true if an int parameter is divisible by 3"""
        if i % 3 == 0:
            return True
    def isBuzz(i):
        """Returns true if an int parameter is divisible by 5"""
        if i % 5 == 0:
            return True
    def isFizzBuzz(i):
        """Returns true if an int parameter is divible by 3 and 5"""
        if i % 3 == 0 and i % 5 == 0:
            return True
    for i in range(1, fizzUntil + 1):
        if isFizzBuzz(i):
            print('FizzBuzz')
        elif isFizz(i):
            print('Fizz')
        elif isBuzz(i):
            print('Buzz')
        else:
            print(i)
        