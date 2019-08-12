def print_grid():

    """
    Print a grid of 4 squares with sides of 4 dashes
     
    """

    # The outer loop to print both row pattern types
    for plus_row in range(3):

        if plus_row > 0:
            # Print the vertical bar rows
            for bar_row in range(3):
                print('|', end=' ')
                for bar_col in range(2):
                    print (8 * ' ', end = '| ')
                print()

        # Print out the row with plus symbols
        print('+', end= ' ')
        for plus_col in range(2):
            print(4 * '- ', end = '+ ')

        print()


if __name__=='__main__':
    print_grid()