'''
Andrew Garcia
Grid Printer 3
6/2/19
'''

def print_grid2(row_column, size):
    def horizontal():  # creates horizontal sections
        print('\n', end='')
        print('+', end='')
        for number in range(size):  # creates first horizontal side of grid
            print(' - ', end='')
        print('+', end='')
        for number in range(row_column - 1):  # selects number of extra columns
            for number in range(size):  # creates size of grid
                print(' - ' , end='')
            print('+', end='')

    def vertical():  # creates vertical sections
        for number in range(size):  # creates firstv vertical side of grid
            print('\n', end='')
            print('|', end='')
            print(('   ' * size), end='')
            print('|', end='')
            for number in range(row_column - 1):  # selects number of extra rows
                print('   ' * size, end='')  # creates size of grid
                print('|', end='')

    def final_grid():  #combines vertical and horizontal sections
        for number in range(row_column):
            horizontal()
            vertical()
        horizontal()

    final_grid()


row_column, size = int(input("Enter Number of Rows and Columns: ")), int(input("Enter Size of Grid: "))

print_grid2(row_column, size)
