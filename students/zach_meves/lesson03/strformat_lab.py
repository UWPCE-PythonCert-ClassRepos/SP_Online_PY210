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


if __name__ == '__main__':
    """Complete the 4 tasks for exercise."""

    # Task 1
    print('Task 1:')
    inp = ( 2, 123.4567, 10000, 12345.67)
    print(f'input = {inp}')
    print(f'output = {task_1(inp)}')

    # Task 2
    print('\nTask 2:')
    # todo
