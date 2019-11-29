#!/usr/bin/env python3

plus = '+'
minus = ' -'
pipe = '|'
space = ' '

def main():
    print("Printing simple grid i.e. Part 1 of lesson02...")
    print_simple_grid()
    print("Printing grid with size argument i.e. Part 2 of lesson02...")
    print_grid(8)
    print_grid()
    print_grid(15)
    print_grid(6)
    print_grid(3)
    print("Printing grid with rows and columns and cell size arguments i.e. Part 3 of lesson02...")
    print_grid_advanced(5, 3)
    print_grid_advanced(3, 4)
    print_grid_advanced(1, 1)

def print_simple_grid():
    '''
    Part 1: write a function that prints a grid w/ two rows and four columns
    '''

    print("%s%s%s%s%s%s%s%s" % (plus, minus * 4, space, plus, minus * 4, space, plus, '\r'))
    for x in range(0, 4):
        print("%s%s%s%s%s%s" % (pipe, space * 9, pipe, space * 9, pipe, '\r'))
    print("%s%s%s%s%s%s%s%s" % (plus, minus * 4, space, plus, minus * 4, space, plus, '\r'))
    for x in range(0, 4):
        print("%s%s%s%s%s%s" % (pipe, space * 9, pipe, space * 9, pipe, '\r'))

    return None

def print_grid(size=3):
    '''
    Part 2: Write a function print_grid(n) that takes one integer argument and prints a grid just like before, but the
    size of the grid is given by the argument
    '''

    offset = size if size % 2 != 0 else size + 1

    print("%s%s%s%s%s%s%s%s" % (plus, minus * (size // 2), space, plus, minus * (size // 2), space, plus, '\r'))
    for x in range(0, (size // 2)):
        print("%s%s%s%s%s%s" % (pipe, space * offset, pipe, space * offset, pipe, '\r'))
    print("%s%s%s%s%s%s%s%s" % (plus, minus * (size // 2), space, plus, minus * (size // 2), space, plus, '\r'))
    for x in range(0, (size // 2)):
        print("%s%s%s%s%s%s" % (pipe, space * offset, pipe, space * offset, pipe, '\r'))
    print("%s%s%s%s%s%s%s%s" % (plus, minus * (size // 2), space, plus, minus * (size // 2), space, plus, '\r'))

    return None

def print_grid_advanced(row_cols=1, cell_size=1):
    '''
    Part 3:
    Write a function that draws a grid with a specified number of rows and columns, and with each cell a given size
    '''
    for x in range(0, row_cols * 2 + 1):
        if x % 2 == 0:
            print("%s%s%s" % (plus, minus * cell_size, space) * row_cols, end=""), print("%s%s" % (plus, '\r'))
        else:
            for y in range(0, cell_size):
                print("%s%s" % (pipe, space * (cell_size * 2 + 1)) * row_cols, end=""), print("%s%s" % (pipe, '\r'))
    return None


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running %s as imported module", __file__)
