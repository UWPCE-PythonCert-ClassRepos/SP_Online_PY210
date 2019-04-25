
def fizz_buzz_1(fizz_until=100):
    """Prints fizzBuzz from 1 through user-input integer"""
    for i in range(1, fizz_until+1):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def fizz_buzz_2(fizz_until=100):
    """Also prints fizzbuzzes. I wanted to use more functions"""
    def is_fizz(i):
        """Returns true if an int parameter is divisible by 3"""
        if i % 3 == 0:
            return True

    def is_buzz(i):
        """Returns true if an int parameter is divisible by 5"""
        if i % 5 == 0:
            return True

    def is_fizz_buzz(i):
        """Returns true if an int parameter is divible by 3 and 5"""
        if i % 3 == 0 and i % 5 == 0:
            return True
    for i in range(1, fizz_until + 1):
        if is_fizz_buzz(i):
            print('FizzBuzz')
        elif is_fizz(i):
            print('Fizz')
        elif is_buzz(i):
            print('Buzz')
        else:
            print(i)
