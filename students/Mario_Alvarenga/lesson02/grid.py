#Mario Alvarenga
#Lesson02
#Grid

# Part 1:Simple Grid
plus = '+ '
minus = '- '
dash = '| '
space = '        '

wall = (dash + space + dash + space + dash)
horizontal = (plus + 4 * minus + plus + 4 * minus + plus)



def grid():
    for i in range(2):
        print(horizontal)
        for j in range(4):
            print(wall)
    print(horizontal)


grid()

# Part 2: Function that takes 1 integer to size  a 2x2 box.
plus = '+'
minus = '-'
dash = '|'
space = ' '

def wall(size):
    return dash + (space * size) + dash + (space * size) + dash
def horizontal(size):
    return plus + space + (minus + space) * size + plus + space + \
           (minus + space) * size + plus


def print_grid(size):  # prints 2x2 grid
    for i in range(2):
        print(horizontal(size))
        for j in range(size):
            print(wall(size * 2 + 1))
    print(horizontal(size))


print_grid(2)


# Part 3: Function that takes 2 inputs,box and grid size

def print_flexible_grid(grid_size, box_size):
    wall = (dash + (space * 2 * box_size) + space) * grid_size + dash
    horizontal = (plus + space + (minus + space) * box_size) * grid_size + plus
   

    for i in range(grid_size):
        print(horizontal)
        for j in range(box_size):
            print(wall)
    print(horizontal)


print_flexible_grid(3, 4)
print_flexible_grid(5, 3)
