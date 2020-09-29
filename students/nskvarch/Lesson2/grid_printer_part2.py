#Part 2 of the grid printer exercise, created by Niels Skvarch
plus = '+'
minus = '-'
pipe = '|'
space = ' '

def print_grid(n):
    print(plus, n * minus, plus, n * minus, plus)
    for i in range(n):
        print(pipe, n * space, pipe, n * space, pipe)
    print(plus, n * minus, plus, n * minus, plus)
    for i in range(n):
        print(pipe, n * space, pipe, n * space, pipe)
    print(plus, n * minus, plus, n * minus, plus)

x = int(input("What size grid would you like?: "))
print_grid(x)
