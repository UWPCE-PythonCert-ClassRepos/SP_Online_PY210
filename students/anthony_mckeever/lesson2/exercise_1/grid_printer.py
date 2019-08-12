"""
Programming In Python - Lesson 2 Exercise 1: Grid Printer
Code Poet: Anthony McKeever
Start Date: 07/22/2019
End Date: 07/23/2019
"""
minus, plus, pipe = '-', '+', '|'

def printer(template, multiple, endChar, times):
    """
    Print the template to the console to form the grid

    :param template:    The Horizontal or Vertical template to print on this call.
    :param multiple:    How many times to repeat the template in the current line.
    :param endChar:     The ending character of the line.
    :param times:       How many times to print the same template in the console
                        on a new line.
    """
    printMe = " ".join((template * multiple) + endChar)
    for i in range(times):
        print(printMe)

def grid_sequencer(dimensions, size):
    """
    Sequence horizontal and vertical templates into the desired grid.

    :param dimensions:  The Dimensions of the grid
    :param size:        The Size of each cell in the grid.
    """
    horizTemp, vertTemp = get_templates(size)

    iterations = (dimensions * 2) + 1
    for i in range(iterations):
        if i % 2 == 0:
            printer(horizTemp, dimensions, plus, 1)
        else:
            printer(vertTemp, dimensions, pipe, size)

def get_templates(n):
    """
    Return the Horizontal and Vertical templates for the desired grid.

    :param n:   The number of times to repeat '-' for the horizontal
                template and ' ' for the vertical template.
    """
    horizontalTemplate = plus + (minus * n)
    verticalTemplate = pipe + (" " * n)
    return horizontalTemplate, verticalTemplate

def print_grid(size):
    """
    Print a 2x2 grid with size/2 x size/2 cells.

    :param size:    The desired height and width of the grid before borders.
    """
    split = int(size / 2)
    grid_sequencer(2, split)

def print_grid2(dimensions, size):
    """
    Print a square dimensions x dimensions grid with size x size cells.

    :param dimensions:  The total dimensions of the grid.  X and Y will use
                        the same value.
    :param size:        The size of each cell in the grid.
    """
    grid_sequencer(dimensions, size)
