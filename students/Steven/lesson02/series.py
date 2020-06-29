#! bin/user/env python3
'''
Creating a Fibonacci Series that starts with integers 0 and 1.
The next integer is determined by summming the previous two.
'''

# Parameter n returns the value in the Fibonacci series
def fibonacci(n):
    x = 2
    fib_list = [0, 1]  # start of fibonacci series
    if n in (0,1):
        # print(n) #  Used to test function output
        return n
    else:
        while len(fib_list) != (n + 1):  # Using a while loop to keep adding to the list until the nth value
            fib_list.append(fib_list[x-2] + fib_list[x-1])
            x += 1
        # print(fib_list[n])  # Used to check function output
        return fib_list[n]

# Parameter n returns the value in the Lucas series
def lucas(n):
    x = 2
    luc_list = [2, 1]  # start of lucas series
    if n in (0,1):
        # print(luc_list[n])
        return luc_list[n]
    else:
        while len(luc_list) != (n + 1):  # Using a while loop to keep adding to the list until the nth value
            luc_list.append(luc_list[x - 2] + luc_list[x - 1])
            x += 1
        # print(luc_list[n])
        return luc_list[n]

# First is the zeroth element and second is the first element in series
def sum_series(n, param1 = 0, param2 = 1):
    counter = 2
    sum_list = [param1, param2]
    if param1 == 0 and param2 == 1:
        # print(fibonacci(n))  # Used to check function output
        return fibonacci(n)
    elif param1 == 2 and param2 == 1:
        # print(lucas(n))  # Used to check function output
        return lucas(n)
    else:
        if n == 0:
            # print(param1)
            return param1
        elif n == 1:
            # print(param2)
            return param2
        else:
            while len(sum_list) != (n + 1):  # Using a while loop to keep adding to the list until the nth value
                sum_list.append(sum_list[counter - 2] + sum_list[counter - 1])
                counter += 1
            # print(sum_list[n])  # Used to check function output
            return sum_list[n]


if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")