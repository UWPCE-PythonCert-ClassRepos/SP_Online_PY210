"""
Purpose: Lessen 2 homework one python certificate from UW
Author: Pirouz Naghavi
Date: 06/26/2020
"""


def create_separating_line(shape, size):
    """Creates separating lines of the grid.

    Args:
      shape: Is a tuple that determines how many cells are present in every
          row or column. Shape tuple follows the convention of (row, column).
      size: Determines how many '-' are present in horizontal separating lines.
          Also, how many '|' are present in vertical separating lines.

    Returns:
        The separating line of the grid as a string. Separating line are identical to first and last line.
    """

    # Separating line's initial value is '+' because  cell always starts +
    separating_line = '+'

    for i in range(shape[1]):
        for j in range(size):
            # Adding ' -' for the specified size to create cell to size
            separating_line += ' -'
        # Adding ' +' to close specified to number of columns. Shape is (row, columns)
        separating_line += ' +'
    return separating_line


def create_middle_line(shape, size):
    """Creates the middle line of the grid.

    Args:
      shape: Is a tuple that determines how many cells are present in every
          row or column. Shape tuple follows the convention of (row, column).
      size: Determines how many '-' are present in horizontal separating lines.
          Also, how many '|' are present in vertical separating lines.

    Returns:
        The middle line of the grid as a string.
    """

    # Middle line's initial value is '|' because  cell always starts | for middle lines
    middle_line = '|'
    for i in range(shape[1]):
        for j in range(size):
            # Adding spaces for the specified size to create cell to size
            middle_line += '  '
        # Adding ' |' to close specified to number of columns. Shape is (row, columns)
        middle_line += ' |'
    return middle_line


def check_input(shape, size):
    """Checks to see if the inputs are correct for the function. If not raises exceptions.

    Args:
      shape: Is a tuple that determines how many cells are present in every
          row or column. Shape tuple follows the convention of (row, column).
      size: Determines how many '-' are present in horizontal separating lines.
          Also, how many '|' are present in vertical separating lines.

    raises:
        ValueError: If size is smaller than zero.
            If length of the argument shape is not equal to 2.
            If argument shape's first value or row is less than one.
            If argument shape's second value or columns is less than one.
        TypeError: Is shape is not a tuple.
    """

    if size < 0:
        raise ValueError('Size is smaller than zero.')
    if not isinstance(shape, tuple):
        raise TypeError('Shape must be a tuple of length 2.')
    if len(shape) != 2:
        raise ValueError('Shape must be a tuple of length only 2.')
    if shape[0] < 1:
        raise ValueError('Grid shape cannot have less than one row.')
    if shape[1] < 1:
        raise ValueError('Grid shape cannot have less than one column.')


def print_grid(shape=(2,2), size=4):
    """Prints a grid based on input arguments

    Args:
      shape: Is a tuple that determines how many cells are present in every
          row or column. Shape tuple follows the convention of (row, column).
      size: Determines how many '-' are present in horizontal separating lines.
          Also, how many '|' are present in vertical separating lines.

    raises:
        ValueError: If size is smaller than zero.
            If length of the argument shape is not equal to 2.
            If argument shape's first value or row is less than one.
            If argument shape's second value or columns is less than one.
        TypeError: Is shape is not a tuple.
    """

    # Checks to see if the inputs are okay otherwise raises appropriate exceptions
    check_input(shape, size)

    # Creates separating lines according input arguments
    separating_line = create_separating_line(shape, size)

    # Creates middle lines according to input arguments
    middle_line = create_middle_line(shape, size)

    # Print first line
    print(separating_line)
    for i in range(shape[0]):
        for j in range(size):
            # Print middle line as many times as the shape dictates
            print(middle_line)
        # Print separating  line as many times as the number rows from shape tuple dictates
        print(separating_line)


if __name__ == '__main__':
    # Printing a test grid
    print_grid(shape=(5,5), size=3)