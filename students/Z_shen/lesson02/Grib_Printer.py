def row_one(x,y):
    print('+',end='')
    for i in range(x-1):
        print('-'*y + '+', end='')
    print('-'*y + '+')
def row_two(x,y):
    print('|',end='')
    for i in range(x-1):
        print(' '*y + '|',end='')
    print(' '*y + '|')
def print_grid(x,y):
    row_one(x,y)
    for i in range(x):
        for i in range(y):
            row_two(x,y)
        row_one(x,y)

print_grid(5,3)

