#This program is to print out a grid


def main():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    print_grid(rows, columns)

def print_grid(rows, columns):
    '''Takes in rows and columns numbers it calls both vertical and horizontal functions'''
    for x in range(columns):
        vertical(rows, columns)
        horizontal(rows, columns)
    vertical(rows, columns)


def vertical(rows, columns):
    '''Takes in numberes rows and columns and prints out the vertical line for the grid'''
    row_lines = "-" * rows
    beg_end = "+"
    vertical_line = beg_end + row_lines
    full_line = vertical_line * columns + beg_end
    print(full_line)

def horizontal(rows,columns):
    '''Takes in numbers rows and columns and prints out the horizontal lines for the grid'''
    spaces = " " * (rows)
    line = '|' + spaces
    for x in range(rows):
        line_total = line * (columns + 1)
        print(line_total)

main()