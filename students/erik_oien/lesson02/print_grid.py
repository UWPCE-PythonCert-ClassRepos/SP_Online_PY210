def horizontal_grid(length):
    for i in range(2):
        print('+', end=' ')
        print('- ' * length, end='')
    print('+')

def vertical_grid(length):
    for i in range(length):
        for j in range(2):
            print('|', end=' ')
            print('  ' * length, end='')
        print('|')

def print_grid(n):
    length = int((n-1) / 2)
    horizontal_grid(length)
    for i in range(2):
        vertical_grid(length)
        horizontal_grid(length)

print_grid(3)

print_grid(9)

print_grid(15)
