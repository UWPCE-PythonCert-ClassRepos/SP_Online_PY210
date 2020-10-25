#Grid Printer Excercise Lesson 2

def print_grid(x,y):
    '''
    Prints grid with x blocks, and y units for each box
    '''
    #get shapes
    plus = '+'
    minus = '-'
    bar = '|'

    #minus sign sequence
    minus_sequence = y * minus
    grid_line = plus + minus_sequence

    #Create bar pattern
    bar_sequence = bar + ' ' * y

    #Print out Grid
    for i in range(x):
        print(grid_line * x, end = plus)

        for i in range(y):
            print('\n',bar_sequence * x, end = bar)
        print()

    print(grid_line * x, end = plus)

print_grid(5,3)
