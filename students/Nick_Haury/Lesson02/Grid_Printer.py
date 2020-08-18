'''
Grid_Printer program contains two main functions, which prints out
different grid patters depending on input parameters
'''

# define useful character strings
plus = "+"
dash = "-"
space = " "
v_line = "|"

def print_grid(size):

# takes an int "size" as a parameter and prints out a grid
# of size "size"

    def print_edge_row(size):
        print(2 * (plus + ((size - 1) // 2) * (space + dash) + space) + plus)

    def print_inner_row(size):
        print(2 * (v_line + size * space) + v_line)

    print_edge_row(size)
    for i in range(2):
        for i in range((size - 1) // 2):
            print_inner_row(size)
        print_edge_row(size)

def print_grid2(number, size):

    # takes ints "number" and "size" as parameters and prints out
    # a grid of "number" boxes of "size" size.

    def print_edge_row(number, size):
        print(int(number) * (plus + int(size) * (space + dash) + space) + plus)

    def print_inner_row(number, size):
        print(int(number)*(v_line + (int(size) * 2 + 1) * space) + v_line)
    
    for n in range(number):
        print_edge_row(number, size)
        for s in range(size):
            print_inner_row(number, size)
    print_edge_row(number, size)    

if __name__ == "__main__":
    pass
    # testing grid printing
    # print_grid(3)
    # print_grid(9)
    # print_grid(15)
    # print_grid2(3,4)
    # print_grid2(5,3)