def print_grid2(squares, scalar):
    """
    Print a grid sized on the squares and scalar paramaters

    :param squares: Row size based on number of squares
    :type squares: int
    :param scalar: Size of squares
    :type scalar: int

    """
    # The outer loop to print both row pattern types
    for plus_row in range(squares + 1):
        if plus_row > 0:

            # Print the vertical bar rows
            for bar_row in range(scalar):
                print('|', end=' ')
                for bar_col in range(squares):
                    print ((2*scalar) * ' ', end = '| ')
                print()

        # Print out the row with plus symbols
        print('+', end= ' ')
        for plus_col in range(squares):
            print(scalar * '- ', end = '+ ')

        print()


if __name__=='__main__':
    print_grid2(3,4)
    print_grid2(5,3)