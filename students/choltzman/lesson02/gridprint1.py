#!/usr/bin/env python3


def main():
    print_grid(9)


def print_grid(n):
    grid_horizontal(n)
    grid_vertical(n)
    grid_horizontal(n)
    grid_vertical(n)
    grid_horizontal(n)


def grid_horizontal(n):
    # This looks wonky with even numbers, but will always be the right length.
    print('+', end='')
    for i in range(n):
        if i % 2 == 0:
            print(' ', end='')
        else:
            print('-', end='')
    print('+', end='')
    for i in range(n):
        if i % 2 == 0:
            print(' ', end='')
        else:
            print('-', end='')
    print('+')


def grid_vertical(n):
    for _ in range(int(n/2)):
        print('|' + ' ' * n + '|' + ' ' * n + '|')


if __name__ == "__main__":
    main()
