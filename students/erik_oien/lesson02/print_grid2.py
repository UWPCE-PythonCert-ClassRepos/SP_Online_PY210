def horizontal_grid(grid, units):
    for i in range(grid):
        print('+', end=' ')
        print('- ' * units, end='')
    print('+')

def vertical_grid(grid, units):
    for i in range(units):
        for j in range(grid):
            print('|', end=' ')
            print('  ' * units, end='')
        print('|')

def print_grid2(grid, units):
    horizontal_grid(grid, units)
    for i in range(grid):
        vertical_grid(grid, units)
        horizontal_grid(grid, units)

print_grid2(3, 4)

print_grid2(5, 3)
