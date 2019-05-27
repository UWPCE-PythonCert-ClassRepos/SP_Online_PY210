
#Prints a simple 3x3 Grid

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




