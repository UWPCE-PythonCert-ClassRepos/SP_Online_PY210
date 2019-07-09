'''
Andrew Garcia
Grid Printer 1
6/2/19
'''

def print_grid():
    def print_horizontal():
        print("+ - - - - + - - - - +")

    def print_vertical():
        print("|         |         |")

    def print_multiple_vertical():
        print_vertical()
        print_vertical()
        print_vertical()
        print_vertical()

    def entire_grid():
        print_horizontal()
        print_multiple_vertical()
        print_horizontal()
        print_multiple_vertical()
        print_horizontal()

    entire_grid()


print_grid()
