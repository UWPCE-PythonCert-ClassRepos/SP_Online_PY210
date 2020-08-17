'''
function print_grid2 takes inputs for number and size, printing
a grid of "number" boxes of "size" size
'''

def print_grid2(number, size):

    # define useful character strings
    plus = "+"
    dash = "-"
    space = " "
    v_line = "|"

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
    # testing grid printing
    print_grid2(3,4)
    print_grid2(5,3)