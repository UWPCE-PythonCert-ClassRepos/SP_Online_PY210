"""
grid_printer.py
Zachary Meves
Python 210
Lesson 02

Module for grid printing functions.
"""


def _row(n, post='+', cell='-'):
    """For internal use only.

    Returns row with ``n`` columns and the given post/cell characters."""

    return post + cell * ((n - 1) // 2) + post + cell * (n // 2) + post + '\n'


def print_grid(x):
    """Print a grid of the specified size. The size is specified as
    the side length of a square grid.

    Parameters
    ----------
    x : int
        Side length of grid"""

    _str_ = _row(x, '+', '-')
    for i in range((x - 1) // 2):  # Iterate over top half of grid
        _str_ += _row(x, '|', ' ')
    _str_ += _row(x, '+', '-')
    for i in range((x - 1) // 2, x - 1):  # Iterate over bottom half of grid
        _str_ += _row(x, '|', ' ')
    _str_ += _row(x, '+', '-')
    print(_str_)


def _row2(n, c, post='+', cell='-'):
    """For internal use only.

    Returns row with ``n`` columns of size ``c`` each
    and the given post/cell characters."""

    return post + n * (cell * c + post) + '\n'


def print_grid2(x, y):
    """Print a grid of the specified size. The size is specified as the
    side length and cell size.

    Parameters
    ----------
    x : int
        Number of rows and columns
    y : int
        Side length of each cell"""

    _str_ = _row2(x, y, '+', '-')
    for ir in range(x):  # Iterate over rows
        for ic in range(y):  # Iterate over cell interior
            _str_ += _row2(x, y, '|', ' ')
        _str_ += _row2(x, y, '+', '-')  # Close the cell
    print(_str_)


if __name__ == "__main__":
    """Test grid printers."""

    # Test print_grid
    for x in [3, 4, 5, 9, 12, 15]:
        print('print_grid({})'.format(x))
        print_grid(x)
        print('')

    # Test print_grid2
    for x, y in zip([3, 5, 4], [5, 3, 4]):
        print('print_grid2({}, {})'.format(x, y))
        print_grid2(x, y)
        print('')
