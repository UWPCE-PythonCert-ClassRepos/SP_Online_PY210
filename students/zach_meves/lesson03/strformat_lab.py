"""
strformat_lab.py

Zach Meves
Python 210
Lesson 03

Exercise : String Formatting
"""


def task_1(tup):
    """Takes a 4-element tuple and returns a string with each element formatted.

    For example, the input::

        ( 2, 123.4567, 10000, 12345.67)

    will produce::

        'file_002 :   123.46, 1.00e+04, 1.23e+04'

    Parameters
    ----------
    tup : tuple
        4-element tuple of numbers

    Returns
    -------
    str
        String formatted as in the example
    """

    return f"file_{int(tup[0]):03d} :   {tup[1]:.2f}, {tup[2]:.2e}, {tup[3]:3.2e}"


def task_2(tup):
    """Takes a 4-element tuple and returns a string with each element formatted. Same as task 1 but
    uses the ``str.format`` method instead of f-strings.

    For example, the input::

        ( 2, 123.4567, 10000, 12345.67)

    will produce::

        'file_002 :   123.46, 1.00e+04, 1.23e+04'

    Parameters
    ----------
    tup : tuple
        4-element tuple of numbers

    Returns
    -------
    str
        String formatted as in the example
        """

    return "file_{:03d} :   {:.2f}, {:.2e}, {:3.2e}".format(int(tup[0]), tup[1], tup[2], tup[3])


def formatter(tup):
    """Takes a tuple of numbers and outputs a string of the form::

        'the n numbers are: num1, num2, ... '

    Parameters
    ----------
    tup : tuple
        Tuple of numbers

    Returns
    -------
    str
        Formatted string"""

    _f_ = '{:d}'
    _fstring_ = (', '.join([_f_ for x in tup])).format(*tup)
    return "The {} numbers are: {}".format(len(tup), _fstring_)


def task_4(tup):
    """Given a 4-element tuple, such as ::

        ( 4, 30, 2017, 2, 27)

    print::

        '02 27 2017 04 30'

    Parameters
    ----------
    tup : tuple
        4-element tuple to rearrange
    """

    print(f'{tup[3]:02d} {tup[-1]:02d} {tup[2]:4d} {tup[0]:02d} {tup[1]:02d}')


def task_5(tup):
    """Given a 4 element list of [name, weight, name, weight], print the names and weights
    of the entries in a formatted string. The names will be upper case, and the weights will be 20% above
    the input weights.

    Parameters
    ----------
    tup : sequence
        Sequence of [name, weight, name, weight] to print"""

    print(f'The weight of an {tup[0][:-1].title()} is {tup[1] * 1.2} and the weight of a {tup[2][:-1].title()} is {tup[-1] * 1.2}')


def task_6():
    """Print a table of several rows, each with a name, age, and cost, to showcase column formatting."""

    items = (('Backpack', 2, 12.78),
             ('Honda Civic', 10, 5200),
             ('Skis', 1, 400),
             ('Pencil', 3, .02))

    print(f'{"Name":<15} | {"Age (YR)":>8} | {"Price ($)":>9}')
    print('-'*(15 + 3 + 8 + 3 + 9))
    for item in items:
        print(f'{item[0]:<15}   {item[1]:>8}   {item[2]:>9.2f}')
    print('-'*(15 + 3 + 8 + 3 + 9))


def task_6_extra(tup):
    """Given a tuple of numbers, print each with a width of 5 characters.

    Parameters
    ----------
    tup : tuple
        Tuple of numbers to print"""

    print((','.join(['{:>5g}' for x in tup])).format(*tup))


if __name__ == '__main__':
    """Complete the 6 tasks for exercise."""

    # Task 1
    print('Task 1:')
    inp = ( 2, 123.4567, 10000, 12345.67)
    print(f'input = {inp}')
    print(f'output = {task_1(inp)}')

    # Task 2
    print('\nTask 2:')
    inp = (2, 123.4567, 10000, 12345.67)
    print(f'input = {inp}')
    print(f'output = {task_2(inp)}')

    # Task 3
    print('\nTask 3:')
    for inp in [(1, 2, 3, 4, 5, 6), (1,), (1, 2, 3)]:
        print(f'input = {inp}')
        print(f'output = {formatter(inp)}')

    # Task 4
    print('\nTask 4:')
    inp = ( 4, 30, 2017, 2, 27)
    print(f'input = {inp}')

    # Task 5
    print('\nTask 5:')
    inp = ['oranges', 1.3, 'lemons', 1.1]
    print(f'input = {inp}')
    task_5(inp)

    # Task 6
    print('\nTask 6:')
    task_6()

    # Extra
    inp = (9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999, 10000, 10001)
    print('\nExtra task (6)')
    print(f'input = {inp}')
    task_6_extra(inp)
    inp = (7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    print(f'input = {inp}')
    task_6_extra(inp)
