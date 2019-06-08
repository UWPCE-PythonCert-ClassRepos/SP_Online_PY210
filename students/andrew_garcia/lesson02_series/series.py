def fibonacci(n):
    """ Computes the 'n'th value in the fibonacci sequence, starting with 0 index """

    number = [0, 1]  # numbers to add together

    if n == 0:
        print(number[0])
    elif n == 1:
        print(number[1])
    else:
        for item in range(n - 1):  # subtracts 1 to account for 0 index
            fib = number[0] + number[1]
            number.append(fib)
            number.pop(0)
        print(number[1])


def lucas(n):
    """ Computes the 'n'th value in the lucas sequence, starting with 0 index """

    number = [2, 1]  # numbers to add together

    if n == 0:
        print(number[0])
    elif n == 1:
        print(number[1])
    else:
        for item in range(n - 1):  # subtracts 1 to account for 0 index
            fib = number[0] + number[1]
            number.append(fib)
            number.pop(0)
        print(number[1])


def sum_series(n, zeroth=0, first=1):
    """
    Computes the 'n'th value in a given series

        :param zeroth=0: Creates the first value to use in a series
        :param first=1: Creates the second value to use in a series

    If the two parameters are left blank, or are filled in 0 and 1, it will start the fibonacci sequence
    If the two parameters are filled in 2 and 1, it will start the lucas sequence
    If the two parameters are filled in with two random numbers, it will create its own sequence
    """
    number = [zeroth, first]  # numbers to add together

    if n == 0:
        print(number[0])
    elif n == 1:
        print(number[1])
    else:
        for item in range(n - 1):  # subtracts 1 to account for 0 index
            fib = number[0] + number[1]
            number.append(fib)
            number.pop(0)
        print(number[1])

fibonacci(2)


if __name__ == "__main__":
    assert fibonacci(2) == 1
    print('working')
