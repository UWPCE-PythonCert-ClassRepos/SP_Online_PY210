
#Prints a simple 3x3 Grid
#Part1

def repeat_line(n):
     n()
     n()

def repeat_lines(n):
    repeat_line(n)
    repeat_line(n)

def print_bar():
    print('+----+----+'),


def print_stick():
    print('|    |    |'),

def print_rows():
    print_bar()
    repeat_lines(print_stick)

def print_gridlines():
    repeat_line(print_rows)
    print_bar()

print_gridlines()



#Part2
def grid_input():
    while True:
        try:
            grid_space = int(input("input grid size\n"))
            if grid_space<2:
                print("invalid integer")
            else:
                return grid_space
        except ValueError:
                print("invalid input")


def print_gridinput():
    length=grid_input()
    width=length
    for n in range(length):
        print(("+" + "-" * width) * length + "+")
        for n in range(length):
            print(("|" + " " * width) * length + "|")
            print(("+" + "-" * width) * length + "+")
        break

print_gridinput()

#Part3

def ask_length():
    while True:
        try:
            grid_length = int(input("Input Grid Rows\n"))
            if grid_length<2:
                print("invalid integer")
            else:
                return grid_length
        except ValueError:
                print("invalid input")

def ask_width():
    while True:
        try:
            grid_width = int(input("Input Grid Columns\n"))
            if grid_width<2:
                print("invalid integer")
            else:
                return grid_width
        except ValueError:
                print("invalid input")

def print_gridinput():
    width= ask_width()
    length= ask_length()
    for n in range(width):
        print(("+" + "-" * length) * width + "+")
        for n in range(length):
            print(("|" + " " * length) * width + "|")
            print(("+" + "-" * length) * width + "+")
        break

print_gridinput()
