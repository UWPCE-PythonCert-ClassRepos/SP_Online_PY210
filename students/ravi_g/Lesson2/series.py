# Fibonacci series

def fibonacci(n):
    '''
    :param n: int
    :return: int
    '''
    count, nth, n1, n2 = 2, 0, 0, 1
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        while count < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return nth

# Lucas series
def lucas(n):
    '''
    :param n: int
    :return: int
    '''
    count, nth, n1, n2 = 2, 0, 2, 1
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        while count < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return nth

# generic series
def generic(n, n1 = 0, n2 = 1):
    '''
    :param n: int
    :param n1: int
    :param n2: int
    :return: int
    '''
    count, nth = 2, 0
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        while count < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return nth

if __name__ == '__main__':
    # enter the number of terms for Fibonacci series or Lucas series

    while 1:
        num_terms = int(input("Enter number of terms: "))
        if num_terms > 0:
            break
        else:
            print('Enter a positive number: ')
    # fibonacci series
    print("Fibonacci {0}th number: ".format(num_terms), fibonacci(num_terms))
    # lucas series
    print("Lucas {0}th number: ".format(num_terms), lucas(num_terms))
    # generic series - Fibonacci
    print("Fibonacci series using generic function; {0}th term is".format(num_terms), generic(num_terms))
    # generic series - Lucas
    print("Lucas series using generic function; {0}th term is".format(num_terms), generic(num_terms, 2, 1))
    # generic series - non-Fibonacci, non-Lucas
    print("Non-Fibonacci, non-Lucas series using generic function; {0}th term is".format(num_terms), generic(num_terms, 3, 4))
