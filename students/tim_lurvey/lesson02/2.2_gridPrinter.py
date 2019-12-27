#!/usr/bin/env python
__author__ = 'Tim Lurvey'


def grid_gen(cellSize: int, count: int = 2) -> str:
    """Build a [count]x[count] print array with borders where [cellSize] is the
    total size between cell borders.

    :param cellSize:    size of individual cell
    :type cellSize:     integer
    :param count:       number of cells to create
    :type count:        integer
    :return:            string of printable grid_gen from params"""
    try:
        assert (isinstance(cellSize, int))
    except AssertionError:
        raise TypeError("cellSize must be an integer")
    #
    try:
        assert (isinstance(count, int))
    except AssertionError:
        raise TypeError("count must be an integer")
    #
    # empty grid_gen string
    grid = ''
    # define horizontal spacing of each cell's two line types
    cell1 = '+' + (' -' * cellSize) + ' +'
    cell2 = '|' + ('  ' * cellSize) + ' |'
    # combine the cell text chunks into a full line
    line1 = cell1 + (cell1[1:] * (count - 1)) + '\n'
    line2 = cell2 + (cell2[1:] * (count - 1)) + '\n'
    # build grid_gen vertically
    for x in range(count):  # building first 2 array/grid_gen spaces
        grid += line1  # add the top border line
        for y in range(cellSize):  # build the lines for single array/grid_gen space
            grid += line2  # add appropriate number of lines
    grid += line1  # add the bottom border of the array/grid_gen
    return grid


def print_grid(n: int) -> None:
    """print a 2x2 array of cell size n"""
    print("Size = {0}\nCount = {1}x{1}".format(n, 2))
    print(grid_gen(cellSize=n, count=2))


def print_grid2(i: int, n: int) -> None:
    """print an ixi array of cell size n"""
    print("Size = {0}\nCount = {1}x{1}".format(n, i))
    print(grid_gen(cellSize=n, count=i))


def grip_print_tests():
    """execute a series of grid_gen print testing"""
    print('\nPart1\n')
    print_grid(3)
    print('\nPart2\n')
    print_grid(1)
    print_grid(3)
    print_grid(6)
    print_grid(9)
    print('\nPart3\n')
    print_grid2(5, 3)


if __name__ == '__main__':
    grip_print_tests()
