# Isabella Kemp
# 1/8/20
# Grid Printer: Exercise 2.2

# part 1: Draw simple grid.
plus = '+ '
minus = '- '
dash = '| '
space = '        '

horizontal = (plus + 4 * minus + plus + 4 * minus + plus)
wall = (dash + space + dash + space + dash)


def grid():
    for i in range(2):
        print(horizontal)
        for j in range(4):
            print(wall)
    print(horizontal)


grid()

# part 2: Create a function that takes 1 integer to dynamically size a 2x2 box.
# newly defined global variables
plus = '+'
minus = '-'
dash = '|'
space = ' '


def horizontal(size):
    return plus + space + (minus + space) * size + plus + space + \
           (minus + space) * size + plus


def wall(size):
    return dash + (space * size) + dash + (space * size) + dash


def print_grid(size):  # prints 2x2 grid
    for i in range(2):
        print(horizontal(size))
        for j in range(size):
            print(wall(size * 2 + 1))
    print(horizontal(size))


print_grid(2)


# part 3: create a function that takes 2 inputs, grid size and box size.
# For example, grid_size = 1 would create a grid which is one box only.
# grid_size = 3 would create a grid of 3 by 3. box_size = 2 for example
# would create 2 dash signs and minus signs for the size of the box.
def print_flexible_matrix(grid_size, box_size):
    horizontal = (plus + space + (minus + space) * box_size) * grid_size + plus
    wall = (dash + (space * 2 * box_size) + space) * grid_size + dash

    for i in range(grid_size):
        print(horizontal)
        for j in range(box_size):
            print(wall)
    print(horizontal)


print_flexible_matrix(3, 6)
