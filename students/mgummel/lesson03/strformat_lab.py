#! /usr/bin/env python3

# Task One
def task_one(a_tuple):
    """
    Prints a statements with string formatting of elements
    from a tuple.
    :param a_tuple: a tuple whose elements will be printed
    :type a_tuple: tuple
    """

    print("file_{:03d} :    {:.2f}, {:.2e}, {:.2e}".format(*a_tuple))

    # Task Two
    print(f"file_{a_tuple[0]:03d} :    {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.2e}")

# Task Three

def formatter(in_tuple):
    """
    Prints a statement containing all elements of a tuple
    :param in_tuple: a tuple whose elements will be printed
    :type in_tuple: tuple
    """
    length = len(in_tuple)
    numbers = ", ".join(["{}"] * length).format(*in_tuple)
    print("The {} numbers are: {}".format(length, numbers))

# Task Four

def scramble(tuple_of_numbers):
    """
    Prints a tuple of numbers in a scrambled  way.
    :param tuple_of_numbers: a tuple whose elements will be printed
    :type tuple_of_numbers: tuple
    """
    print("{3:02d} {4:02d} {2:02d} {0:02d} {1:02d}".format(*tuple_of_numbers))

#Task Five

def fruit_weight(weights):
    """
    Prints f-statements with the weight of a fruit. The first statement will
    have the fruits lower case and the second will have the weights multiplied 
    by 1.2 and the fruit names in upper case.
    """
    print(f"The weight of an {weights[0][:-1]} is {weights[1]} and  the weight of a {weights[2][:-1]} is {weights[3]}")
    print(f"The weight of an {weights[0][:-1].upper()} is {weights[1]*1.2} and  the weight of a {weights[2][:-1].upper()} is {weights[3]*1.2}")

#Task Six
def tables():
    """
    Prints a table with containing a name, age, and a cost.
    """
    print('{:20}{:>5}{:>15}'.format('Tiger Woods', 52, '$1000211.22'))
    print('{:20}{:>5}{:>15}'.format('Elizabeth Smith', 123, '$1009.01'))
    print('{:20}{:>5}{:>15}'.format('Frank Lloyd Wright', 3, '$99.01'))
    print('{:20}{:>5}{:>15}'.format('Justin Timberlake', 39, '$199.01'))

def bonus_task(tuple_10):
    """
    Prints a Tuple with 10 consecutive numbers in columns of 5.
    :param tuple_10: a tuple containing 10 consecutive numbers
    :type tuple_10: tuple
    """
    print(" ".join(["{:5}"] * len(tuple_10)).format(*tuple_10))

if __name__ == '__main__':
    # Method calls to print all strings created in the script
    task_one((2, 123.4567, 10000, 12345.67))
    formatter((1, 2, 3, 4, 5, 6))
    scramble((4, 30, 2017, 2, 27))
    fruit_weight(['oranges', 1.3, 'lemons', 1.1])
    tables()
    bonus_task((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
