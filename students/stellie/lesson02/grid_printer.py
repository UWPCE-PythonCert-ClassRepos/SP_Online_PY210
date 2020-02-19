def h_line(x, y):
    # To formulate + - - - - + - - - - +, one '+' for every '-'
    for _i in range(x):
        print('+', end=' ')
        for _j in range(y):
            print('-', end=' ')
    print('+')
# h_line(2, 4)


def v_line(x, y):
    # To formulate |         |         |, one '|' for every space
    for _i in range(x):
        print('|', end=' ')
        for _j in range(y):
            print(' ', end=' ')
    print('|')
# v_line(2, 4)


def print_grid(x, y):
    print('Size:', x, '(columns)', 'x', y, '(units)')
    for _i_row in range(x):
        h_line(x, y)
        for _j_size in range(y):
            v_line(x, y)
    return h_line(x, y)


def print_grid_2(z):
    x = 2
    y = int((z - 1) / x)
    print('Size:', x, '(columns)', 'x', y, '(units)')
    for _i_row in range(x):
        h_line(x, y)
        for _j_size in range(y):
            v_line(x, y)
    return h_line(x, y)


# Part 1
print('Part 1')
print_grid(2, 4)
print('\n')

# Part 2
print('Part 2')
print_grid_2(3)
print('\n')

# Part 3
print('Part 3')
print_grid(2, 7)
print('\n')
