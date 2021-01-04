#!/usr/bin/env python

# ---------------------------------------------------------------------------- #
# Title: Lesson 2
# Description: Exercise 2.2 - Grid Printer
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-02-2020, Created Grid Printer Function
# ---------------------------------------------------------------------------- #

def generate_grid(num_columns=2, num_rows=2, column_width=4, row_width=4):
    '''
        Display a grid on the std output.

        :param num_columns: (int) Number of columns in the grid
        :param num_rows: (int) Number of rows in the grid
        :param column_width: (int) column width in the grid
        :param row_width: (int) rows width in the grid
        :return: None
    '''

    # Defining separator strings for the corners and borders
    corner_separator = '*'
    vertical_separator = '|'
    horizontal_separator = '-'

    # Generating the string for the row header
    row_header_str = ''
    for j in range(num_columns):
        row_header_str += (corner_separator + (column_width * horizontal_separator))
    row_header_str += corner_separator

    # Generating the string for an inner row element
    inner_row_str = ''
    for j in range(num_columns):
        inner_row_str += (vertical_separator + (column_width * ' '))
    inner_row_str += vertical_separator

    # Generating the grid
    for i in range(num_rows):
        print(row_header_str)
        for k in range(row_width):
            print(inner_row_str)
    print(row_header_str)

def print_grid(cell_size = 4, num_rows_columns = 2):
    '''
        Display a grid on the std output.

        :param num_rows_columns: (int) Number of rows and columns
        :param cell_size: (int) Column and row width
        :return: None
    '''

    try:
        cell_size_int = int(cell_size)
    except ValueError:
        print("You did not provide a valid cell size, so the grid will be displayed with a default size (4)")
        cell_size_int = 4
    try:
        num_rows_columns_int = int(num_rows_columns)
    except ValueError:
        print("You did not provide a valid number of rows and colums, so the grid will be displayed with a default number (2)")
        num_rows_columns_int = 2

    grid_args = {
        'column_width': cell_size_int,
        'row_width': cell_size_int,
        'num_columns': num_rows_columns_int,
        'num_rows': num_rows_columns_int
    }

    generate_grid(**grid_args)


if __name__ == '__main__':

    print("Invoking print_grid() without no arguments passed:")
    print_grid()

    print("Invoking print_grid(cell_size) with an argument that specifies the column & cell size (width): ")
    cell_size = input("How wide do you want the cell to be?: ")
    print_grid(cell_size)

    print("Invoking print_grid(num_rows_columns, cell_size) with arguments that specifies the column & cell size and number: ")
    cell_size = input("How wide do you want the cell to be?: ")
    num_rows_columns = input("How many rows & columns do you want the grid to have?: ")
    print_grid(cell_size, num_rows_columns)
