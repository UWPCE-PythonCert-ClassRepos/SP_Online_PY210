#!/usr/bin/env python3


def main():
    print_grid(5, 3)


def print_grid(x, y):
    for _ in range(x):
        grid_horizontal(x, y)
        grid_vertical(x, y)
    grid_horizontal(x, y)


def grid_horizontal(x, y):
    for _ in range(x):
        print('+' + ' -' * y + ' ', end='')
    print('+')


def grid_vertical(x, y):
    for _ in range(y):
        for _ in range(x):
            print('|' + '  ' * y + ' ', end='')
        print('|')


if __name__ == "__main__":
    main()
