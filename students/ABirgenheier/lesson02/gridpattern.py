print('Brute forced grid')
print('+', 4*'-', '+', 4*'-', '+')
print('|', 4*' ', '|', 4*' ', '|')
print('|', 4*' ', '|', 4*' ', '|')
print('|', 4*' ', '|', 4*' ', '|')
print('|', 4*' ', '|', 4*' ', '|')
print('+', 4*'-', '+', 4*'-', '+')
print('|', 4*' ', '|', 4*' ', '|')
print('|', 4*' ', '|', 4*' ', '|')
print('|', 4*' ', '|', 4*' ', '|')
print('|', 4*' ', '|', 4*' ', '|')
print('+', 4*'-', '+', 4*'-', '+')
print()
print('Use print_grid(x) or print_grid2(a,b) for customized grids.')


def print_grid(x):
    x = round(x)
    print('+', x*'-', '+', x*'-', '+')
    for y in range(0, x):
        (print('|', x*' ', '|', x*' ', '|'))
    print('+', x*'-', '+', x*'-', '+')
    for y in range(0, x):
        (print('|', x*' ', '|', x*' ', '|'))
    print('+', x*'-', '+', x*'-', '+')


def print_grid2(a, b):
    a = round(a)
    b = round(b)
    for units in range(0, a):
        for units in range(0, a):
            print('+', b*'-', end=' ')
        print('+')
        for dash in range(0, b):
            for units in range(0, a):
                print('|', b*' ', end=' ')
            print('|')
    for units in range(0, a):
        print('+', b*'-', end=' ')
    print('+')
