#Part1
#Write a function that draws a grid like the following:

# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

def row():
   print('+ - - - - + - - - - +')

def do_four():
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')

def execute():
    row()
    do_four()
    row()
    do_four()
    row()


#Part 2:
#Write a function print_grid(n) that takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument.

def grid_part_2(z):
        n = int(z)
        plus_line = '+' + ((' ''-'' ') * n )
        for r in range(2):
                print(plus_line * 2 + "+" + ' ')
                for l in range(n):
                        print (("|" + "   " * n) * 2 + "|")
        print(plus_line * 2 + "+" + ' ')

#Part 3:
# A function with two parameters
# Write a function that draws a similar grid with a specified number of rows and columns, and with each cell a given size.

def grid_part_3(a,b):
    plus_line = '+' + (' ''-'' ' * b)
    for r in range(a):
        print((plus_line * a) + '+'' ')
        for l in range(b):
            print((('|'+('   ' * b)) * (a)) + '|')
    print((plus_line * a) +'+')