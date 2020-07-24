def grid_printer():
    plus = ('+ ' + ('- ' * 4)) * 2
    tally = ('|' + (' ' * 9)) * 3
    print(plus, end='+')
    print()
    print(tally)
    print(tally)
    print(tally)
    print(tally)
    print(plus, end='+')
    print()
    print(tally)
    print(tally)
    print(tally)
    print(tally)
    print(plus, end='+')

grid_printer(3)



def grid_printer_2 (n):
    x = n//2
    y = n+1
    for i in range(1):
        print('+' + (' -' * x) + ' +' + (' -' * x) + ' +')
    for i in range(x):
        if n % 2 >= 1:
            print('|' + (' ' * n) + '|' + (' ' * n) + '|')
        else:
            print('|' + (' ' * y) + '|' + (' ' * y) + '|')
    for i in range(1):
        print('+' + (' -' * x) + ' +' + (' -' * x) + ' +')
    for i in range(x):
        if n % 2 >= 1:
            print('|' + (' ' * n) + '|' + (' ' * n) + '|')
        else:
            print('|' + (' ' * y) + '|' + (' ' * y) + '|')
    for i in range(1):
        print('+' + (' -' * x) + ' +' + (' -' * x) + ' +')

#grid_printer_2(15)



def grid_printer_3 (n,z):
    for i in range (0,n):
        for i in range(0,n):
            print('+', ('- ' * z), end=' ')
        print('+')
        for i in range(0,z):
            for i in range(0,n):
                print('|', (' ' * (z*2)), end=' ')
            print('|')
    for i in range(0,n):
        print('+', ('- ' * z), end=' ')
    print('+')

#grid_printer_3(3,4)