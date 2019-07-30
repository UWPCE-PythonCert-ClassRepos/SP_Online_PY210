def print_grid(scalar):

    """
    Print a grid sized on the scalar parameters

    :param scalar: Row size made of squares
    :type scalar: int

    """

    grid_size = int(scalar / 2)

    # The outer loop to print both row pattern types
    for plus_row in range(3):
        if plus_row > 0:
            # Print the vertical bar rows
            for bar_row in range(grid_size):
                print('|', end=' ')
                for bar_col in range(2):
                    print ((scalar - 1) * ' ', end = '| ')
                print()

        # Print out the row with plus symbols
        print('+', end= ' ')
        for plus_col in range(2):
            print(grid_size * '- ', end = '+ ')

        print()


if __name__=='__main__':
    print_grid(3)
    print_grid(15)