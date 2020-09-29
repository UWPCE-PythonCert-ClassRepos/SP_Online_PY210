#This program is to print out a grid


def main():
    grid_number = int(input("Grid Number?: "))
    print_grid(grid_number)

def print_grid(grid_number):
   '''Takes in grid_number,and call both the vertical and horizontal function'''
   vertical(grid_number)
    horizontal_loop(grid_number)
    vertical(grid_number)
    horizontal_loop(grid_number)
    vertical(grid_number)


def vertical(grid_number):
    '''Takes in grid_number, and prints out the vertical line of the grid'''
    line_break = grid_number // 2
    line = line_break * '-'
    beg_end = '+'
    complete_line = beg_end + line + beg_end + line + beg_end
    print(complete_line)

def horizontal_loop(grid_number):
    '''Takes in grid_number, and prints out the horizontal line of the grid'''
    line_break = grid_number // 2
    spaces = " " * (line_break - 2)
    for x in range(line_break):
        print('|', spaces, '|', spaces, '|')


main()